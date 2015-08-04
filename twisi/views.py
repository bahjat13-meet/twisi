from django.shortcuts import render
from twisi.models import Twisser
from twisi.models import Drawing
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import simplejson
from django.contrib.auth import authenticate
import datetime
import pytz
# Create your views here.

def base(request):
    return render(request, 'twisi/home.html')


@require_http_methods(["GET", "POST"])
def registration(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		nationality = request.POST['nationality']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')

	# check for a duplicate username here User.objects.filter(username=username).count()
	if (User.objects.filter(username=username).count()==1):
		return check_login(request)
	user = User(username = username)
	user.set_password(password)
	user.save()
	twisser = Twisser(user=user , nationality=nationality)
	twisser.save()

	response = { 'success' : True}
	return HttpResponse(simplejson.dumps(response), content_type='application/json')



@require_http_methods(["GET", "POST"])
def check_login(request):
	asdfasdoifh
	return HttpResponse(simplejson.dumps(login_helper(request)), content_type='application/json')


@require_http_methods(["GET", "POST"])
def upload_image(request):
	response = login_helper(request)
	if (response['success'] == False):
		return response

	try:	
		username = request.POST['username']
		category = request.POST['category']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')
	user = 	User.objects.get(username = username)
	if request.method == 'POST':
		try:
			drawing = Drawing(user = user ,category = category, date=datetime.datetime.now(pytz.UTC))
			drawing.save()
			filename = 'twisi/static/img/gallery/{0}.png'.format(drawing.id)
			drawing.filename=filename
			drawing.save()
		except:
			response = { 'success' : False, 'message' : "the drawings didnt save"}
			return HttpResponse(simplejson.dumps(response), content_type='application/json')
		handle_uploaded_file(request.FILES['file'], filename)
		response = { 'success' : True}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')
	else:
		response = { 'success' : False, 'message' : "the immage didnt post"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')	

# Put a try, except around saving the drawings to the database, if there's an error in saving the drawings, return the message in the json
# Return success false if method isn't POST
# in registration, if user already exists. call check_login


def handle_uploaded_file(f, filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def login_helper(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return response
	user = authenticate(username = username , password = password)
	if user is not None:
		response = { 'success' : True}
		return response
	else:	
		response = { 'success' : False, 'message' : "wrong username/password"}
		return response


		           	









