
from django.shortcuts import get_object_or_404, render

from cadastro.models import Cracha


def detalhes(request, pk):
    cracha = get_object_or_404(Cracha, pk=pk)
    context = {
        'cracha': cracha
    }
    return render(request, 'detalhes.html', context)
