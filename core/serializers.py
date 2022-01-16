from rest_framework import serializers


class PresignedURLSerializer(serializers.Serializer):
    object_name = serializers.CharField()
    type = serializers.CharField()
