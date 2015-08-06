from django.conf.urls import url

import views

urlpatterns = [
	url(r'^$', views.base, name='home'),
	url(r'^registration$', views.registration, name='registration'),
	url(r'^check_login$', views.check_login, name='check_login'),
	url(r'^upload_image$', views.upload_image, name='upload_image'),
	url(r'^get_own_images$', views.get_own_images, name='get_own_images'),
	url(r'^get_image$', views.get_image, name='get_image'),
	url(r'^get_public_images_by_score$', views.get_public_images_by_score, name='get_public_images_by_score'),
	url(r'^get_public_images_by_date$', views.get_public_images_by_date, name='get_public_images_by_date'),
	url(r'^submit_image$', views.submit_image, name='submit_image'),
	url(r'^add_twissies$', views.add_twissies, name='add_twissies'),
	url(r'^add_votes$', views.add_votes, name='add_votes'),
	url(r'^gallery$', views.page, name='page2'),
	url(r'^register$', views.register, name='register'),
	url(r'^signin$', views.login_page, name='login'),
	url(r'^logout$', views.logout_page, name='logout'),
	]
