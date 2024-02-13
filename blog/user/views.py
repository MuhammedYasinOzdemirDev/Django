from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
# from django.contrib.auth import login  # login etme metodu session gibi
from django.contrib.auth.models import User  # kullanıcı objesi getirilir
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


def register(request):

    # post bilgileri ile form doldurulur
    form = RegisterForm(request.POST or None)  # postolmussa calışır
    if form.is_valid():  # is_valid fonksiyonu clean metodunu çağırır ve kontrol eder doğru ise bloğa girer değilse hata fırlatır
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUserr = User(username=username)
        newUserr.set_password(password)  # şifreli saklar
        newUserr.save()
        # kullanıcı giriş yaptırırı session gibi bilgileri alır
        login(request, newUserr)
        messages.success(request, "Başarıyla Kayıt Oldunuz")

        return redirect("anasayfa")  # path ismine gore gidir
    form = RegisterForm()
    context = {"form": form}
    return render(request,  "register.html", context)


def Login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        # kullanıcı varmı kontrol eder yok sa None dondurur
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Boyle bir kullanıcı bulunmamakatdır")
            return render(request, 'login.html', {"form": form})
        else:
            messages.success(request, "Başarıyla giriş yapıldı")
            login(request, user)

            return redirect("anasayfa")
    return render(request, 'login.html', {"form": form})


def Logout(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış yapıldı..")
    return redirect("anasayfa")
