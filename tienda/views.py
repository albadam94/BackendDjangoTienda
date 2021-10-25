from django.shortcuts import render

# Create your views here.
from tienda.models import Tienda

# Create your views here.

def tienda(request):

    tienda=Tienda.objects.all()
    return render(request, "tienda/tienda.html", {"tienda": tienda})