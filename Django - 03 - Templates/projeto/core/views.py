from django.shortcuts import render

from django.shortcuts import render

def index(request):
  context =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
  return render(request, 'index.html', context)