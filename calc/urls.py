from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('add',views.add, name = 'add')
    # path('excel/',views.some_view,name="exportExcel"),
]