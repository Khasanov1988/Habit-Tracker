from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit


class RewardValidator:
    def __init__(self, is_pleasant_field, pleasant_habit_field, reward_field):
        self.is_pleasant_field = is_pleasant_field
        self.pleasant_habit_field = pleasant_habit_field
        self.reward_field = reward_field

    def __call__(self, data):
        is_pleasant = data.get(self.is_pleasant_field)
        pleasant_habit = data.get(self.pleasant_habit_field)
        reward = data.get(self.reward_field)

        if is_pleasant and (pleasant_habit is not None or reward is not None):
            raise serializers.ValidationError(
                'There can be no reward or link to another habit for a pleasurable habit.')
        elif not is_pleasant and pleasant_habit is None and reward is None:
            raise serializers.ValidationError(
                'For a non-pleasant habit, you should set the "pleasant_habit" or "reward" field')
        elif pleasant_habit is not None and reward is not None:
            raise serializers.ValidationError('Cannot set both "pleasant_habit" and "reward" fields at the same time')


class DurationValidator:
    """
    Check that the duration should not be more than 120 seconds
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if tmp_val > 120:
                raise ValidationError('Duration cannot be more than 120 seconds')


class PleasantValidator:
    """
    Check that only habits with a sign of a pleasant habit can be linked to other habits
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if not tmp_val.is_pleasant:
                raise ValidationError('Only habits with a sign of a pleasant habit can be linked to other habits')


class PeriodValidator:
    """
    Check that a habit cannot be performed less than once every 7 days
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if tmp_val > 7:
                raise ValidationError('Do not perform the habit less than once every 7 days')
