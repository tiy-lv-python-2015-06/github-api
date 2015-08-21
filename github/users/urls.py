from django.conf.urls import url
from users.views import GitHubView

urlpatterns = [

    url(r'^/traciarms', GitHubView.as_view(), name='git_hub_view'),

]