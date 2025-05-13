from django.http import HttpResponse


def data_view(request):
    return HttpResponse('<h1>Это страница Data</h1>'
                        '<h2>Это Первый проект Django на Python на странице Data.</h2>'
                        '<p>Здесь содержимое для Data.</p>')


def test_view(request):
    return HttpResponse('<h1>Это страница Test</h1>'
                        '<h2>Это Первый проект Django на Python на странице Test.</h2>'
                        '<p>Здесь содержимое для Test.</p>')


from django.shortcuts import render

# Create your views here.
