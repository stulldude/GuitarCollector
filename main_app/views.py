from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Guitar, Amp
from .forms import ModificationForm
from main_app import models


# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, gtr_id):
    guitar = Guitar.objects.get(id=gtr_id)
    amps_not_favorite = Amp.objects.exclude(id__in = guitar.amps.all().values_list('id'))
    modification_form = ModificationForm()
    return render(request, 'guitars/detail.html', { 
        'guitar': guitar, 'modification_form': modification_form,
        'amps': amps_not_favorite 
    })

def add_mod(request, gtr_id):
    form = ModificationForm(request.POST)
    if form.is_valid():
        new_mod = form.save(commit=False)
        new_mod.gtr_id = gtr_id
        new_mod.save()
    return redirect('detail', gtr_id=gtr_id)

def assoc_amp(request, gtr_id, amp_id):
    Guitar.objects.get(id=gtr_id).amps.add(amp_id)
    return redirect('detail', gtr_id=gtr_id)

def unassoc_amp(request, gtr_id, amp_id):
    Guitar.objects.get(id=gtr_id).amps.remove(amp_id)
    return redirect('detail', gtr_id=gtr_id)

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['brand', 'gtrmodel', 'year', 'color']
    success_url = '/guitars/'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = '__all__'

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'

class AmpCreate(CreateView):
    model = Amp
    fields = '__all__'

class AmpUpdate(UpdateView):
    model = Amp
    fields = '__all__'

class AmpDetail(DetailView):
    model = Amp

class AmpDelete(DeleteView):
    model = Amp
    success_url = '/amps/'

class AmpList(ListView):
    model = Amp