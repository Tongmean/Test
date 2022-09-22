from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def LoginPage(request):
    
#     return HttpResponse("hello")
    
def LoginPage(request):

    return render(request, 'LoginPage.html')