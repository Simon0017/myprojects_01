from django.urls import path
from . import views
from django.contrib import admin

app_name  = "mart"
urlpatterns = [
     path("",views.home,name='home'),
     path("products",views.goods,name='goods'),
     path("purchase",views.purchase,name='purchase'),
     path('buy/<int:brand_id>/', views.buy, name='buy'),
     path('sales',views.sales,name='sales'),
     path("suppliers",views.store_suppliers,name='suppliers'),
     path("staff",views.view_staff,name='staff'),
     path("shifts",views.staff_shifts,name='shifts'),
     path("model",views.model,name='model')

]
 