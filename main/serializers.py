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
        required=False,  # Fayl ixtiyoriy bo‘lishi uchun
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )

    class Meta:
        model = Songs
        fields = "__all__"

    def validate_duration(self, value):
        """Davomiylik 7 daqiqadan oshmasligi kerak."""
        max_duration = timedelta(minutes=7)
        if value > max_duration:
            raise ValidationError("Qo'shiq davomiyligi 7 daqiqadan oshmasligi kerak.")
        return value