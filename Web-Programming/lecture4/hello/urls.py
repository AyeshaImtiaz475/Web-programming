from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("ayesha", views.ayesha, name="ayesha"),
    path("muqaddas", views.muqaddas, name="muqaddas"),
    path("poem", views.poem, name="poem")
]