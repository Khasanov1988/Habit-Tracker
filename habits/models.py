from datetime import datetime

from django.db import models
from django.utils import timezone


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='пользователь')  # создатель привычки
    location = models.CharField(max_length=150, verbose_name='место')  # время, когда необходимо выполнять привычку
    time = models.TimeField(default='00:00', null=True, blank=True, verbose_name='время')  # время, когда необходимо выполнять привычку
    action = models.TextField(verbose_name='действие')  # действие, которое представляет из себя привычка
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')  # привычка, которую можно привязать к выполнению полезной привычки
    pleasant_habit = models.ForeignKey('habits.Habit', on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name='связанная привычка') # привычка, которая связана с другой привычкой
    period = models.PositiveSmallIntegerField(default=1, verbose_name='периодичность') # периодичность выполнения привычки для напоминания в днях
    reward = models.CharField(max_length=150, default=None, null=True, blank=True, verbose_name='вознаграждение') # чем пользователь должен себя вознаградить после выполнения
    duration = models.PositiveSmallIntegerField(default=120, verbose_name='время на выполнение') # время, которое предположительно потратит пользователь на выполнение привычки
    is_publish = models.BooleanField(default=False, verbose_name='признак публичности')  # привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки

    def __str__(self):
        # Строковое отображение объекта
        return f'Мне нужно {self.action} сейчас в {self.location}'

    class Meta:
        verbose_name = 'привычка' # Настройка для наименования одного объекта
        verbose_name_plural = 'привычки' # Настройка для наименования набора объектов