from rest_framework import serializers
from .models import CarMark, Car


class CarMarkSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)

    def create(self, validated_date):
        car_mark = CarMark.objects.create(**validated_date)
        return car_mark

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    car_mark_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    doors = serializers.IntegerField()
    year = serializers.DateField()
    date_of_create = serializers.DateTimeField(required=False)
    image = serializers.ImageField()

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        instance.car_mark_id = validated_data.get("car_mark_id", instance.car_mark)
        instance.name = validated_data.get("name", instance.name)
        instance.doors = validated_data.get("doors", instance.doors)
        instance.year = validated_data.get("year", instance.year)
        instance.date_of_create = validated_data.get("car_mark_id", instance.date_of_create)
        instance.image = validated_data.get("image", instance.image)

        instance.save()
        return instance



#----------------------------------------------


class CarMarkSerializer2(serializers.ModelSerializer):
      class Meta:
          model = CarMark
          fields = ['id','name']


class CarSerializer2(serializers.ModelSerializer):
      class Meta:
            model = Car
            fields = '__all__'