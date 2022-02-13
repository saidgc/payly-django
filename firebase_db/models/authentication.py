import requests
from django.contrib import auth
from django.core.handlers.wsgi import WSGIRequest

from account.models import PaylyUser as User
from firebase_db.helpers.settings import firebase


class FirebaseAuthentication(object):
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
                django_user.firebase_user_id = firebase_user.get('localId')
                django_user.save()
            auth.login(request, django_user)
        return True
