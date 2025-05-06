from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm


# Create your views here.
# 1. function based view
def hello(request):
    # http://127.0.0.1:8000/app/function
    return HttpResponse("Hello World! from function based view!")


# 2. class based view
class HelloView(View):
    def get(self, request):
        # http://127.0.0.1:8000/app/class
        return HttpResponse("Hello from class based view!")


def home(request):
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation created successfully!")

    return render(request, "index.html", {"form": form})
