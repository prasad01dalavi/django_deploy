from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student


class SampleData(APIView):

    def get(self, request):
        response = []
        students = Student.objects.all()
        for student in students:
            response.append({
                "name": student.name,
                "age": student.age,
                "roll_number": student.roll_number
            })

        return Response(response)
