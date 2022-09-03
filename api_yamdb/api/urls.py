from . import views
from users import views as user_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', user_views.UserViewSet, basename='users')
router.register('titles', views.TitleViewSet, basename='titles')
router.register('genres', views.GenreViewSet)
router.register('categories', views.CategoryViewSet, basename='categories')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewsViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentsViewSet, basename='comments'
)
urlpatterns = [
    path(
        'auth/signup/',
        user_views.CreateUserViewSet.as_view({'post': 'create'})
    ),
    path(
        'auth/token/',
        user_views.ObtainTokenView.as_view(),
        name='token_obtain_pair'),
    path('', include(router.urls)),
]
