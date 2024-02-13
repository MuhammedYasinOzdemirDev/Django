from django.db import models

# Create your models here.
# model olusturmaya yarar


class Article(models.Model):  # sqlalcamy gibi model olustururuz tablo
    # baska tabloyu gosteriri oraya atıf yapar ForegeinKey
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    # bu sayede tablolar arası erişim ve hazır kullanıcı modeli kullanılır
    # auth.user tablosundan alır hazır modellerin içinde yer alır
    # ondelete modals .Cascade  kullanıcı silinirse makaleyide siler
    # başlık alanı belirtilir textfielde benzr
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")  # text araeya benzer
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma tarihi")  # o anki tarihi olusturmayı yarar

    def __str__(self) -> str:
        # bu metot ile Article object yerine sitede veya baska yerde baslık ismi gorunur
        return self.title
# Bundan sonra kayıt etmek için admin paneline gidilir
# verbosname gorunecek yazıyı belirler


class Comment2(models.Model):  # yorum modeli
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        # bu metot ile Article object yerine sitede veya baska yerde baslık ismi gorunur
        return self.comment_author
