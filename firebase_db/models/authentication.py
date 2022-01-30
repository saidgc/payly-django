import requests
from django.contrib import auth

from ..helpers.firebase_auth import auth as firebase
from django.contrib.auth.models import User


def login(request, user: str, email: str, password: str) -> bool:
    try:
        firebase_user = firebase.sign_in_with_email_and_password(
            email,
            password,
        )
    except requests.exceptions.HTTPError:
        login_error = True
        return False
    else:
        django_user = auth.authenticate(
            request,
            username=firebase_user['email'],
            password=password,
        )
        if not django_user:
            django_user = User.objects.create_user(
                user,
                firebase_user['email'],
                password,
            )
        auth.login(request, django_user)
    return True
