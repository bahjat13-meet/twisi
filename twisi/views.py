from django.shortcuts import render
from twisi.models import Twisser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import simplejson
# Create your views here.

def base(request):
    return render(request, 'twisi/base.html')


@require_http_methods(["GET", "POST"])
def registration(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		nationality = request.POST['nationality']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')
	user = User(username = username)
	user.set_password(password)
	user.save()
	twisser = Twisser(user=user , nationality=nationality)
	twisser.save()

	response = { 'success' : True}
	return HttpResponse(simplejson.dumps(response), content_type='application/json')


