# Views for maps application

from django.shortcuts import render
import os
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Create your views here.
def default_map(request):
	# TODO: move this token to Django settings from an environment variable
	# found in the Mapbox account settings and getting started instructions
	# see https://www.mapbox.com/account under the "Access tokens" section
	mapbox_access_token = env('mapbox_access_token')
	return render(request, 'default.html',
				  { 'mapbox_access_token': mapbox_access_token })

