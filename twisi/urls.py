from django.conf.urls import url

import views

urlpatterns = [
    url(r'^registration$', views.registration, name='registration'),
    url(r'^$', views.base, name='home'),
]