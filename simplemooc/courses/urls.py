from django.urls import include
from django.urls import path
from simplemooc.courses import views

app_name='courses'

urlpatterns = [

    path('', views.index, name='index'),
	path('<slug:atalho>', views.details, name='details' ),
    #path('contato/', views.contato, name='contato'),
    
]