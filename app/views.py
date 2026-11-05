from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os


def home_view(request):
    pages = {
        'Главная страница': '/current_time/',
        'Текущее время': '/current_time/',
        'Рабочая директория': '/workdir/',
    }
    return render(request, 'app/home.html', {'pages': pages})


def time_view(request):
    now = datetime.now().strftime('%H:%M:%S')
    return HttpResponse(f'Текущее время: {now}')


def workdir_view(request):
    items = os.listdir('.')
    html = '<h1>Содержимое рабочей директории</h1><ul>'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul>'
    return HttpResponse(html)
