from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.hello, name='hello'),
    path('create/', view=views.create_account, name='create_account'),
    path('update_profile', view=views.update_profile, name='update_profile'),
    path('create_profile', view=views.create_profile, name='create_profile'),
    path('view_profile', view=views.view_profile, name='view_profile'),
    path('login', view=views.login, name='login'),
    path('change_password', view=views.change_password, name='change_password'),
]