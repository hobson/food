# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def chart(request):
    nodes = ["node 1", 'node2', 'node3', 'node4']
    edges = [{'source': 1, 'target': 2},{'source': 2, 'target': 3},{'source': 3, 'to': 0}, {'source': 1, 'target': 3},{'source': 2, 'target': 0}]
    return render(request, 'charts/index.html', {'data': {'nodes': nodes, 'edges': edges}})

def index(request):
    return HttpResponse("This is the index page for totalgood.com in the food.totalgood.food app.")

def home(request):
    return HttpResponse("This is the home page for totalgood.com in the food.totalgood.food app.")
