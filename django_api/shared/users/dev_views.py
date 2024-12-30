from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TenantUser

@api_view(['POST'])
@permission_classes([AllowAny])  # Permet l'accès sans authentification
def dev_get_token(request):
    """Endpoint temporaire pour obtenir un token JWT pour les tests"""
    user_email = request.data.get('email', 'matteo.divita@outlook.be')
    try:
        user = TenantUser.objects.get(email=user_email)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    except TenantUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)