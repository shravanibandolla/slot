from django.shortcuts import render,redirect
from .models import Slot
# Create your views here.

def home(request):
    return render(request, "home.html")

def available_slots(request):
    slots = Slot.objects.filter(status="available")
    return render(request, "available_slots.html", {"slots": slots})

def booked_slots(request):
    slots = Slot.objects.filter(status="booked")
    return render(request, "booked_slots.html", {"slots": slots})

def book_slot(request, id):
    slot = Slot.objects.get(id=id)
    if slot.status == "available":
        slot.status = "booked"
        slot.save()
    return redirect("available_slots")
def add_slot(request):
    if request.method == "POST":
        time = request.POST.get("time")
        status = request.POST.get("status")

        Slot.objects.create(time=time, status=status)

        return redirect("/slots/available/")

    return render(request, "add_slot.html")
