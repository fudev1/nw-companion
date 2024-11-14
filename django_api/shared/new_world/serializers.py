from rest_framework import serializers
from .models import NwCompany


class NwCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = NwCompany
        fields = ['name', 'server', 'faction', 'owner']


        # extra_kwargs = {
        #     'server': {'required' : True},
        # }





        """
        extra_kwargs est un dictionnaire qui permet de spécifier des params supplémentaire pour certains champs du modèle
        - read_only
        - write_only
        - required 
        - allow_blank
        interet : flexibilité (patch)
        """

