from django.contrib import admin
from .models import Posts
# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'text', 'pub_date')
    list_display_links = ('id', 'title')
    search_fields = ('text', 'title')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
