from django.contrib import admin
from .models import Book
class Book_admin(admin.ModelAdmin):
    list_display = ('title','author','publish_date','price')

admin.site.register(Book,Book_admin)
# Register your models here.
