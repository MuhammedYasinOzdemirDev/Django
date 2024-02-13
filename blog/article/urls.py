from django.contrib import admin
from django.urls import path, include
from . import views  # . klasor altındaki anlama gelir
app_name = "article"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("anasayfa/", views.Anasayfa),
    path("addarticle", views.addarticle, name="addarticle"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("detail/<int:id>", views.detail, name="detay"),
    path("edit/<int:id>", views.edit, name="guncelle"),
    path('', views.articles, name="articles"),
    path('addcomment/<int:id>', views.addcomment, name="yorumekle"),
]
# Projeden include edilen patternlerin fonksiyonlara yonlendirilir
# genellikle ekleme silme gibi olayda bu daha mantıklı kullanımdır
