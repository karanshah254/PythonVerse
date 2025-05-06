from django.urls import path
from . import views

urlpatterns = [
    path("function", views.hello),  # Function based view
    path("class", views.HelloView.as_view()),  # Class based
    path("reservation", views.home),
]
