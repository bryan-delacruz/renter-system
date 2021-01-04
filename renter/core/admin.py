from django.contrib import admin
from .models import Owner, Renter, Floor, Building, Room

admin.site.register([Owner, Renter, Floor, Building, Room])
