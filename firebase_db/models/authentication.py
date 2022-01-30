import requests
from django.contrib import auth

from ..helpers.settings import firebase
from django.contrib.auth.models import User


class FirebaseAuthentication():
    def __init__(self):
        self.firebase_auth = firebase.auth()

    def login(self, request, user: str, email: str, password: str) -> bool:
        try:
            firebase_user = self.firebase_auth.sign_in_with_email_and_password(
                email,
                password,
            )
        except requests.exceptions.HTTPError:
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
