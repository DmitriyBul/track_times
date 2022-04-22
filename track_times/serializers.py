from rest_framework.serializers import ModelSerializer

from track_times.models import UserTime


class TimesSerializer(ModelSerializer):
    class Meta:
        model = UserTime
        fields = '__all__'
