from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render_to_response

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

    teff_min, teff_max = request.GET.get('teff_min'), request.GET.get('teff_max')
    logg_min, logg_max = request.GET.get('logg_min'), request.GET.get('logg_max')
    stars = Targets.objects.filter(teff__range=(teff_min, teff_max)).filter(logg__range=(logg_min, logg_max))

    template = loader.get_template('irtf/index.html')
    context = {
                'output': stars,
                'min_teff': teff_min,
                'max_teff': teff_max,
            }

    return HttpResponse(template.render(context, request))


   # query = request.GET.get('name')
   # star = Targets.objects.filter(name='BD+002058A')
   # if star:
   #     response = HttpResponse(content_type='text/csv')
   #     response['Content-Disposition'] = 'attachment; filename="irtf_test.csv"'

   #     writer = csv.writer(response)
   #     writer.writerow(star)

    #return response

