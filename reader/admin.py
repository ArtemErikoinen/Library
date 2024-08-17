from django.contrib import admin

from .models import Reader
from book.models import HistoryBook
# Register your models here.
class HistoryBookInline(admin.TabularInline):
    model = HistoryBook


    def has_add_permission(self,request,obj=None):
        return False

    def has_change_permission(self,request, obj=None):
        return False


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    inlines = [HistoryBookInline]
    list_display = ['last_name','first_name','school_class']
    search_fields = ('school_class',)
    list_filter = ('school_class',)
# Register your models here.
