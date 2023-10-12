from django.http import HttpResponse
from django.shortcuts import render

from cadastro.forms import CrachaForm
from cadastro.models import Cracha


def home(request):
    form = Cracha.objects.all()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)


def add(request):
    form = None
    if request.method == 'POST':
        form = CrachaForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('Form not valid')
            return HttpResponse('ola')
        print('Form not valid')
    else:
        form = CrachaForm()
    return render(request, 'add.html', {'form': form})


def detalhes(request):
    return render(request, 'detalhes.html')
