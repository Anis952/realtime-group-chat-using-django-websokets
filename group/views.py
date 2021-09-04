from django.shortcuts import render


def home(request):
    return (request, 'group/index.html'),

