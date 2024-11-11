from django.urls import path
from .views import RoleViewSet, UsersViewSet
from .views import RegisterView, LoginView, UserView, LogoutView
role_list = RoleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

role_detail = RoleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# users
users_list = UsersViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

users_detail = UsersViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('settings/roles/add', role_list, name='role-list'),    # Định tuyến đến list và create
    path('settings/roles/add/<int:pk>/', role_detail, name='role-detail'),  # Định tuyến đến retrieve, update, delete
    path('users/add', users_list, name='users-list'),    # Định tuyến đến list và create
    path('users/add/<int:pk>/', users_detail, name='users-detail'),  # Định tuyến đến retrieve, update, delete
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]