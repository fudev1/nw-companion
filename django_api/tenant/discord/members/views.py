from rest_framework import viewsets
from .models import MemberProfile
from .serializers import MemberProfileSerializer


class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

