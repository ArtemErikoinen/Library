from django.contrib import admin
from book.models import Book, HistoryBook
from reader.models import Reader
from import_export import resources, fields
from import_export.admin import ExportMixin,ExportActionMixin,ExportActionModelAdmin,ImportExportActionModelAdmin

from import_export.widgets import ForeignKeyWidget, CharWidget
class HistoryBookResource(resources.ModelResource):
    
    book = fields.Field(
        column_name='Книга',
        attribute='book',
        widget=ForeignKeyWidget(Book, 'name'))

    name = fields.Field(
        column_name='ФИ',
        attribute='name',
        widget=ForeignKeyWidget(Reader, 'full_name'))
    school_class = fields.Field(
        column_name='Класс',
        attribute='name',
        widget=ForeignKeyWidget(Reader, 'school_class'))

    data_of_capture = fields.Field(
        column_name='Дата выдачи',
        attribute='data_of_capture',
    )
    data_of_return = fields.Field(
        column_name='Дата возврата',
        attribute='data_of_return',
    )





    class Meta:
        model = HistoryBook
        verbose_name = 'Экспорт формуляров'
        verbose_name_plural = 'Экспорт формуляров'
        fields = ('book','school_class', 'name','data_of_capture','data_of_return')
        filter = ('school_class',)




@admin.register(HistoryBook)
class HistoryBookAdmin(ExportActionModelAdmin):
    resource_classes = [HistoryBookResource]
    list_display = ['book', 'name', 'data_of_capture','data_of_return','extradition']
    list_filter = ('extradition',)



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



