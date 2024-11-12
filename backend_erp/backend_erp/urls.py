from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

# Định nghĩa API chào mừng hoặc trang chủ
def welcome(request):
    data = {
        "message": "Welcome to the ERP System API!"
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('db_diy.urls')),
    path('inventory/', include('inventory.urls')),
    path('supplier/', include('supplier.urls')),
    
    # Định tuyến API chào mừng (trang chủ)
    path('', welcome, name='home'),  # Trang chủ trả về thông điệp chào mừng
]

# Thêm cấu hình cho static và media file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
