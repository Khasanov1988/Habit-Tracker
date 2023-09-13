from celery import shared_task
import json
from datetime import datetime, timedelta, time as datetime_time

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from habits.models import Habit


@shared_task
def create_task(pk):
    """
    Function create periodic task
    """
    print('Мы тут были')
    habit = Habit.objects.get(pk=pk)
    day_interval = habit.period
    time = habit.time  # Исправление опечатки в названии поля времени

    # Создаем интервал для повтора
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=day_interval,
        period=IntervalSchedule.DAYS,
    )

    # Создаем объект времени для указанного времени
    reminder_time = datetime_time(hour=time.hour, minute=time.minute)

    # Вычисляем дату и время следующего выполнения задачи
    now = datetime.utcnow()
    next_execution_time = datetime.combine(now.date(), reminder_time)

    if now > next_execution_time:
        # Если текущее время больше времени выполнения,
        # добавляем один день к дате
        next_execution_time += timedelta(days=1)

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Sending message by Telegram to habit {pk}',
        task='habits.tasks.send_reminder',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'chat_id': habit.owner.telegram_chat_id,
            'text': habit.__str__()
        }),
        expires=next_execution_time + timedelta(seconds=30),
        start_time=next_execution_time,  # Указываем начальное время выполнения
    )


@shared_task
def send_reminder(chat_id, text, **kwargs):
    pass
