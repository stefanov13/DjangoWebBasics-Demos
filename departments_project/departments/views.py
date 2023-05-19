from django.shortcuts import get_object_or_404, render, redirect


from .models import Person
from .forms import TestForm, ModelTestForm


def index(request):
    # Взема всичко обекти от базата
    users = Person.objects.all()

    context = {
        'users': users
    }

    return render(request, 'index.html', context)


def profile(request, ime):
    # Взема определен потребител по първо име (поле в базата)
    user = Person.objects.filter(first_name=ime).get()

    # user = get_object_or_404(Person, first_name=ime)

    context = {
        'user': user
    }

    # redirect със get_absolute_url който е в модела Person
    # return redirect(user)

    return render(request, 'profile.html', context)


def test_form(request):
    if request.method == 'GET':
        # Зарежда празна форма
        form = ModelTestForm()
    else:  # if request.method == 'POST':
        # Зарежда
        form = ModelTestForm(request.POST)
        # проверява дали въведените данни във формата са валидни
        if form.is_valid():

            # Ако формата не е ModelForm, а е само Form
            # Вземаме висчки нужни полета от формата

            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # age = form.cleaned_data.get('age')

            # Създаваме нов обект в базата
            # Person.objects.create(first_name=first_name, last_name=last_name, age=age)

            form.save()

            # redirect with named url / view
            return redirect('profile-data', form.cleaned_data['first_name'])

            # redirect with absolute url
            # return redirect(f'127.0.0.1/departments/profile{form.cleaned_data.get("first_name")}')

            # redirect with relative url
            # return redirect(f'profile/{form.cleaned_data.get("first_name")}/')

    # Името на речника не е от значение
    data = {
        'form': form
    }

    return render(request, 'register.html', data)