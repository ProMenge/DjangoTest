from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
# Create your views here.

class PostView(generic.View): 
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')