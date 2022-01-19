from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('int:<package_id>/', views.package_detail, name='package_detail'),
    path('add/', views.add_package, name='add_package'),
    path('edit/<int:package_id>/', views.edit_package, name='edit_package'),
    path('deactivate/<int:package_id>/', views.deactivate_package,
         name='deactivate_package'),
    path('activate/<int:package_id>/', views.activate_package,
         name='activate_package'),
]
