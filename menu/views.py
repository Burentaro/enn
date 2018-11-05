from django.shortcuts import render

from .models import MenuItem

# Create your views here.

def menu_item_detail(request):

	obj = MenuItem.objects.get(id=1)

	return render(request, 'menu/detail.html', {})