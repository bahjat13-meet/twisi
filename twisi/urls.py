from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.base, name='home'),
     url(r'^registration$', views.registration, name='registration'),
      url(r'^check_login$', views.check_login, name='check_login'),
 ]
