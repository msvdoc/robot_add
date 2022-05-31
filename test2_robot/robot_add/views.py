from django.shortcuts import render
from . import access_bitrix


# Create your views here.
def index(request):
	txt1 = {'text1': 'Всё удачно!', 'text2': access_bitrix.ac}
	return render(request, 'index.html', context=txt1)