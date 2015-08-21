
from django.shortcuts import render, render_to_response

# Create your views here.
import requests


def get_profile(request, username):
    response = requests.get('https://api.github.com/users/{}'.format(username)).json()
    response['repo_things'] = requests.get('https://api.github.com/users/{}/repos'.format(username)).json()
    return render_to_response(template_name='index.html', context=response)