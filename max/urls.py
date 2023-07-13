"""
URL configuration for max project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kassa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('operations/', views.operation_name_list, name='operation_list'),
    path('operations/delete/', views.delete_operation_name, name='operation_delete'),
    path('operations/update/<int:pk>/', views.edit_operation_name, name='operation_edite'),
    path('operations/add', views.add_operation_name, name='operation_add'),
    path('sales/', views.sale_list, name='sale_list'),
    path('sale/', views.sale, name='sale'),
    path('sale/<int:pk>/', views.sale, name='view_sale'),
    path('sale/add', views.add_sale, name='add_sale'),

]
