from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
     url(r'^registration$', views.registration, name='registration'),
]
