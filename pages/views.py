from django.shortcuts import render

from menu.models import MenuItem

# Create your views here.


def home(request):

	context = {
		'title': 'ホーム'
	}

	return render(request, 'pages/home.html', context)


def greeting(request):

	context = {
		'title': '挨拶'
	}

	return render(request, 'pages/greeting.html', context)


def courses(request):

	context = {
		'title': 'コース'
	}

	return render(request, 'pages/courses.html', context)
