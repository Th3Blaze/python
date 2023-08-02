from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def buscar_ventas(request):
    form=busquedaForm()
    ventas=Venta.objects.all()
    if request.method=='POST':
        form=busquedaForm(request.POST)
        if form.is_valid():
            try:
                nombre_cliente=form.cleaned_data['nombre_cliente']
                producto_vendido=form.cleaned_data['producto_vendido']
                pais_cliente=form.cleaned_data['pais_cliente']

                ventas = ventas.filter(
                cliente__nombre__icontains=nombre_cliente,
                producto__vendido__icontains=producto_vendido,
                cliente__pais__icontains=pais_cliente
                )

            except Exception as e:
                #capturamos el error
                error_message=str(e)
                print('aca eta el error'+error_message)
                ventas=[]
    
    return render(request,'buscar_ventas.html',{'form':form,'ventas':ventas})