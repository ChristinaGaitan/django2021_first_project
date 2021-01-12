from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  date_dictionary = {'insert_me': 'Hello I am from view.py!'}
  return render(request, 'first_app/index.html', context=date_dictionary)
