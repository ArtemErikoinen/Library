from django.contrib import admin
from book.models import *



class HistoryBookInline(admin.TabularInline):
    model = HistoryBook
    autocomplete_fields = ('name',)
    extra = 0
    raw_id_fields = ('name',)
    show_change_link = True


    def save(self, *args, **kwargs):
        self.c+=1
        super(HistoryBookInline, self).save(*args, **kwargs)



@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    inlines = [
        HistoryBookInline,
    ]
    list_display = ['name', 'author', 'year', 'publishing_house','id', 'numbers']
    ordering = ['name']
    list_per_page = 20
    search_fields = ('name',)



