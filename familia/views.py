from multiprocessing import context
from django.shortcuts import render

from familia.models import familia


def mama(request):
    mama = familia.objects.create(name = "vanesa", tipo_de_familia = "madre", age = 32)
    
    context = {
        "mama" : mama
     }

    return render(request, "mama.html",context=context)

def papa(request):
    papa = familia.objects.create(name = "norberto", tipo_de_familia = "padre", age = 41)
    context = {
        "papa": papa
    }
    return render(request,"papa.html", context=context)

def abuela(request):
    abuela = familia.objects.create(name = "noemi", tipo_de_familia = "abuela", age = 65)
    context = {
        "abuela": abuela
    }
    return render(request,"abuela.html",context=context)