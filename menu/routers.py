#./routers.py
from rest_framework import routers
from menu.viewsets import MenuViewSet
router = routers.SimpleRouter()
router.register(r'menu', MenuViewSet, basename='menu')


#restaurant/urls.py
from django.contrib import admin
from django.urls import path, include

from routers import router
    
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'restaurant'), namespace='restaurant'))
]