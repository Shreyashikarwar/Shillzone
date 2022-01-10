import random
from urllib import request
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from django.template.loader import render_to_string, get_template
import random as r
import string
from custom_user.models import User
from django.conf import settings
import smtplib
import email.message
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views import generic
from django.contrib.auth.models import auth
from .forms import SignUpForm


class SignUpView(generic.View):

    def get(self, request, *args, **kwargs):
        sign_up_form = SignUpForm

        return render(request, 'accounts/sign-up.html', {'sign_up_form': sign_up_form})

    def post(self, request, *args, **kwargs):
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(request, 'User Registered Successfully.')
        else:
            messages.error(request, sign_up_form.errors)

        return HttpResponseRedirect(reverse('accounts_app_link:sign_up_view_link'))


class SignInView(generic.View):
    def get(self, request, *args, **kwargs):

        return render(request, 'accounts/sign-in.html')

    def post(self, request, *args, **kwargs):

        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"{email} Logged In Successfully")
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('accounts_app_link:sign_in_view_link'))

    # def register(request):
    #
    #     if request.method == POST:
    #         username = request.POST('username')
    #         email = request.POST('email')
    #         password1 = request.POST('password1')
    #         password2 = request.POST('password2')
    #
    #         if password1 == password2:
    #             if User.objects.filter(username=username).exists():
    #                 print('Username taken')
    #             elif User.objects.filter(email == email):
    #                 print('Email taken')
    #             else:
    #                 user = User.objects.create_user(username=username, password1=password1, password2=password2,
    #                                                 email=email)
    #                 user.save();
    #                 return redirect('/accounts')
    #     else:
    #         return render(request, 'sign-in.html')
    #


class ForgotPasswordView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/forgot.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if User.objects.all().filter(email=request.POST['email']).exists():
                print(request.POST['email'])
                otp = ""
                for i in range(4):
                    otp += str(r.randint(1, 9))
                    print(otp)
                user_instance = get_object_or_404(User, email=request.POST['email'])
                user_instance.otp = otp
                user_instance.save()
                data_content = {"username": user_instance.email,
                                "user_otp": user_instance.otp}
                email_content = 'accounts/email.html'
                email_template = get_template(email_content).render(data_content)
                reciver_email = user_instance.email
                print(reciver_email)
                print(settings.EMAIL_HOST_USER)
                Subject = 'Need a password?'
                email_msg = EmailMessage(Subject, email_template, settings.EMAIL_HOST_USER, [reciver_email],
                                         reply_to=[settings.EMAIL_HOST_USER])
                email_msg.content_subtype = 'html'
                email_msg.send(fail_silently=False)

                messages.success(request, "OTP has been sent to your registered email if not then resend again")
                return render(request, 'accounts/verification.html', {'email': request.POST['email']})
            else:
                messages.error(request, "Please enter registered email")

        return render(request, 'accounts/forgot.html')


class VerificationView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, "accounts/verification.html")

    def post(self, request, *args, **kwargs):

        first = request.POST["first"]
        print(first)
        second = request.POST["second"]
        print(second)
        third = request.POST["third"]
        print(third)
        forth = request.POST["forth"]
        print(forth)
        otp = request.POST["first"] + request.POST["second"] + request.POST["third"] + request.POST["forth"]

        user = get_object_or_404(User, email=request.POST['email'])
        userprofile_instance = get_object_or_404(User, email=user)
        print(userprofile_instance.otp, otp)
        print(type(userprofile_instance.otp), type(otp))
        if userprofile_instance.otp == int(otp):
            userprofile_instance.verify_status = True
            try:
                password1 = request.POST["password1"]
                print(password1)
                password2 = request.POST["password2"]
                print(password2)
                if password1 == password2:
                    userprofile_instance = get_object_or_404(User, email=request.POST['email'])
                    userprofile_instance.set_password(password1)
                    print(email)
                    userprofile_instance.save()
                    messages.success(request, 'Your Password is changed successfully')
                    return render(request, 'accounts/sign-up.html')
            except:
                userprofile_instance.verify_status = False
                messages.error(request, 'Entered OTP is WRONG.')
        else:
            messages.error(request, "Entered OTP or Password doesn't matched")
            return render(request, 'accounts/verification.html', {'email': request.POST['email']})
        return HttpResponseRedirect(reverse('/accounts'))


class ResendCodeView(generic.View):
    def post(self, request):
        user_email = request.POST["user_email"]
        if User.objects.filter(email=user_email).filter(is_active=False).exists():

            otp = ''.join([random.choice(string.digits)
                           for i in range(0, 4)])
            # User.objects.filter(email=email).filter(is_active=False).update(otp=otp)
            # user_instance = get_object_or_404(User, email=email)
            ################################################ EMAL SEND CODE START ##############
            user_instance = get_object_or_404(User, email=request.POST['email'])
            user_instance.otp = otp
            user_instance.save()
            
            data_content = {"username": user_instance.email,
                            "user_otp": user_instance.otp}
            email_content = 'accounts/email.html'
            email_template = get_template(email_content).render(data_content)
            reciver_email = user_instance.email
            print(reciver_email)
            print(settings.EMAIL_HOST_USER)
            Subject = 'Need a password?'
            email_msg = EmailMessage(Subject, email_template, settings.EMAIL_HOST_USER, [reciver_email],
                                     reply_to=[settings.EMAIL_HOST_USER])
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)
            ################################################ EMAL SEND CODE END ##############
            messages.info(request, 'New verification has been sent to your email id.' + user_instance.email)

            return HttpResponseRedirect(reverse('accounts_app_link:verification_view_link'))
        else:
            messages.error(request, "This email not registered.")
            return HttpResponseRedirect(reverse('accounts_app_link:verification_view_link'))
