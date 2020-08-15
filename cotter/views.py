import jwt
import json
import requests

from django.shortcuts import render
from cotter.models import SiteUser

CotterJWKSURL = "https://www.cotter.app/api/v0/token/jwks"


def login(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode("utf-8"))

        cotter_jwk = requests.get(url=CotterJWKSURL)
        jwk_data = cotter_jwk.json()

        print("******************")
        print(jwk_data)
        print("******************")
    # Getting jwt key
        public_key = jwk_data['keys'][0]

    # Getting access token and validate it
        token = req['oauth_token']['access_token']
        response = jwt.decode(token, public_key, algorithms='ES256')

    # User Authenticated!
    # 1) If user doesn't exist, register user to db. Otherwise, continue
    # 2) Either use Cotter's Access Token for your entire API authorization
    #    OR
    #    You can Generate your JWT Tokens or other session management here

        user_id = req['user']['ID']
        identifier = req['user']['identifier']
        user = SiteUser.objects.get_or_create(user_id=user_id, identifier=identifier)

        print('------------------------------')
        print(user)
        print('------------------------------')

        request.session['cotter_user_id'] = user_id
        return response