from django.contrib import admin

# Register your models here.
# model kayıt etme yeri

# article modeli alınır .models suanki klasoru temsil eder
from .models import Article, Comment2

"""admin.site.register(Article)#Kayıt eder articleı
#not bunu django soylemek için uygulamayı setting kaydetmek lazım projenin"""

admin.site.register(Comment2)
# kayıt edilen objenin özelleştilmesi halinde panelde gözükür


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    # bunları link haline getirir  #https://docs.djangoproject.com/en/2.0/ref/contrib/admin/ bu sitede özellikler
    list_display_links = ["title", "author", "created_date"]
    # sadece title bolumune gore arama bolumu olusturur
    search_fields = ["title"]
    list_filter = ["created_date"]  # zamana gore filtreleme alanı olusturur

    class Meta:  # bu sayede birbirlerine bağlanır
        model = Article


# admin.register(Article)
