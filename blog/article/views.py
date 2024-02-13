from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Comment2
# Create your views here.
# url metodların yazıldığı bolumdur
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def index(request):  # request mutlaka her zaman olmalı
    # kolaylık olması açısında HttpResponse donderilir
    return HttpResponse("Anasayfa")


def index2(request):
    context = {
        "numbers": [*range(20)], "sayi": 5
    }  # iki çeşit veri gonderilebilir değişken olarak
    # response doner
    return render(request, "deneme.html", {"numbers": [*range(20)], "sayi": 5})


def Anasayfa(request):
    return render(request, "anasayfa.html")


def Hakkimizda(request):
    return render(request, "hakkimizda.html")


def details(request, id):
    return HttpResponse("ID:"+str(id))  # dinamik id tanımlama


@login_required(login_url="user:login")
def dashboard(request):
    # giriş yapılan kullanıcıların bilgileri sozluk yapısı alınır
    articles = Article.objects.filter(author=request.user)
    return render(request, "dasboard.html", {"articles": articles})


@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        # otomatik model olusturdu ama veri tabanınana kaydetmedi
        article = form.save(commit=False)
        article.author = request.user  # author bilgisi girildi
        article.save()
        messages.success(request, "Makale başarıyla kaydedildi...")
        return redirect('kontrol')
    return render(request, "addarticle.html", {"form": form})


@login_required(login_url="user:login")
def detail(request, id):
    # liste dondugu için ilk elemanı alırız
    # article = Article.objects.filter(id=id).first()
    # id eşit olanı bulur yoksa 404 sayfası gosterirr
    article = get_object_or_404(Article, id=id)
    comment = Comment2.objects.filter(id=id)
    return render(request, "detail.html", {"article": article, "comments": comment})


@login_required(login_url="user:login")
def edit(request, id):

    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user  # author bilgisi giril
        article.save()
        messages.success(request, "Makale başarıyla guncellendi...")
        return redirect('kontrol')
    return render(request, 'updatearticle.html', {'form': form})


@login_required(login_url="user:login")
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    # uygulama altında gidis app_name gore
    messages.success(request, "Makale başarıyla silindi...")
    return redirect('kontrol')


def articles(request):
    keyword = request.GET.get('keyword')
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {'articles': articles})
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


def addcomment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        author = request.POST.get('isim')
        content = request.POST.get('content')
        comment = Comment2(comment_author=author, comment_content=content)
        comment.article = article

        comment.save()

        return redirect("/article/detail/"+str(id))
