from django.urls import path,include
from produto import views as v

app_name='produto'

urlpatterns = [
    path('',v.produt_list, name='produt_list'),
    path('<int:pk>/',v.produt_detail, name='produt_detail'),
    
]
