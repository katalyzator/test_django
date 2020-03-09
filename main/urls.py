from django.urls import path

from main.views import index_view, application_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('applications/', application_view, name='application_view')
]
