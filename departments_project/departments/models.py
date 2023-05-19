from django.db import models
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First - Name')
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    '''
    Ако искаме да създадем динамично url по дадено поле от модела
    '''
    # def get_absolute_url(self):
    #     return reverse("profile-data", kwargs={"first_name": self.first_name})
