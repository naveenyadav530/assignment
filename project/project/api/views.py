
from rest_framework.views import APIView
from rest_framework import permissions
from api.serializers import FormSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from webapp.models import SignUp
from django.shortcuts import get_object_or_404
from django.http import Http404


class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SignUp.objects.all()
    serializer_class = FormSerializer
