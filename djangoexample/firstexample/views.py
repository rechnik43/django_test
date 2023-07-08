from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    string1 = "<h1>Hello World</h1>"
    string2 = "<h2>My name is <b>Serge</b></h2>"
    result_string = string1 + string2
    return HttpResponse(result_string)

def root(request):
    string3 = "<h1>Изучаем django</h1>"
    string4 = "<strong>Автор</strong>: <i>Салов С.Н.</i>"
    result_string1 = string3 + string4
    return HttpResponse(result_string1)

def about(request):
    name = "<h2>Имя: Сергей</h2>"
    middle_name = "<h2>Отчество: Николаевич</h2>"
    surname = "<h2>Фамилия: Салов</h2>"
    phone = "<h2>телефон: 8-923-600-01-02</h2>"
    email = "<h2>email: salov@mail.ru</h2>"
    res = name + middle_name + surname + phone + email
    return HttpResponse(res)

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def goods(request, number):
    result = None
    for i in range(len(items)):
        if number == items[i]["id"]:
            result = "<h1>Карточка товара</h1>"
            result += f'{items[i]["name"]}, {items[i]["quantity"]} штук<br> '
    if result is None:
        result = "<h1>Товар не найден</h1>"
    link1 = "<a href = '/items'>список товаров</a>"
    return HttpResponse(result+link1)

def goods_list(request):
    goods = ' '
    title = "<h1>Список товаров</h1>"
    for i in range(len(items)):
        goods += f'{items[i]["id"]}: "<a href=/item/{items[i]["id"]}>{items[i]["name"]}</a>", {items[i]["quantity"]} штук<br>'
    goods_all = title + goods
    return HttpResponse(goods_all)


