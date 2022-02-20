from django.shortcuts import render
from django.http import HttpResponse
from .models import Memories

def profile(request):
    latest_memories_list = Memories.objects.all()
    context = {'latest_memories_list': latest_memories_list}

    return render(request, 'main/profile.html', context)

def api_test(request, name_request):
    if name_request == 'db_all':
        memorie_list = Memories.objects.all()
        context = {'memorie_list': memorie_list}
    else:
        context = {}
    return render(request, 'main/apihtml.html', context)

'''def save_events_json(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
    return HttpResponse("OK")

def add_memory_place(request, q):
    result = ''
    if 'address' in request.POST:
        result = request.POST['address']
        
    return render(request, 'main/add_memory.html', context = {'name': result})'''

def add_memory(request):
    return render(request, 'main/add_memory.html')


def check_memory(request):
    if request.GET:
        print('asdasdasd')
        address = request.GET
        print(address, '#################################################')
        return HttpResponse("OK")
    else:
        return HttpResponse('NO')

'''def add_memory_place(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
    return render(request, 'main/test_ajax.html')'''
        

