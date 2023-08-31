from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_post_list, name='blog'),
    path('hello/', views.hello, name='hello'),
    path('', views.get_all_products, name='product'),
]