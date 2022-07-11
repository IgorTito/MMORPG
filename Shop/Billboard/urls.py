
from django.urls import path

from .views import CreateAd, imagePage, AdView, create, OneAd, DeleteAd, UpdateAd, EchoList, CreateEcho

urlpatterns = [
    path('', AdView.as_view()),
    path('ad/create/', CreateAd.as_view(), name="ad_create"),
    path('private/', create, name="private"),
    path('image/', imagePage, name="image"),
    path('<int:pk>', OneAd.as_view(), name="one"),
    path('<int:pk>/delete/', DeleteAd.as_view(), name="ad_delete"),
    path('<int:pk>/update/', UpdateAd.as_view(), name="ad_update"),
    path('<int:pk>/echo/', EchoList.as_view(), name="com"),
    path('<int:pk>/echo/create/', CreateEcho.as_view(), name="echo_create"),


]
