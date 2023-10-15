from django.db.models import Q
from django.shortcuts import redirect, render

from cadastro.forms import CrachaForm
from cadastro.models import Cracha


def home(request):
    form = Cracha.objects.all().order_by('nome')
    context = {
        'form': form
    }
    return render(request, 'home.html', context)


def search(request):
    Keyword = request.GET.get('Keyword', '')
    form = Cracha.objects.filter(Q(nome__icontains=Keyword))
    context = {
        'form': form}
    return render(request, 'home.html', context)


def add(request):
    form = None
    if request.method == 'POST':
        form = CrachaForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('Form not valid')
            return redirect('home')
        print('Form not valid')
    else:
        form = CrachaForm()
    return render(request, 'add.html', {'form': form})
