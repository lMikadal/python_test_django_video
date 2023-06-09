from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('<int:id>', views.testid, name='testid'),
    path('home', views.testpage, name='testpage'),
    path('page2/<int:d_id>', views.testpage2, name='testpage2'),
    path('page3', views.testpage3, name='testpage3'),
    path('form', views.testForm, name='testform'),
    path('sub', views.testInsert, name='sub')
]