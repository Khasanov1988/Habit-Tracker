from celery import shared_task
import json
from datetime import datetime, timedelta, time as datetime_time

from django.core.exceptions import ObjectDoesNotExist
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def create_task(pk):
    """
    Function creates a periodic task
    """
    habit = Habit.objects.get(pk=pk)
    day_interval = habit.period
    time = habit.time  # Fixing a typo in the field name

    # Create an interval for repetition
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=day_interval,
        period=IntervalSchedule.DAYS,
    )

    # Create a time object for the specified time
    reminder_time = datetime_time(hour=time.hour, minute=time.minute)

    # Calculate the date and time of the next task execution
    now = datetime.utcnow()
    next_execution_time = datetime.combine(now.date(), reminder_time)

    if now > next_execution_time:
        # If the current time is greater than the execution time,
        # add one day to the date
        next_execution_time += timedelta(days=1)

    # Create a task for repetition
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Sending message by Telegram to habit {pk}',
        task='habits.tasks.send_reminder',
        args=json.dumps([habit.owner.telegram_chat_id, str(habit)]),
        kwargs=json.dumps({
            'chat_id': habit.owner.telegram_chat_id,
            'text': habit.__str__()
        }),
        expires=next_execution_time + timedelta(seconds=30),
        start_time=next_execution_time,  # Specify the initial execution time
    )


@shared_task
def delete_task(pk):
    """ Function deletes a periodic task"""
    try:
        task = PeriodicTask.objects.get(name=f'Sending message by Telegram to habit {pk}')
        task.delete()
    except ObjectDoesNotExist:
        print(f"Task with the name 'Sending message by Telegram to habit {pk}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


@shared_task
def send_reminder(*args, **kwargs):
    """ Function sends a reminder message"""
    send_telegram_message(kwargs['chat_id'], kwargs['text'])
