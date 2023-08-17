
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static  # 

urlpatterns = [

    # super admin URLs
    path('super_admin/', admin.site.urls),

    # Site admin URLs
    path('', include('accounts.urls')),
    
    path('site_admin/', include('accounts.urls')),
    path('site_admin/', include('menu.urls')),

    path('api/', include('accounts.api_urls')),
    path('api/', include('menu.api_urls')),
    path('api/token/', TokenObtainPairView.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
handler404  = "utils.errors.handler404"
handler500 = "utils.errors.handler500"  