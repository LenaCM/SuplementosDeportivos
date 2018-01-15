from django.shortcuts import render, get_object_or_404
from .forms import ProveedorForm
from django.shortcuts import redirect
from .models import Proveedor

def index(request):
	return listaProveedores(request, 'index')

def nuevoProveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores:nuevo')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/nuevo.html', {'form':form})

def listaProveedores(request, pagina):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/'+ pagina + '.html', {'proveedores':proveedores})

def editarProveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            return redirect('/proveedores/lista')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/editar.html', {'form': form})

def eliminarProveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect('proveedores:index')