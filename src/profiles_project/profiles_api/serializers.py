from rest_framework import serializers

class FirstSerializer(serializers.Serializer):
    """
        Serializes a name field.
    """

    name = serializers.CharField(max_length=10)