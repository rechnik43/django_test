from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.root, name='root'),
    path('about/', views.about, name='about'),
    path('items/', views.goods_list, name='goods_list'),
    path('item/<int:number>/', views.goods, name='goods'),
]
