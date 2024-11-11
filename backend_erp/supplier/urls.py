from django.urls import path
from .views import CompanyViewSet, SupplierViewSet, BankAccountViewSet

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

supplier_list = SupplierViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

supplier_detail = SupplierViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

banker_list = BankAccountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

banker_detail = BankAccountViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('company/add', company_list, name='company-list'),    # Định tuyến đến list và create
    path('company/add/<int:pk>/', company_detail, name='company-detail'),  # Định tuyến đến retrieve, update, delete
    path('supplier/add', supplier_list, name='supplier-list'),
    path('supplier/add/<int:pk>/', supplier_detail, name = 'supplier-detail'),
    path('banker/add', banker_list, name='banker-list'),
    path('banker/add/<int:pk>/', banker_detail, name = 'banker-detail'),
]
