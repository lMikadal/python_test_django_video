from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

test_data = [
    {'id': 1, 'txt': 'lorem1'},
    {'id': 2, 'txt': 'lorem2'}
]

# test_link = [
#     'home',
#     'page2',
#     'page3'
# ]

def test(request):
    return HttpResponse('<h1>test=>HttpResponse</h1>')

def testid(request, id):
    return HttpResponse('<h1>test id = ' + str(id) + '</h1>')

def testpage(request):
    # context = { 'link': test_link}
    return render(request, 'app_2/index.html')#, context)

def testpage2(request, id):
    # context = { 'id': id, 'link': test_link }
    one_data = None
    try:
        one_data = [ d for d in test_data if d['id'] == id][0]
    except IndexError:
        print('No index')
    context = { 'data': one_data }
    return render(request, 'app_2/page2.html', context)#, context)

def testpage3(request):
    context = { 'data': test_data }#, 'link': test_link }
    return render(request, 'app_2/page3.html', context)