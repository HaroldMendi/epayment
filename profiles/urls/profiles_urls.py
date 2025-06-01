from django.urls import path
from ..views.profiles import ProfileListView, ProfileCreationForm, ProfileDetailView, ProfileUpdateView, AccessDeniedView
from ..views.users import UserCreateView, LoginView, Logout
from ..views.dashboard import DashboardView


urlpatterns = [
    path('',DashboardView.as_view(),name='home'),
    path('profile-list',ProfileListView.as_view(),name='profile_list'),
    path('profile-create',ProfileCreationForm.as_view(),name='profile_create'),
    # path('profile-update/<slug:slug>',ProfileUpdateView.as_view(),name='profile_update'),
    path('profile-update/<int:pk>/',ProfileUpdateView.as_view(),name='profile_update'),
    path('profile-detail/<slug:slug>',ProfileDetailView.as_view(),name='profile_detail'),
    path('access-denied',AccessDeniedView.as_view(),name='access_denied'),
    path('epayment/register',UserCreateView.as_view(),name='register'),
    path('epayment/login',LoginView.as_view(),name='login'),
    path('epayment/logout',Logout,name='logout'),
]


