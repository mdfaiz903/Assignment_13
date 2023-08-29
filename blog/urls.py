from django.urls import path
from . views import blog_view
urlpatterns = [
    path('blog_view/',blog_view,name='blog_view')
]
