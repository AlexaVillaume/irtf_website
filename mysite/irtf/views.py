from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .models import Targets
from .forms import IndexForm

import csv
import numpy as np

def index(request):

    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = IndexForm()

    return render(request, 'irtf/index.html', {'form': form})


"""
def index(request):

    #try:
    #    star = Targets.objects.filter(name=query)
    #except (KeyError, Target.DoesNotExist):
    #    return render(request, {
    #        'error_message': "That star doesn't exist"
    #    })

    query = request.GET.get('name')
    star = Targets.objects.filter(name='BD+002058A')
    #star = Targets.objects.filter(name=query)
    if star:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="irtf_test.csv"'

        writer = csv.writer(response)
        writer.writerow(star)

    #return response

    names = Targets.objects.order_by('name')

    template = loader.get_template('irtf/index.html')
    context = {
                'output': names,
            }

    return HttpResponse(template.render(context, request))
"""


