from django.shortcuts import render
from django.http import HttpResponse
from .models import Memories
from .forms import MemoryForm

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

def add_memory(request):
    return render(request, 'main/add_memory.html')


def check_memory(request):
    if request.GET:
        address = request.GET
        print(address)
        return HttpResponse("OK")
    else:
        return HttpResponse('NO')


def get_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)

        if form.is_valid():
            print(form.data['memory_name'], '###############################################')
            return HttpResponse('<h1>Form is all right</h1>')
    else:
        form = MemoryForm()
        print('FORM IS BEAD', '###############################################')
    
    return render(request, 'main/add_memory.html', {'form': form})


