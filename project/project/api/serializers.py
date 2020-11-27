
from rest_framework import serializers
from rest_framework.validators import   ValidationError
import re
from webapp.models import SignUp


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = "__all__"

