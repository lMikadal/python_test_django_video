from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import tPosition
from app_2.forms import TestForm

# Create your views here.

# test_data = [
#     {'id': 1, 'txt': 'lorem1'},
#     {'id': 2, 'txt': 'lorem2'}
# ]

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

def testpage2(request, d_id):
    # context = { 'id': id, 'link': test_link }
    one_data = None
    # try:
    #     one_data = [ d for d in test_data if d['id'] == id][0]
    # except IndexError:
    #     print('No index')
    try:
        one_data = tPosition.objects.get(id=d_id)
    except:
        print('No id')
    context = { 'data': one_data }
    return render(request, 'app_2/page2.html', context)#, context)

def testpage3(request):
    # context = { 'data': test_data }#, 'link': test_link }
    position = tPosition.objects.order_by('id')
    context = { 'data': position }
    return render(request, 'app_2/page3.html', context)

def testForm(request):
    form = TestForm()
    context = {'form': form}
    return render(request, 'app_2/form.html', context)#, context)

def testInsert(request):
    if request.method == "POST":
       form = TestForm(request.POST)
       if form.is_valid():
            form.save()
            return HttpResponseRedirect('page3')
    return render(request, 'app_2/index.html')