from django.contrib import admin
from .models import Event, Blog, Comment

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name","date")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog", "user")

