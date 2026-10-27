from django.shortcuts import render


def redes(request):
    # La lista de redes llega por el context processor "redes_sociales".
    return render(request, 'redes_sociales/redes.html')
