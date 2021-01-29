from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('silogic', views.silogic, name='silogic'),
    path('addition', views.addition, name='addition'),
    path('additionlogic', views.additionlogic, name='additionlogic')


 ]