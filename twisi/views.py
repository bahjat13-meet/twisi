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
import pdb
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
	return HttpResponse(simplejson.dumps(login_helper(request)), content_type='application/json')


@require_http_methods(["GET", "POST"])
def upload_image(request):
	break
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
			drawing = Drawing(twisser=user.twisser,category = category, date=datetime.datetime.now(pytz.UTC))
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


# parameters (request.POST): username, password, nationality, category, is_public
# 1. getting own pictures (user.id, doesn't matter if submitted)
# 2. getting pictures of a certain nationality and category
# 3. all submitted pictures
def get_own_images(request):
	response = login_helper(request)
	if (response['success'] == False):
		return response
	try:	
		username = request.POST['username']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')
	user = User.objects.get(username=username)
	drawings = user.twisser.drawing_set.all()
	drawing_dicts = [drawing.serialize() for drawing in drawings]
	response = {
		'success' : True, 'drawings' : drawing_dicts
	}
	return HttpResponse(simplejson.dumps(response), content_type='application/json')




def get_image(request):
	response = login_helper(request)
	if (response['success'] == False):
		return response
	try:	
		category = request.POST['category']
		nationality = request.POST['nationality']
	except:
		response = { 'success' : False, 'message' : "Missing fields"}
		return HttpResponse(simplejson.dumps(response), content_type='application/json')
	drawings = Drawing.objects.filter(twisser__nationality=nationality, category=category).all()
	drawing_filtering = [drawing.serialize() for drawing in drawings]
	response = {
		'success' : True, 'drawings' : drawing_filtering
	}
	return HttpResponse(simplejson.dumps(response), content_type='application/json')

	


def get_public_images(request):
	response = login_helper(request)
	if (response['success'] == False):
		return response
	drawings = Drawing.objects.filter(is_public=True).all()
	drawing_filtering = [drawing.serialize() for drawing in drawings]
	response = {
		'success' : True, 'drawings' : drawing_filtering
	}
	return HttpResponse(simplejson.dumps(response), content_type='application/json')

	
	
	


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


		           	









