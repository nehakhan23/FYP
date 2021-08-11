"""gamification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from mysite.core import views as core_views
from django.urls import path
from django.contrib.auth import views as auth_views
from GamificationForEmployees import  views

urlpatterns = [
    url(r'^user_login/$', auth_views.LoginView.as_view(),{'template_name': 'login.html'}, name='user_login'),
    url(r'^admin_login/$', auth_views.LoginView.as_view(),{'template_name': 'login.html'}, name='admin_login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^user/(?P<value>\w+)/monthly$', views.userMonthlyPerformanceByID, name='usermonthlyperformancebyid'),
    url(r'^user/(?P<value>\w+)/yearly$', views.userYearlyPerformanceByID, name='useryearlyperformancebyid'),

   

    path('',views.home),
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('predict/', views.predict_chances, name = 'submit_prediction'),
    # path('bonus/', views.predict_chances, name = 'submit_prediction'),
    path('change_month',views.changeMonth,name='changeMonth'),
    path('createuser',views.createUsers,name='createUsers'),
    path('changepassword',views.changePassword,name='changePassword'),
    path('get_data_by_eno',views.getDataByEno,name='getDataByEno'),
    path('get_data_by_month',views.getDataByMonth,name='getDataByMonth'),
    
    

    path('user',views.signup,name='usersignup'),
    # path('user/list',views.usersList,name='userlist'),
    # path('user/update',views.userUpdate,name='userupdate'),

    path('users/monthly',views.usersDataMonthly,name='usersmonthlyData'),
    path('users/yearly',views.usersDataYearly,name='usersyearlyData'),
    
    path('users/performance/monthly',views.usersMonthlyPerformance,name='usersmonthlyPerformance'),
    path('users/performance/yearly',views.usersYearlyPerformance,name='usersyearlyPerformance'),


    


]
