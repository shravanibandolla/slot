from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot

# Dashboard Home
def home(request):
    slots = Slot.objects.all().order_by("id")

    available_count = Slot.objects.filter(status="available").count()
    booked_count = Slot.objects.filter(status="booked").count()

    return render(request, "home.html", {
        "slots": slots,
        "available_count": available_count,
        "booked_count": booked_count
    })

# Available Slots
def available_slots(request):
    slots = Slot.objects.filter(status="available")
    return render(request, "available_slots.html", {"slots": slots})

# Booked Slots
def booked_slots(request):
    slots = Slot.objects.filter(status="booked")
    return render(request, "booked_slots.html", {"slots": slots})

# Book Slot
def book_slot(request, id):
    slot = get_object_or_404(Slot, id=id)

    if slot.status == "available":
        slot.status = "booked"
        slot.save()

    return redirect("home")

# Add Slot
def add_slot(request):
    if request.method == "POST":
        time = request.POST.get("time")
        status = request.POST.get("status")

        Slot.objects.create(time=time, status=status)

        return redirect("home")

    return render(request, "add_slot.html")