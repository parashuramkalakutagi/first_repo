

from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('product',views.product_datail,basename='product')
router.register('product_inventory_datail',views.product_inventory_datail,basename='product_inventory_datail')
router.register('media_datai',views.media_datail,basename='media_datai')
router.register('catagory_datail',views.catagory_datail,basename='catagory_datail')
router.register('stock_datail',views.stock_datail,basename='stock_datail')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh')                                             
                    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
