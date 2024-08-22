from django.contrib import admin

from .models import Reader,SchoolClass
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
class ReaderInline(admin.TabularInline):
    extra = 0
    model = Reader
    def has_change_permission(self,request, obj=None):
        return False
@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    inlines = [ReaderInline]
    list_display = ['numbers','classroom_teacher','email_teacher']

# Register your models here.
