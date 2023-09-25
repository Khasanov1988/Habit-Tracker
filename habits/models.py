from django.db import models


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, verbose_name='user')  # creator of the habit
    location = models.CharField(max_length=150, verbose_name='location')  # location where the habit should be performed
    time = models.TimeField(default='00:00', null=True, blank=True, verbose_name='time')  # time when the habit should be performed
    action = models.TextField(verbose_name='action')  # action that represents the habit
    is_pleasant = models.BooleanField(default=False, verbose_name='pleasant habit flag')  # a flag indicating if the habit is pleasant
    pleasant_habit = models.ForeignKey('habits.Habit', on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name='related habit') # a habit that is related to another habit
    period = models.PositiveSmallIntegerField(default=1, verbose_name='frequency') # how often the habit should be performed for reminders in days
    reward = models.CharField(max_length=150, default=None, null=True, blank=True, verbose_name='reward') # what the user should reward themselves with after completion
    duration = models.PositiveSmallIntegerField(default=120, verbose_name='completion time') # the time the user is expected to spend on completing the habit
    is_publish = models.BooleanField(default=False, verbose_name='public flag')  # habits can be made public so that other users can use them as examples

    def __str__(self):
        # String representation of the object
        return f'I need to {self.action} now at {self.location}'

    class Meta:
        verbose_name = 'habit' # Configuration for the name of a single object
        verbose_name_plural = 'habits' # Configuration for the name of a set of objects
