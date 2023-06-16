from django.contrib import admin
from .models import Person, Pet


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
