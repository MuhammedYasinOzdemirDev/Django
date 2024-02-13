"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article.views import index, index2, Anasayfa, Hakkimizda, details, dashboard
# url işlemleri yapılır
urlpatterns = [
    path("admin/", admin.site.urls),
    path("index2", index2)  # birşey yazılmamaıs anasayfa yı temsil eder
    # otamatik/ vardır ilk basta url ler belilernir
    , path("index", index, name="index"), path("", Anasayfa, name="anasayfa"), path("hakkimizda", Hakkimizda),
    # include başka yerde uygulamada olusturulan patternleri include/ dan sonra eşleşenlerle birleştiriri fonksiyonu yonlendirir bu sayede hem kalablık gozukmez hem duzenli olur başka python dosyasında uygulama altında urls olustururlur
    path("detail/<int:id>", details), path("article/", include("article.urls")),
    path("user/", include("user.urls")),
    path("dashboard", dashboard, name="kontrol")

]  # name vermek redirect  işlemlerde url for mantığı ile çağğrılır
