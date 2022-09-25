from django.conf.urls import url,include
from ada import views

app_name='ada'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('admindash/',views.admindash,name='admindash'),
]
