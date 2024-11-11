from django.urls import path
from .views import MaterialViewSet, ProductViewSet

material_list = MaterialViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

material_detail = MaterialViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('material/add', material_list, name='material-list'),    # Định tuyến đến list và create
    path('material/add/<int:pk>/', material_detail, name='material-detail'),  # Định tuyến đến retrieve, update, delete
    path('product/add', product_list, name='product-list'),
    path('product/add/<int:pk>/', product_detail, name = 'product-detail'),
]
