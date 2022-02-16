from django.shortcuts import render
from django.http import HttpResponse
from .models import Memories

def profile(request):
    latest_memories_list = Memories.objects.order_by('-date_memorie')
    context = {'latest_memories_list': latest_memories_list}

    return render(request, 'main/profile.html', context)
