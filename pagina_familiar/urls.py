from django.contrib import admin
from django.urls import path
from familia.views import mama, papa, abuela

urlpatterns = [
    path('admin/', admin.site.urls),
    path("mama/", mama, name = "nombre de mi mama"),
    path("papa/", papa, name = "nombre de mi papa"),
    path("abuela/", abuela , name = "nombre de mi abuela")
]
