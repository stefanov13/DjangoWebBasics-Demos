from django import path, include  # импорти за urls.py файла
from django.db import models  # импортва вградените model класове
from django import forms  # импорт за формите /forms.py/
from django.core import validators  # build-in валидатори за модели / форми които се пишат във validators=[]
from .models import <Model>  # импортване на модел от файлва models.py който е в текущата директория
from .forms import <Form>  # импортване на формите от файла forms.py който е в текущата директория
from .validators import <validator>  # ако имаме файл на име 'validators' във текущата директория го импортваме и си вкарваме нужните ни валидатори
from django.core.exceptions import ValidationError  # грешката за валидации която вдигаме, ако нашата валидация е грешна
from django.shortcuts import render, redirect  # render е за рендериране на темплейта и подаване на контекста към него, redirect е за препращане към друго view когато ни е нужно
from django.conf import settings  # импортва се във project:urls.py за mediafiles или когато имаме DEBUG = False
from django.conf.urls.static import static  # импортва се във project:urls.py за mediafiles или когато имаме DEBUG = False

# project:urls

# if settings.DEBUG:
#     прави се когато трябва да работи със файлове качени в проекта (не url-и от интернет)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import reverse, reverse_lazy  # когато ни трябва да генерираме динамично url във view-та, model-и и на други места

# templates
app/templatetags/file.py

{% load file %}  # зареждане на файла с custom филтрите и тагове

from django import template # импортване при създаване на къстъм темплейти във файла на темплейтите.
# file.py:
# @register.simple_tag
# def test_tag():
#     pass
{% test_tag as test %}  # Ако e таг и тага връща някакъв резултат задаваме променлива 'test' и на нея закачаме това което връша таг-а
# ако е inclusion_tag той създава нов контекст и трябва само да се зареди файла във темплейта и може да се използва променливата във контекста от тага
# ако е филтър пак се зарежда само файла и филтъра се ползва там където ни трябва {{ name|custom_filter }}

{% load static %}  # зарежда ни static тага за да можем да използваме статичните файлове за проекта
{% extends 'template_name.html' %}  # екстендва зададения темплейт файл
{% block <name> %} {% endblock %}  # декларира се в родителския темплейт и се презаписва в наследяващите го темплейти
{% include <name.html> %}  # вкарва един темплейт файл в друг
{% for %} {% endfor %}  # for цикъл - изисква затварящ таг
{% if %} {% endif %}  # if проверка - изисква затварящ таг

