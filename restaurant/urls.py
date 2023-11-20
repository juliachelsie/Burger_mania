from restaurant import views
from django.urls import path

app_name = 'restaurant'

urlpatterns = {
    path('', views.reserve_table, name='reserve_table')
}
