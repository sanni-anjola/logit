from django.http import HttpResponse
from django.shortcuts import render

# class UserViewSet()
# Create your views here.
def create_account(request):
    return HttpResponse('Create account')


def hello(request):
    return HttpResponse('Hello')


def login(request):
    return HttpResponse('login')


def change_password(request):
    return HttpResponse('Change password')


def view_profile(request):
    return HttpResponse('View profile')


def create_profile(request):
    return HttpResponse('create profile')


def update_profile(request):
    return HttpResponse('Update profile')
