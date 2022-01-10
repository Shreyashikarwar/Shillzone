from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign_up_view_link'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in_view_link'),
    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_view_link'),
    path('verification/', views.VerificationView.as_view(), name='verification_view_link'),
]