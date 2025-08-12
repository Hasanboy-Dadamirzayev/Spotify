from datetime import timedelta

from rest_framework.serializers import *
from .models import *
from django.core.validators import FileExtensionValidator


class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongsTableSerializer(ModelSerializer):

    file = FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )

    class Meta:
        model = Songs
        fields = "__all__"

    def validate_duration(self, duration):
        h, m, s = map(int, duration.split(":"))  # "01:02:01" -> 1, 2, 1
        if timedelta(hours=h, minutes=m, seconds=s) > timedelta(minutes=7):
            raise ValidationError("Davomiylik 7 daqiqadan oshmasligi kerak")
        return duration

