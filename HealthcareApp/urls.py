from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('diabetic',views.diabetic,name='diabetic'),
    path('heart',views.heart,name='heart'),
]