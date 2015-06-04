from django.shortcuts import render
#from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html')

def model_page(request):
	return render(request, 'models.html')
