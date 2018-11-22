'''
Author: Kris Shin
Edit Time: 18-11-11 17:02:33
'''
from django.conf.urls import url

from names import views

urlpatterns = [url(r'^$', views.show_all, name='show_all')]
