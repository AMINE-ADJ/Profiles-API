from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""
    name = serializers.CharField(max_length=10)
    nickname = serializers.CharField(max_length=5)