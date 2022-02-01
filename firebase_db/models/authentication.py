import requests
from django.contrib import auth
from django.core.handlers.wsgi import WSGIRequest

from ..helpers.settings import firebase
from django.contrib.auth.models import User

FIREBASE_KEY = 'firebase_user_id'


class FirebaseAuthentication:
    def __init__(self) -> None:
        self.firebase_auth = firebase.auth()

    def login(self, request: WSGIRequest, user: str, email: str, password: str) -> bool:
        try:
            firebase_user = self.firebase_auth.sign_in_with_email_and_password(
                email=email,
                password=password,
            )
        except requests.exceptions.HTTPError:
            return False
        else:
            django_user = auth.authenticate(
                request=request,
                username=firebase_user['email'],
                password=password,
            )
            if not django_user:
                django_user = User.objects.create_user(
                    username=user,
                    email=firebase_user['email'],
                    password=password,
                )
            auth.login(request, django_user)
            request.session[FIREBASE_KEY] = firebase_user.get('idToken')
        return True
