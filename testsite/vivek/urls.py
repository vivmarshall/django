from django.conf.urls import url
from django.urls import path
from vivek import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    path('host/', views.hostpage.as_view(),name='host'),
    path('install/', views.installpage.as_view(),name='install'),

    path('hostname/', views.my_view1,name='my_view_name1'),
    path('packageinstall/', views.take_view,name='take_view'),

]
