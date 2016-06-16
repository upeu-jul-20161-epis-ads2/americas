from django.conf.urls import url
from django.views.generic import TemplateView
from apps.home import views as home_views

urlpatterns = [

    url(r'^', home_views.index, name='index'),
    url(r'^index/', home_views.index, name='index'),


]
