from django.shortcuts import render

# Create your views here.

# ESTOS SON LOS CONTROLADORES QUE ME DEVUELVEN RENDERIZADA LA PAGINA HTML O MIS TEMPLATES
def index(request):
    return render(request, "index.html")

def trabajos(request):
    return render(request, "trabajos.html")

def registrarse(request):
    return render(request, "registrarse.html")

def iniciarSesion(request):
    return render(request, "iniciarSesion.html")

def mantencion1(request):
    return render(request, "mantencion1.html")

def mantencion2(request):
    return render(request, "mantencion2.html")

def mantencion3(request):
    return render(request, "mantencion3.html")

def mantencion4(request):
    return render(request, "mantencion4.html")

def mantencion5(request):
    return render(request, "mantencion5.html")

def mantencion6(request):
    return render(request, "mantencion6.html")

def repuestos(request):
    return render(request, "repuestos.html")

