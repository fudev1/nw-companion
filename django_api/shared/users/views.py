from rest_framework import viewsets
from .serializers import TenantUserSerializer
from .models import TenantUser

import requests 
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect
from django.conf import settings


# Create your views here.
class TenantUserViewSet(viewsets.ModelViewSet):
    queryset = TenantUser.objects.all()
    serializer_class = TenantUserSerializer


DISCORD_CLIENT_ID = "1318216962270040144"
DISCORD_CLIENT_SECRET = "RCxjL-HObB56ZYma81CguMEPTCvtYgPl"
DISCORD_REDIRECT_URI = "http://localhost:8000/api/users/discord/login/redirect"
DISCORD_AUTH_URL = "https://discord.com/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&response_type=code&redirect_uri={DISCORD_REDIRECT_URI}&scope=identify email guilds"



def discord_login(request: HttpRequest):
    return redirect(DISCORD_AUTH_URL)

def discord_login_redirect(request: HttpRequest):
    code = request.GET.get("code")
    if not code: 
        return HttpResponseBadRequest("code not provided")
    

    token_url = "http://discord.com/api/oauth2/token"
    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": DISCORD_REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_response = requests.post(token_url, data=data, headers=headers)
    if token_response.status_code != 200:
        return JsonResponse({"error": "Failed to obtain token"}, status=400)

    token_data = token_response.json()

    # Utiliser le token pour récupérer les infos utilisateur
    user_url = "https://discord.com/api/users/@me"
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}

    user_response = requests.get(user_url, headers=headers)
    if user_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch user info"}, status=400)

    user_data = user_response.json()

    # Retourner les données utilisateur pour debug
    return JsonResponse({"user": user_data, "token": token_data})





# DISCORD_AUTH_URL = "https://discord.com/oauth2/authorize?client_id=1318216962270040144&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fapi%2Fusers%2Fdiscord%2Flogin%2Fredirect&scope=identify+guilds+email+guilds.members.read"


# # VUE POUR DISCORD LOGIN : REDIRIGER USER => DISCORD POUR AUTHENTIFICATION
# def discord_login(request: HttpRequest):
#     return redirect(DISCORD_AUTH_URL)
    

# # VUE POUR DISCORD CALLBACK : GERER REDIRECTION DE DISCORD APRES AUTHENTIFICATION
# def discord_login_redirect(request: HttpRequest):
#     code = request.GET.get('code')
#     print(code)
#     user = exchange_code(code)
#     return JsonResponse({ "user": user  })

# def exchange_code(code: str):
#     # PAYLOAD => demander publication endpoint discord => request body
#     data = {
#         "client_id": "1318216962270040144",
#         "client_secret": "RCxjL-HObB56ZYma81CguMEPTCvtYgPl",
#         "grant_type": "authorization_code",
#         "code": code,
#         "redirect_uri": "http://localhost:8000/api/users/discord/login/redirect",
#         "scope": "identify email guilds"
#     }

#     headers = {
#         "Content-Type": 'application/x-www-form-urlencoded'
#     }

#     response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
#     print(response)
#     credentitials = response.json()
#     print(credentitials)
#     access_token = credentitials['access_token']
#     response = requests.get('https://discord.com/api/users/@me', headers={
#         'Authorization': 'Bearer %s' % access_token
#     })

#     print("mareponse", response)
#     user = response.json()
#     print("user", user)
#     return user


