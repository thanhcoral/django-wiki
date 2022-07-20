from django.contrib.auth import get_user_model
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        max_length=50, 
        required=True,
        allow_blank=False,
        trim_whitespace=False,
        error_messages= {
            "required": "required",
            "blank": "blank",
            "max_length": "max_length",
        } 

    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'full_name')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)