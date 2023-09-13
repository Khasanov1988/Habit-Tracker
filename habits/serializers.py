from rest_framework import serializers

from habits.models import Habit
from habits.validators import *


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardValidator(is_pleasant_field='is_pleasant', pleasant_habit_field='pleasant_habit', reward_field='reward'),
            DurationValidator(field='duration'),
            PleasantValidator(field='pleasant_habit'),
            PeriodValidator(field='period'),
        ]

