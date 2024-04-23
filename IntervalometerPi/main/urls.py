from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("running", views.running, name="running"),
<<<<<<< HEAD
    path("clicking", views.clicking, name="clicking")
]
=======
]
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
