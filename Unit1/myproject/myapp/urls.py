from django.urls import path
from . import views
urlpatterns = [
    path('hello/',views.hello),
    path('home/' , views.home),
    path('about/' , views.about),
    path('result/' , views.result),
    path('dynamic/<str:name>/', views.dynamic_url),
    path('menuitem/<str:dis>/' , views.menuitem),
    path('movies/<str:mov>/' , views.movies),
    path('recip/' , views.recip),
    path('add/' , views.add),
]
