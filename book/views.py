from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

from .admin import HistoryBookResource
from .models import HistoryBook
from .admin import HistoryBookResource
def export(request):
    person_resource = HistoryBookResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response



# Create your views here.
