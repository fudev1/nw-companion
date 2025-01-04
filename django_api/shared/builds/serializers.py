from rest_framework import serializers
from .models import NwBuild, NwEquipmentSet

class NwEquipmentSetSerializer(serializers.ModelSerializer):
    class Meta: 
        model = NwEquipmentSet
        fields = '__all__'


class NwBuildSerializer(serializers.ModelSerializer):
    equipment = NwEquipmentSetSerializer(required=False)
    
    class Meta:
        model = NwBuild
        fields = '__all__'

    def create(self, validated_data):
        equipment_data = validated_data.pop('equipment', None)
        build = NwBuild.objects.create(**validated_data)
        
        if equipment_data:
            NwEquipmentSet.objects.create(build=build, **equipment_data)
        
        return build

    def update(self, instance, validated_data):
        equipment_data = validated_data.pop('equipment', None)
        
        # Mise à jour du build
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Mise à jour de l'equipment
        if equipment_data:
            equipment = instance.equipment
            for attr, value in equipment_data.items():
                setattr(equipment, attr, value)
            equipment.save()
            
        return instance