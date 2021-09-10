from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display =("title","slug","author","created","updated")
   preserve_filters ={"slug":("title",)}