from . import views
from django.urls import path


urlpatterns = [
    path('', views.User_reservation.as_view(), name='book'),

]
