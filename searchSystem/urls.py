from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

from . import views
from . import plantViews

app_name = 'searchSystem'

urlpatterns = [
    path('index/',plantViews.index,name='index'),
    path('logOut/', views.LogOutView.as_view(), name='log_out'),

    path('search/', plantViews.searchByInput, name='search'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('signUp/', views.SignUpView.as_view(), name='signUp'),
    path('searchByInput/', plantViews.searchByInput, name='searchByInput'),
    path('searchByKeywords/', plantViews.searchByKeywords, name='searchByKeywords'),
    path('search/detail/<int:disease_id>/',plantViews.detail,name='detail'),
    path('comment/', plantViews.comment, name='comment'),

    path('diseaseGraph/', plantViews.diseaseGraph, name='Graph'),
    path('buildNode/', plantViews.buildNode),
    path('change/profile/', views.ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='change_email'),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT})

]


# handler404 = views.page_not_found