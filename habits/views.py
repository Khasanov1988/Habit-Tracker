from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwnerOrStaff
from habits.serializers import HabitSerializer
from habits.tasks import create_task, delete_task


class HabitCreateAPIView(generics.CreateAPIView):
    """Habit create endpoint"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()
        create_task.delay(new_habit.pk)


class HabitListAPIView(generics.ListAPIView):
    """Habit list endpoint"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
    pagination_class = HabitPaginator


class PublicHabitListAPIView(generics.ListAPIView):
    """Public habit list endpoint"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_publish=True)
    permission_classes = [IsAuthenticated]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Habit detail view endpoint"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Habit update endpoint"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Habit delete endpoint"""
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]

    def perform_destroy(self, instance):
        delete_task.delay(instance.pk)
        return super().perform_destroy(instance)
