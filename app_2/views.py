from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse('<h1>test=>HttpResponse</h1>')

def testid(request, id):
    return HttpResponse('<h1>test id = ' + str(id) + '</h1>')

def testpage(request):
    return render(request, 'app_2/index.html')

def testpage2(request, id):
    return render(request, 'app_2/page2.html', context={'id':id})
