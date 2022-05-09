from django.shortcuts import render

from django.http import HttpResponse


def index(req):
    return HttpResponse("Hello, user. You're at the chat index.")