from django.urls import path
from websiteapp import views

urlpatterns=[
    path('webindexpage/',views.webindexpage,name="webindexpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('brandpage/<catg>',views.brandpage,name="brandpage"),
    path('singleproduct/<int:dataid>/',views.singleproduct,name="singleproduct"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('contactdisplay/',views.contactdisplay,name="contactdisplay"),
    path('login/',views.login,name="login"),
    path('user_reg/',views.user_reg,name="user_reg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('cart/',views.cart,name="cart"),
]