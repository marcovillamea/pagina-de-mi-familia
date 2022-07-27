from django.urls import path

from familia.views import mama,papa,abuela,lista_familia



urlpatterns = [
    path("mama/", mama , name= "mama"),
    path("abuela/", abuela , name="nombre de abuela"),
    path("papa/", papa, name= "nombre papa"),
    path("lista_familia/", lista_familia, name="lista de familia")
    



]