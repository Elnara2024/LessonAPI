from django.db import models


class CarMark(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models. Model):
    car_mark = models.ForeignKey(
        CarMark,
        on_delete=models.SET_NULL,
        null=True
    )

    name = models.CharField(max_length=255)

    DOOR_CHOICES = (
        (2, "2"),
        (4, "4")
         )
    doors = models.IntegerField(choices=DOOR_CHOICES)

    year = models.DateField()
    date_of_create = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="Images")

    def __str__(self):
          return f"{str(self.car_mark.name)} - {self.name}"





