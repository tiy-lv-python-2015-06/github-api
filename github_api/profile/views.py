import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def profile(request, user_name):
    response = requests.get("https://api.github.com/users/{}".format(user_name)).json()
    response['repo_detail'] = requests.get("http://10.68.0.90:8000/api/github/{}/repos".format(user_name)).json()
    return render_to_response(template_name='user_profile.html', context=response)