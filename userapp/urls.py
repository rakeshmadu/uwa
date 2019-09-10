from django.urls import path,include
from touroperator import views
from django.contrib import admin
from django.urls import path
from userapp import views
from django.conf.urls import url

urlpatterns = [
    path('home/',views.Home),
    path('userhome/',views.UserHome),
    path('admin2/',views.register),
    path('user/',views.userreg),
    path('adminreg/',views.adminRegister),
    path('adminlog/',views.adminLogin),
    path('bookings/',views.bookings),
    path('details/',views.getdtls),
    path('alldtls/',views.alldetails),
    path('pflow/',views.pflow),
    path('online',views.multp),
    path('invid/<int:id>/',views.invid)
]