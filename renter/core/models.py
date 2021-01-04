from django.db import models

class Owner(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    adress = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=9, blank=True, null=True)
    mail = models.EmailField(unique=True, blank=True, null=True)


class Renter(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    adress = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=9, blank=True, null=True)
    mail = models.EmailField(unique=True, blank=True, null=True)


class Floor(models.Model):
    Number = models.IntegerField(5)


class Building(models.Model):
    Name = models.CharField(max_length=50)

class Room(models.Model):
    owenerId = models.ForeignKey(Owner, on_delete=models.CASCADE)
    renterId = models.ForeignKey(Renter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    state = models.BooleanField(default=True)
    roomArea = models.PositiveSmallIntegerField(blank=True, null=True)
    roomAdress = models.CharField(max_length=100, null=True, blank=True)
    floorId = models.ForeignKey(Floor, on_delete=models.CASCADE)
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)
    ownBathroom = models.BooleanField(default=True, null=True, blank=True)
    priceLight = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    priceWater = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    priceInternet = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    priceSignalTelevision = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    priceRoom = models.PositiveSmallIntegerField()
    priceSubTotal = models.PositiveSmallIntegerField(null=True, blank=True)
    priceTotal = models.PositiveSmallIntegerField()
    dateInitial = models.DateField(null=True, blank=True)
    dateFinal = models.DateField(null=True, blank=True)
