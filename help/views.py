from django.shortcuts import render

# Create your views here.

def helpPage(request):
	return render(request, 'help/helpPage.html', dict())