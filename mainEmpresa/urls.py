from django.urls import path
from . import views

app_name = "mainEmpresa"

urlpatterns = [
    path("", views.EmpresaList.as_view(), name="list"),
    path("create/", views.EmpresaCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.EmpresaUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", views.EmpresaDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", views.EmpresaDelete.as_view(), name="delete"),
]
