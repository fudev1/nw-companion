from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets 
from .models import Character, Role, MemberProfile, CharacterRole, User
from .serializers import CharacterSerializer, RoleSerializer, MemberProfileSerializer, CharacterRoleSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

class CharacterRoleViewSet(viewsets.ModelViewSet):
    queryset = CharacterRole.objects.all()
    serializer_class = CharacterRoleSerializer