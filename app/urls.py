from django.conf.urls import url
from app import views

urlpatterns = [
    # Projeto Intelligent Promoter
    url(r'^intelligent_promoter/image/$', views.image_list),
   

    
    # Projeto Identificador de Fungos - Gabriel
    # Coloquem suas Urls aqui abaixo
    #\/ \/ \/ \/ \/ \/ 
 
    # Projeto Identificador de Fungos - Gabriel
    # Coloquem suas Urls aqui abaixo
    #\/ \/ \/ \/ \/ \/ 
  url(r'^agricultura/$', views.agricutura),

]