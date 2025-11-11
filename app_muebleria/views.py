from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Sucursal

# Vistas para Empleados
def inicio_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        empleado = Empleado(
            fecha_contratacion=request.POST['fecha_contratacion'],
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            cargo=request.POST['cargo'],
            telefono=request.POST['telefono'],
            sueldo=request.POST['sueldo']
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleados': empleados})

def realizar_actualizacion_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.nombre = request.POST['nombre']
        empleado.edad = request.POST['edad']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.sueldo = request.POST['sueldo']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# Vistas para Sucursal
def inicio_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursal.html', {'sucursales': sucursales})

def agregar_sucursal(request):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal = Sucursal(
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            num_sucursal=request.POST['num_sucursal'],
            encargado=request.POST['encargado'],
            codigo_postal=request.POST['codigo_postal'],
            ciudad=request.POST['ciudad'],
            id_empleado=empleado
        )
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/agregar_sucursal.html', {'empleados': empleados})

def actualizar_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursales': sucursales})

def realizar_actualizacion_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=request.POST['id_empleado'])
        sucursal.telefono = request.POST['telefono']
        sucursal.direccion = request.POST['direccion']
        sucursal.num_sucursal = request.POST['num_sucursal']
        sucursal.encargado = request.POST['encargado']
        sucursal.codigo_postal = request.POST['codigo_postal']
        sucursal.ciudad = request.POST['ciudad']
        sucursal.id_empleado = empleado
        sucursal.save()
        return redirect('ver_sucursal')
    
    empleados = Empleado.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal, 'empleados': empleados})

def borrar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursal')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')