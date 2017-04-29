from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.core import serializers

from .models import Targets
from .forms import ExploreForm, DownloadForm

import json
import h5py
import csv
import numpy as np

def index(request):
        template = loader.get_template('irtf/index.html')

        return HttpResponse(template.render(request))

def explore(request):
    try:
        teff_min = request.POST['teff_min']
        teff_max = request.POST['teff_max']
        logg_min = request.POST['logg_min']
        logg_max = request.POST['logg_max']


    except:
        return render(request, 'irtf/explore.html', {
            'error_message': "Something is not right"
            })

    else:
        form = ExploreForm(request.POST)
        stars = Targets.objects.filter(teff__range=(teff_min, teff_max),
                                       logg__range=(logg_min, logg_max)).exclude(
                                        irtf_spec__isnull=True)
        download = DownloadForm(initial={
                'teff_min': teff_min,
                'teff_max': teff_max,
                'logg_min': logg_min,
                'logg_max': logg_max,
                })

        context = {
                    'form': form,
                    'output': stars,
                    'download_form': download
                }
        template = loader.get_template('irtf/explore.html')

        return HttpResponse(template.render(context, request))


def get_data(teff_min, teff_max, logg_min, logg_max):
    return Targets.objects.filter(teff__range=(teff_min, teff_max),
                                  logg__range=(logg_min, logg_max)).exclude(
                                          irtf_spec__isnull=True)

def download_data(request):

    teff_min = request.POST['teff_min']
    teff_max = request.POST['teff_max']
    logg_min = request.POST['logg_min']
    logg_max = request.POST['logg_max']
    stars = get_data(teff_min, teff_max, logg_min, logg_max)


    data = serializers.serialize('json', stars)

    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=irtf_test.json'

    return response


