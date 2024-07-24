from django.shortcuts import render
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todoApp/index.html", {"tasks": request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return render(
                request, "todoApp/index.html", {"tasks": request.session["tasks"]}
            )
        else:
            return render(request, "todoApp/add.html", {"form": form})

    return render(request, "todoApp/add.html", {"form": NewTaskForm()})
