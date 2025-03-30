from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    path('make_prediction/',views.make_prediction,name='make_prediction')
]
