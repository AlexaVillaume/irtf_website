from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import Targets
from .forms import IndexForm, DownloadForm

import h5py
import csv
import numpy as np

def index(request):

    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            teff_min = request.POST['teff_min']
            teff_max = request.POST['teff_max']
            logg_min = request.POST['logg_min']
            logg_max = request.POST['logg_max']
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
            template = loader.get_template('irtf/index.html')

    else:
        form = IndexForm()

    return HttpResponse(template.render(context, request))

def get_csv_data(teff_min, teff_max, logg_min, logg_max):
    return Targets.objects.filter(teff__range=(teff_min, teff_max),
                                  logg__range=(logg_min, logg_max)).exclude(
                                          irtf_spec__isnull=True)

def download_data(request):

    teff_min = request.POST['teff_min']
    teff_max = request.POST['teff_max']
    logg_min = request.POST['logg_min']
    logg_max = request.POST['logg_max']
    stars = get_csv_data(teff_min, teff_max, logg_min, logg_max)


    #response = HttpResponse(content_type='application/hdf5')
    #response['Content-Disposition'] = 'attachment; filename="irtf_test.hdf5"'

    #h = h5py.File(response)
    #h.create_dataset('Name', data=stars[0].name)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="irtf_test.csv"'

    props = ['name', 'teff', 'logg', 'fe_h']
    writer = csv.writer(response)
    for star in stars:
        row = []
        for prop in props:
            row.append(getattr(star, prop))
        writer.writerow(row)

    return response


