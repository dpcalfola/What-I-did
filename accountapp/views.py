from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class AccountCreateView(CreateView):
    model = User
