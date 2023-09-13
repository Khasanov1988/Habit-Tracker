from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('habits/', HabitListAPIView.as_view(), name='habits-list'),
    path('habits/public/', PublicHabitListAPIView.as_view(), name='public-habits-list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits-get'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]
