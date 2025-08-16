from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Inventory, UpdateInventory, DeleteInventory

def index(request):
    return render(request, "index.html")

# ✅ Home/Menu view
def menu(request):
    coffees = Inventory.objects.all()
    return render(request, 'menu.html', {'coffees': coffees})


# ✅ Update inventory view
def update_inventory(request, pk):
    coffee = get_object_or_404(Inventory, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        image = request.FILES.get("image")

        UpdateInventory.update(
            pk=pk,
            name=name,
            price=float(price) if price else None,
            quantity=int(quantity) if quantity else None,
            image=image
        )
        return redirect("menu")  # redirect back to menu page

    return render(request, "update_inventory.html", {"coffee": coffee})


# ✅ Delete inventory view
def delete_inventory(request, pk):
    if request.method == "POST":
        DeleteInventory.delete(pk)
        return redirect("menu")
    coffee = get_object_or_404(Inventory, pk=pk)
    return render(request, "delete_inventory.html", {"coffee": coffee})
