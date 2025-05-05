from django.urls import path
from . import views
urlpatterns = [
    path('',views.test_app, name='test_app'),
    path('aboutUs/',views.about, name= 'about')
]