from django.shortcuts import render
from app.models import *
from django.views.generic import ListView
# Create your views here.

class SchoolList(ListView):
    model=School
    context_object_name='schools'

    #template_name='app/school_list.html'
    #queryset=school.objects.filter(name='jspinder')

    ordering=['name']