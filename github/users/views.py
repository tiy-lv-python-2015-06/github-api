from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.
class GitHubView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(GitHubView, self).get_context_data(**kwargs)
        username = 'traciarms'

        # context['profile_info'] = requests.\
        #     get("http://10.68.0.90:8000/api/github/{}/".format(username)).json()
        context['profile_info'] = requests.get("https://api.github.com/users/{}".format(username)).json()
        context['profile_repo'] = requests.get("https://api.github.com/users/{}/repos".format(username)).json()
        # context['profile_repo'] = requests.\
        #     get("http://10.68.0.90:8000/api/github/{}/repos/".format(username)).json()
        return context
