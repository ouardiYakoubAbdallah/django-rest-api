from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """
        A serializer for our UserProfile object.
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }