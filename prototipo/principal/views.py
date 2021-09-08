# Generales
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
# Modelos
from principal.models import *
# Formularios
from principal.forms import *

def index(request):
    telefonos = Telefono.objects.all()
    dispositivos = Dispositivo.objects.all()
    accesorios = Accesorio.objects.all()
    monederos = Monedero.objects.all()
    informacion = {'telefonos': telefonos, 'dispositivos':dispositivos, 'accesorios':accesorios,'monederos':monederos}
    return render(request, 'index.html', informacion)

def telefonos(request):
    telefonos = Telefono.objects.all()
    monederos = Monedero.objects.all()
    informacion = {'telefonos': telefonos, 'monederos':monederos}
    return render(request, 'telefonos.html', informacion)

def crear_telefono(request):
    if request.method=='POST':
        form = FormTelefono(request.POST)
        if form.is_valid():
                form.save() 
                return redirect(index)
    else:
        form = FormTelefono()
    titulo = "Añadir telefono"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-telefonos.html',  informacion)

def editar_telefono(request, id):
    telefono = Telefono.objects.get(pk=id)
    if request.method=='POST':
        form = FormTelefono(request.POST, instance=telefono)
        if form.is_valid():
                form.save() 
                return redirect(index)
    else:
        form = FormTelefono(instance=telefono)
    titulo = "Editar información del telefono"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-telefonos.html',  informacion)

def eliminar_telefono(request, id):
        Telefono.objects.get(pk=id).delete()
        return redirect(index)
    
def monedero(request, id):
    monedero = Monedero.objects.get(pk=id)
    informacion = {'monedero':monedero}
    return render(request, 'monedero.html', informacion)

def monedero_telefono(request, id):
    telefono = Telefono.objects.get(pk=id)
    if request.method=='POST':
        form = FormMonederoTelefono(telefono, request.POST)
        if form.is_valid():
                form.save()
                return redirect(index)
    else:
        form = FormMonederoTelefono(telefono)
    titulo = "Repartir dinero de "
    diccionario = {'form': form, 'telefono': telefono, 'titulo':titulo, 'valor':True, 'valor3': True}
    return render(request, 'forms/form-transacciones.html', diccionario)

def monedero_transaccion(request, id):
    monedero = Monedero.objects.get(pk=id)
    if request.method=='POST':
        form = FormMonedero(monedero, request.POST)
        if form.is_valid():
                form.save()
                return redirect(index)
    else:
        form = FormMonedero(monedero)
    titulo = "Nueva transacción"
    diccionario = {'form': form, 'monedero': monedero, 'titulo':titulo, 'valor':True, 'valor2': True}
    return render(request, 'forms/form-transacciones.html', diccionario)

def eliminar_transaccion(request, id):
        Transaccion.objects.get(pk=id).delete()
        return redirect(index)
    
def dispositivos(request):
    dispositivos = Dispositivo.objects.all()
    monederos = Monedero.objects.all()
    informacion = {'dispositivos': dispositivos, 'monederos':monederos}
    return render(request, 'dispositivos.html', informacion)

def crear_dispositivo(request):
    if request.method=='POST':
        form = FormDispositivo(request.POST)
        if form.is_valid():
                form.save() 
                return redirect(dispositivos)
    else:
        form = FormDispositivo()
    titulo = "Añadir dispositivo"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-dispositivos.html',  informacion)

def editar_dispositivo(request, id):
    dispositivo = Dispositivo.objects.get(pk=id)
    if request.method=='POST':
        form = FormDispositivo(request.POST, instance=dispositivo)
        if form.is_valid():
                form.save() 
                return redirect(dispositivos)
    else:
        form = FormDispositivo(instance=dispositivo)
    titulo = "Editar información del dispositivo"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-dispositivos.html',  informacion)

def eliminar_dispositivo(request, id):
        Dispositivo.objects.get(pk=id).delete()
        return redirect(dispositivos)
    
def monedero_dispositivo(request, id):
    dispositivo = Dispositivo.objects.get(pk=id)
    if request.method=='POST':
        form = FormMonederoDispositivo(dispositivo, request.POST)
        if form.is_valid():
                form.save()
                return redirect(index)
    else:
        form = FormMonederoDispositivo(dispositivo)
    titulo = "Repartir dinero de "
    diccionario = {'form': form, 'dispositivo': dispositivo, 'titulo':titulo, 'valor':True, 'valor3': True}
    return render(request, 'forms/form-transacciones2.html', diccionario)


def crear_accesorio(request):
    if request.method=='POST':
        form = FormAccesorio(request.POST)
        if form.is_valid():
                form.save() 
                return redirect(index)
    else:
        form = FormAccesorio()
    titulo = "Añadir accesorio"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-accesorios.html',  informacion)

def monedero_accesorio(request, id):
    accesorio = Accesorio.objects.get(pk=id)
    if request.method=='POST':
        form = FormMonederoAccesorio(accesorio, request.POST)
        if form.is_valid():
                form.save()
                return redirect(index)
    else:
        form = FormMonederoAccesorio(accesorio)
    titulo = "Repartir dinero de "
    diccionario = {'form': form, 'accesorio': accesorio, 'titulo':titulo, 'valor':True, 'valor3': True}
    return render(request, 'forms/form-transacciones3.html', diccionario)

def editar_accesorio(request, id):
    accesorio = Accesorio.objects.get(pk=id)
    if request.method=='POST':
        form = FormAccesorio(request.POST, instance=accesorio)
        if form.is_valid():
                form.save() 
                return redirect(index)
    else:
        form = FormAccesorio(instance=accesorio)
    titulo = "Editar información del accesorio"
    informacion = {'form':form, 'titulo':titulo}
    return render(request, 'forms/form-accesorios.html',  informacion)

def eliminar_accesorio(request, id):
        Accesorio.objects.get(pk=id).delete()
        return redirect(index)