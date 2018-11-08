from django.shortcuts import render

from .models import MenuItem

# Create your views here.


def menu(request):

	context = {
		'items': MenuItem.objects.all(),
		'title': 'メニュ',
	}

	return render(request, 'menu/menu.html', context)


def menu_item_detail(request):

	context = {
		'item': MenuItem.objects.get(id=1)
	}

	return render(request, 'menu/detail.html', context)
