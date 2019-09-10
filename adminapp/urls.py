from django.urls import path,include
from touroperator import views
from django.contrib import admin
from django.urls import path
from adminapp import views
from django.conf.urls import url
from adminapp.admin import admin

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('register',views.signup),  
    path('login',views.signin),  
    path('sigout',views.signout),
    path('adminhome',views.adminhome),
    path('dash',views.dashboard)
    # path('pflow',views.pflow),
    # path('multiplepiecharts',views.multiplepiecharts)
   
]