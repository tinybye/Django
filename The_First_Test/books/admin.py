from django.contrib import admin
from books.models import Publisher,Author,Book
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title','authors','publisher','publication_date')

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)

