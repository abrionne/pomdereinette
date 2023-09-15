"""
URL configuration for pom_de_reinette project.

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
from django.urls import path, include
from salaire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', views.custom_login, name='login'),
    path('logout/',views.custom_logout, name='logout'),
    path('restricted_access/',views.restricted_access, name='restricted_access'),
    path("home/", views.home,name="home"),
    path('delete/', views.delete, name='delete'),
    path("cost/list/", views.cost_list,name="cost_list"),
    path("cost/create/", views.cost_create,name="cost_create"),
    path("cost/detail/<int:id>/", views.cost_detail,name="cost_detail"),
    path("cost/update/<int:id>/", views.cost_update,name="cost_update"),
    path("cost/delete/<int:id>/", views.cost_delete,name="cost_delete"),
    path("pricing/list/", views.pricing_list,name="pricing_list"),
    path("pricing/create/", views.pricing_create,name="pricing_create"),
    path("pricing/detail/<int:id>/", views.pricing_detail,name="pricing_detail"),
    path("pricing/update/<int:id>/", views.pricing_update,name="pricing_update"),
    path("pricing/delete/<int:id>/", views.pricing_delete,name="pricing_delete"),
    path("contract/list/", views.contract_list,name="contract_list"),
    path("contract/create/", views.contract_create,name="contract_create"),
    path("contract/detail/<int:id>/", views.contract_detail,name="contract_detail"),
    path("contract/update/<int:id>/", views.contract_update,name="contract_update"),
    path("contract/delete/<int:id>/", views.contract_delete,name="contract_delete"),
    path("month/list/", views.month_list,name="month_list"),
    path("month/list_contract/<int:id>/", views.month_list_contract,name="month_list_contract"),
    path("month/create/", views.month_create,name="month_create"),
    path("month/detail/<int:id>/", views.month_detail,name="month_detail"),
    path("month/update/<int:id>/", views.month_update,name="month_update"),
    path("month/delete/<int:id>/", views.month_delete,name="month_delete"),
    path("month/day_update/<int:id>", views.day_update,name="day_update"),
    path("summary/list/", views.summary_list,name="summary_list"),
    path("summary/create/", views.summary_create,name="summary_create"),
    path("summary/detail/<int:id>/", views.summary_detail,name="summary_detail"),
    path("summary/update/<int:id>/", views.summary_update,name="summary_update"),
    path("summary/delete/<int:id>/", views.summary_delete,name="summary_delete"),
    path("contractend/list/", views.contractend_list,name="contractend_list"),
    path("contractend/create/", views.contractend_create,name="contractend_create"),
    path("contractend/detail/<int:id>/", views.contractend_detail,name="contractend_detail"),
    path("contractend/update/<int:id>/", views.contractend_update,name="contractend_update"),
    path("contractend/delete/<int:id>/", views.contractend_delete,name="contractend_delete"),
]