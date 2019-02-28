from django.conf.urls import url
from django.urls import path
from vivek import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    path('whatever/', views.my_view1,name='my_view_name1'),
    path('whatever/', views.my_view2,name='my_view_name2'),

]
