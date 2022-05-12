from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'catalog/dashboard.html')

def loginPage(request):
    return render(request, 'collabapp/hello.html')