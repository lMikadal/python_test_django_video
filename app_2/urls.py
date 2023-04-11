from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:id>', views.testid, name='testid'),
    path('home', views.testpage, name='testpage'),
    path('page2/<int:id>', views.testpage2, name='testpage2'),
    path('page3', views.testpage3, name='testpage3'),
]