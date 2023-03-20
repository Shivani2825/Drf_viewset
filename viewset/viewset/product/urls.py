
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import *

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewset)
router.register(r'product_item', ItemViewset)

urlpatterns = [
    path("api/", include(router.urls))
]
