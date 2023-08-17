from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model =Menu
        # fields = '__all__'
        fields = ('id','meal_name','describe','price','category','image')
        


