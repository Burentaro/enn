from django.shortcuts import render

from .models import MenuItem

from .forms import MenuItemForm

# Create your views here.


def menu(request):

	context = {
		'items': MenuItem.objects.all(),
		'title': 'メニュ',
	}

	return render(request, 'menu/menu.html', context)


def menu_item_detail(request):

	context = {
		'item': MenuItem.objects.get(id=1),
		'title': '詳細'
	}

	return render(request, 'menu/detail.html', context)


def menu_item_create(request):

	form = MenuItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = MenuItemForm()

	context = {
		'form': form,
		'title': 'メニュアイテム登録'
	}

	return render(request, 'menu/create.html', context)

