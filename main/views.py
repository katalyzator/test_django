from django.shortcuts import render

from main.models import Application


def index_view(request):
    applications = Application.objects.filter(status='opened', name='')

    template_name = 'index.html'
    context = {'applications': applications}

    return render(request, template_name, context)


def application_view(request):
    template_name = 'applications.html'
    context = {}

    return render(request, template_name, context)
