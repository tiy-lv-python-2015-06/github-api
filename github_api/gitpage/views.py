
from django.shortcuts import render, render_to_response

# Create your views here.
import requests


def get_profile(request):
    response = requests.get('https://api.github.com/users/Apentz49').json()
    response['repo_things'] = requests.get('https://api.github.com/users/Apentz49/repos').json()
    return render_to_response(template_name='index.html', context=response)
