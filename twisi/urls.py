from django.conf.urls import url

import views

urlpatterns = [

    url(r'^registration$', views.registration, name='registration'),
    url(r'^check_login$', views.check_login, name='check_login'),
	url(r'^$', views.base, name='home'),
	url(r'^upload_image$', views.upload_image, name='upload_image'),
]

