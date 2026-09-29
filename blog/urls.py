from django.urls import path    # 
from . import views     # From current directory, import file named "views"

urlpatterns = [
    path("", views.index, name = 'index'),
    path('specific', views.specific, name= 'specific'),
    path('article/<int:article_id>', views.article, name = 'article')
]