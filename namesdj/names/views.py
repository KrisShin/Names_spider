'''
Author: Kris Shin
Edit Time: 18-11-11 16:37:41
'''
from django.shortcuts import render
from django.http import JsonResponse

class Names(View):
    def get(self, request):
        return HttpResponse('hello world')