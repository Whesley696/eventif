
from django.contrib import admin
from django.urls import path
from subscriptions.views import new, detail
app_name = 'subscriptions'
urlpatterns = [
  path('inscricao/', new, name='new'),
  path('<int:pk>/', detail, name='detail')

]


