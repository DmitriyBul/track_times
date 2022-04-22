import datetime

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from track_times import serializers
from track_times.models import UserTime, UserActivity
from track_times.serializers import TimesSerializer


class UserTimeViewSet(ModelViewSet):
    queryset = UserTime.objects.all()
    serializer_class = TimesSerializer


class UserDetailView(ModelViewSet):
    serializer_class = serializers.TimesSerializer

    def get_queryset(self, *args, **kwargs):
        date = datetime.datetime.today()
        week = date.strftime("%m")
        user_id = self.kwargs['id']
        today = date.today()
        today_qs = UserActivity.objects.filter(user__id=user_id, start__year=today.year, start__month=today.month,
                                               start__day=today.day)
        week_qs = UserActivity.objects.filter(user__id=user_id, start__week__lte=week)
        # queryset = {'week_qs': week_qs, 'today_qs': today_qs}
        return week_qs
