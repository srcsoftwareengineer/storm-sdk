'''
Created on 15 de jul. de 2025

@author: masterdev
'''

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("sign-in/", auth_views.LoginView.as_view(template_name="core/sign_in.html"), name="sign_in"),
    path("sign-up/", views.register, name="sign_up"),
    path("logout/", auth_views.LogoutView.as_view(next_page="core:sign_in"), name="logout"),
    path("raffles/", views.list_raffles, name="list_raffles"),
    path("raffles/create/", views.create_raffle, name="create_raffle"),
    path("raffles/<int:raffle_id>/publish/", views.publish_raffle, name="publish_raffle"),
    path("raffles/<int:raffle_id>/draw/", views.draw_raffle, name="draw_raffle"),
]
# urlpatterns += [
#     path("raffles/", views.list_raffles, name="list_raffles"),
#     path("raffles/create/", views.create_raffle, name="create_raffle"),
# ]