from django.urls import path
from .views import PostList, PostDetail, NewsCreate, NewsUpdate, PostDelete, SearchList, \
   CategoriesList, CategoryDetail, subscribe, unsubscribe


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', SearchList.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='create_news'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='update_news'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/', CategoriesList.as_view(), name='categories'),
   path('categories/<int:pk>/', CategoryDetail.as_view(), name='one_category'),
   path('categories/<int:pk>/subscribers', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]