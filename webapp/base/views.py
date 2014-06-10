""" Views for the base application """

from django.contrib.auth import get_user_model
from django.shortcuts import render


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

User = get_user_model()
