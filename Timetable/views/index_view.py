from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={'user_name': '[REDACTED]', 'items': ['item1', 'item2']})
