'''
Author: Kris Shin
Edit Time: 18-11-11 16:37:41
'''
from django.shortcuts import render

from names.models import NamesModel


def show_all(request):
    if request.method == 'GET':
        return render(request, 'first_names.html', {'names': NamesModel.objects.all()})
