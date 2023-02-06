from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request):
    all_val_dict = Parser('http://www.cbr.ru/scripts/XML_daily.asp').pars()
    if request.method == 'GET':
        context = {
            'names': all_val_dict,
            'result': 1
        }
        return render(request=request, template_name='main/index.html', context=context)
    if request.method == 'POST':
        convert = request.POST.get('convert')
        convert_value = request.POST.get('amount')
        convert_to = request.POST.get('convert_to')
        if not convert_value:
            convert_value = '1.0'

        result = round(float(all_val_dict[convert].replace(',', '.')) * float(convert_value.replace(',', '.')) / \
                 float(all_val_dict[convert_to].replace(',', '.')), 2)

        context = {
            'from_convert': convert,
            'from_convert_to': convert_to,
            'from_amount': convert_value,
            'names': all_val_dict,
            'result': result
        }
        return render(request=request, template_name='main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')


def all_currency(request):
    all_val_dict = Parser('http://www.cbr.ru/scripts/XML_daily.asp').pars()
    context = {
        'names': all_val_dict
    }
    return render(request, 'main/all_currency.html', context=context)


class Parser:
    def __init__(self, url):
        self.__url = url

    def pars(self):
        request = requests.get(self.__url)
        soup = BeautifulSoup(request.content, 'xml')
        d = dict()
        d['Российский рубль'] = '1.0'
        for i, j in zip(soup.findAll('Name'), soup.findAll('Value')):
            d.setdefault(i.text, j.text)
        return d
