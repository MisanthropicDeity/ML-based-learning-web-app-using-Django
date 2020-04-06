from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home),
    path('img_enc/',views.proc),
    path('imgEnc/',views.get_img)
]
