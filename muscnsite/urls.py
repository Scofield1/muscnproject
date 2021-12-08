from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('mission', views.mission, name='mission'),
    path('visionary', views.visionary, name='visionary'),
    path('membership', views.membership, name='membership'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('subscriber', views.subscriber, name='subscriber'),
    path('base/<str:name>', views.dashboard, name='dashboard'),
]