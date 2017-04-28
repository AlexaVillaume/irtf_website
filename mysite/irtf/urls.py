from django.conf.urls import url

from . import views

urlpatterns = [

            # view to render search form
            url(r'^$', views.index, name='index'),

            # view to handle data downlaod
            url(r'^download/$', views.download_data, name='download_data')

            ]
