from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    adress = models.TextField()
    cellphone = models.CharField(max_length=9, blank=True, null=True)
    mail = models.EmailField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = '01-Propietarios'
        ordering = ['name', 'surname']

    def __str__(self):
        return "{} {}, DNI: {}, Dirección: {}, Celular {}, Correo {}".format(self.name, self.surname, self.dni,
                                                                          self.adress, self.cellphone, self.mail)


class Renter(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    adress = models.TextField()
    cellphone = models.CharField(max_length=9, blank=True, null=True)
    mail = models.EmailField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = '02-Inquilinos'
        ordering = ['name', 'surname']

    def __str__(self):
        return "{}, {} DNI: {} Dirección: {} Celular {} Correo {}".format(self.name, self.surname, self.dni,
                                                                          self.adress, self.cellphone, self.mail)


class Building(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '03-Edificios'
        ordering = ['name']

    def __str__(self):
        return "Edificio: {}".format(self.name)


class Floor(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '04-Pisos'
        ordering = ['name']

    def __str__(self):
        return "Piso: {}".format( self.name)


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
    priceMaintenance = models.PositiveSmallIntegerField(null=True, blank=True)
    priceWarranty = models.PositiveSmallIntegerField(null=True, blank=True)
    dateInitial = models.DateField(null=True, blank=True)
    dateFinal = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '05-Habitaciones'
        ordering = ['buildingId', 'floorId', 'renterId', 'priceTotal', 'dateInitial', 'dateFinal']

    def __str__(self):
        return "Edificio: {}, Piso: {}, Inquiligno: {}, Precio Total {}, fecha Inicial: {}, fecha Fin {}".format(
            self.buildingId, self.floorId, self.renterId, self.priceTotal, self.dateInitial, self.dateFinal)
