from django.shortcuts import render
from . import model


def home(request):
    return render(request, 'index.html')


def result(request):
    salary = int(request.GET['salary'])
    age = int(request.GET['age'])
    prediction = model.pre(age, salary)
    return render(request, 'leaves.html', {'result': prediction})
