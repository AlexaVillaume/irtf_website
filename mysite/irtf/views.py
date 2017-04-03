from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Targets, EquivWidths

import csv
import numpy as np

def index(request):
    names = Targets.objects.order_by('name')

    template = loader.get_template('irtf/index.html')
    context = {
                'output': names,
            }

    return HttpResponse(template.render(context, request))


def test_write_csv(request):
    names = Targets.objects.order_by('name')[:5]
    output = ', '.join([str(n) for n in names])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="irtf_test.csv"'

    writer = csv.writer(response)
    writer.writerow(output)
    return response

