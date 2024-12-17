from urllib.parse import urlencode
from rest_framework import viewsets
from .serializers import TenantUserSerializer
from .models import TenantUser
from django.utils.timezone import now

import requests 
from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect
from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken


DISCORD_CLIENT_ID = settings.DISCORD_CLIENT_ID
DISCORD_CLIENT_SECRET = settings.DISCORD_CLIENT_SECRET
DISCORD_REDIRECT_URI = settings.DISCORD_REDIRECT_URI
DISCORD_AUTH_URL = settings.DISCORD_AUTH_URL




# Create your views here.
class TenantUserViewSet(viewsets.ModelViewSet):
    queryset = TenantUser.objects.all()
    serializer_class = TenantUserSerializer




def generate_jwt_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# ➡️ 1. Récupérer `code` envoyé par Discord
# ➡️ 2. Echanger `code` contre un `access_token` & `refresh_token`
# ➡️ 3. Utiliser `access_token` pour call api (/users/@me) et récupérer info users // Return JSON
# ➡️ 4. Vérifier si user existe : update ou le créer => DB


def discord_login(request: HttpRequest):
    return redirect(DISCORD_AUTH_URL)


def discord_login_redirect(request: HttpRequest):
    
    # ✅➡️ 1. Récupérer `code` envoyé par Discord
    code = request.GET.get("code")
    if not code:
        return JsonResponse({'error': "No code provided"}, status=400)



    # ✅➡️ 2. Echanger le code contre access_token
    token_url = "https://discord.com/api/oauth2/token"
    data = {
        "client_id": settings.DISCORD_CLIENT_ID,
        "client_secret": settings.DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.DISCORD_REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_response = requests.post(token_url, data=data, headers=headers)
    if token_response.status_code != 200:
        return JsonResponse({"error": "Failed to obtain token"}, status=400)

    token_data = token_response.json()
    access_token = token_data.get("access_token")



    # ✅➡️ 3. Récupérer les info user from discord
    user_response = requests.get(
       "https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {access_token}"}, 
    )
    if user_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch user info"}, status=400)
    
    user_data = user_response.json()
    # 🎯 print(f'mon user data:', user_data)



    # ✅➡️ 4. Créer ou mettre à jour user discord => DB
    user, created = TenantUser.objects.update_or_create(
        discord_id=user_data["id"],
        defaults={
            # Champs indispensables (use [])
            "username": user_data["username"],
            "global_name": user_data["global_name"],
            "email": user_data["email"],
            "avatar": user_data["avatar"],
            "locale": user_data["locale"],
            "public_flags": user_data["public_flags"],

            # Champs optionnels (use get() avec valeur par defaut si aucun key)
            "mfa_enabled": user_data.get("mfa_enabled", False),
            "banner": user_data.get("banner", None),
            "banner_color": user_data.get("banner_color", None),
            "accent_color": user_data.get("accent_color", None),
            "verified": user_data.get("verified", False),

            # Champs généré coté server
            "last_login": now(),
        }
    )



    # ✅➡️ 5. Générer les tokens JWT
    # tokens = generate_jwt_for_user(user)
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)



    # # ✅➡️ 5. Reponse
    # return JsonResponse({
    #     "message": "Utilisateur authentifié",
    #     "user": {
    #         "id": user.discord_id,
    #         "username": user.username,
    #         "global_name": user.global_name,
    #         "email": user.email,
    #         "avatar": user.avatar,
    #         "last_login": user.last_login,
    #     },
    #     "tokens": tokens
    # })


    # ✅➡️ 5. Réponse : Rediriger vers le frontend avec les tokens
    redirect_url = "http://localhost:4200/login/callback"
    query_params = urlencode({
        "access": access_token,
        "refresh": str(refresh),
        "user_id": user.discord_id,
        "username": user.username,
        "global_name": user.global_name,
        "avatar": user.avatar,
        "email": user.email,
        "locale": user.locale,
        "banner_color": user.banner_color,
        "last_login": user.last_login.isoformat(),
    })

    # 🎯🎯 --. DEBUG 
    # print("DEBUG - Données envoyées au frontend:")
    # print("Access Token:", access_token)
    # print("Refresh Token:", str(refresh))
    # print("Query Params:", query_params)


    return redirect(f"{redirect_url}?{query_params}")
