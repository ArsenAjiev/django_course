from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    #  path('', index, name='home'),
    #  path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('add-news/', add_news, name='add_news'),

    # path('test/', test),

]