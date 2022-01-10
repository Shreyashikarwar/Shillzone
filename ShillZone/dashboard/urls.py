from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_view_link'),
    path('manage-profile', views.ManageProfileView.as_view(), name='manage_profile_view_link'),
    path('create', views.CreateView.as_view(), name='create_view_link'),
    path('add-user', views.AddUserView.as_view(), name='add_user_view_link'),
    path('manage-user', views.ManageUserView.as_view(), name='manage_user_view_link'),
    path('edit-user', views.EditUser.as_view(), name= 'edit_user_view_link'),
    path('delete-user', views.DeleteUser.as_view(), name= 'delete_user_view_link'),
    path('password-update', views.PasswordUpdateView.as_view(), name='password_update_view_link'),

    # path('following-pages', views.FollowingPageView.as_view(), name='following_view_link'),
    # path('notification', views.NotificationView.as_view(), name='notification_view_link'),
    # path('my-pages', views.MyPagesView.as_view(), name='my_pages_view_link'),

    # path('promotion', views.PromotionView.as_view(), name='promotion_view_link')
]