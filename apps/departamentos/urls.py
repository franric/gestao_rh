from django.urls import path
from .views import DepartamentosList, DepartamentosEdit, DepartamentosNovo, DepartamentosDelete


urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('edit/<int:pk>', DepartamentosEdit.as_view(), name='update_departamento'),
    path('novo/', DepartamentosNovo.as_view(), name='create_departamento'),
    path('delete/<int:pk>', DepartamentosDelete.as_view(), name='delete_departamento'),
]
