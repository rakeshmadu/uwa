from django.urls import path,include
from touroperator import views
from django.contrib import admin
from django.urls import path
from touroperator import views
from django.conf.urls import url
from touroperator.admin import admin



urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home),
    path('signup',views.Sign),
    path('signin',views.login),
    path('logout',views.logout),
    path('book',views.booking),
    path('blist',views.booklist),
    path('count',views.count),
    path('list',views.reglist),
    path('multy/<int:id>/',views.multy),
   
    # url(r'^multy/(?P<id>\d+)/$',views.multy)

]