from . import views 
from django.urls import path
from myapi.views import Payment_api


urlpatterns=[
    path('home/',views.home,name='home'),
    path('course/<int:id>',views.Course,name='Course'),
    path('Inquerry',views.CallRequest,name='INQUERRY'),
    path('register',views.register,name='register'),
    path('login',views.Login,name='login'),
    path('',views.test),
    path('payment/',Payment_api.as_view()),
    path('abc',views.check,name='abc'),
    path('tes',views.tes),
]