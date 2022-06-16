from .import views
from django.urls import path

urlpatterns=[
    path('<slug:slug>',views.Blogview.as_view(), name='blog_view'),
    path('about/',views.aboutview.as_view(), name='about_view'),
    path('',views.postlist.as_view(), name='home_view')
]