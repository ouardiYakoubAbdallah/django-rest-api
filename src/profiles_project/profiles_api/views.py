from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class FirstView(APIView):
    """
        Basic APIView.
    """

    def get(self, request, format=None):

        django_apiview = [
            'Django is a high-level Python Web framework',
            'Django encourages rapid development and clean, pragmatic design.',
            'Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.',
            'It’s free and open source.'
        ]

        return Response({
            'message': 'Hello view!',
            'view': django_apiview
        })