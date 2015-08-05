from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.base, name='home'),
     url(r'^registration$', views.registration, name='registration'),
      url(r'^check_login$', views.check_login, name='check_login'),
	url(r'^upload_image$', views.upload_image, name='upload_image'),
	url(r'^get_own_images$', views.get_own_images, name='get_own_images'),
	url(r'^get_image$', views.get_image, name='get_image'),
	url(r'^get_public_images$', views.get_public_images, name='get_public_images'),
 ]
