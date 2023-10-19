from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path("login",views.LoginPage, name="login"),
    path("signup",views.SignupPage, name="signup"),
    path("update_password",views.update_password, name="update_password"),
    path("",views.outindex, name="out_index"),
    path("index",views.index, name ="index"),
    path("product",views.product, name ="product"),
    path("product_detail/<slug:slug>",views.product_detail, name ="product_detail"),
    path("cart",views.cart, name ="cart"),
    path("delete_cart/<str:itemcode>",views.delete_cart, name ="delete_cart"),
    path("delete_all/<str:uid>",views.delete_all, name ="delete_all"),
    path('update_cart/<int:booking_id>', views.update_cart, name='update_cart'),
]

urlpatterns += staticfiles_urlpatterns() 

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)