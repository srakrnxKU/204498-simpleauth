from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='app.index'),
    path('login/', views.login_page, name='app.login_page'),
    path('logout/', views.logout_page, name='app.logout_page')
]
