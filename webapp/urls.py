from django.urls import path
from webapp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savecat/',views.savecat,name="savecat"),
    path('catdisplay/',views.catdisplay,name="catdisplay"),
    path('editcat/<int:dataid>',views.editcat,name="editcat"),
    path('Updatecat/<int:dataid>',views.Updatecat,name="Updatecat"),
    path('delcat/<int:dataid>',views.delcat,name="delcat"),
    path('productpage/',views.productpage,name="productpage"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('prodisplay/',views.prodisplay,name="prodisplay"),
    path('proedit/<int:dataid>',views.proedit,name="proedit"),
    path('proupdate/<int:dataid>',views.proupdate,name="proupdate"),
    path('prodel/<int:dataid>',views.prodel,name="prodel"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout")
]