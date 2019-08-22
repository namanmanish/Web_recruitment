from django.contrib import admin
from .models import Person
from .models import State
from .models import City
from .models import College

admin.site.register(Person)
admin.site.register(State)
admin.site.register(City)
admin.site.register(College)

# Register your models here.
