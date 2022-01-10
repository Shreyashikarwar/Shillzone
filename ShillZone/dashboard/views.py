from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from .models import *
from accounts.forms import SignUpForm
from custom_user.models import User
from accounts.forms import PasswordForm


# Create your views here.
class DashboardView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/dashboard.html')


class AddUserView(generic.View):

    def get(self, request, *args, **kwargs):
        add_user_form = SignUpForm()
        return render(request, 'dashboard/add-user.html', {'add_user_form': add_user_form})

    def post(self, request):
        add_user_form = SignUpForm(request.POST)
        if add_user_form.is_valid():
            add_user_form.save()
            messages.success(request, 'User Registered Successfully')
            return render(request, 'dashboard/add-user.html')
        # user_name = request.POST['user_name']
        # email = request.POST['email']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # print(password2)
        #
        # if add_user_form.is_valid():
        #     try:
        #         if password1 == password2:
        #             add_user = User(user_name=user_name, email=email, password1=password1, password2=password2)
        #             add_user.save()
        #             print('Hello Peter')
        #             messages.success(request, 'User added.')
        #             return render(request, 'dashboard/manage-user.html')
        #     except:
        #         if password1 != password2:
        #             messages.error(request, "Password doesn't matches")
        #             return render(request, 'dashboard/manage-user.html')
        else:
            User.objects.all().filter(email=request.POST['email']).exists()
            print(request.POST['email'])
            messages.error(request, 'User already exists.')
            return render(request, 'dashboard/add-user.html')
        return HttpResponseRedirect(reverse('dashboard_app_link:add_user_view_link'))


class ManageUserView(generic.View):
    def get(self, request):
        manage_user = User.objects.all()
        return render(request, 'dashboard/manage-user.html', {'manage_user': manage_user})


class EditUser(generic.View):
    def get(self, request):
        user_instance = get_object_or_404(User, id=request.GET['user_id'])
        return render(request, 'dashboard/edit-user.html', {'user_instance': user_instance})

    def post(self, request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=request.GET['user_id']).exists():
            user_instance = get_object_or_404(User, email=request.GET['user_id'])
            print(user_instance)
            User.objects.filter(email=user_instance).update(password=password)
            User.objects.filter(email=user_instance).update(user_name=user_name, email=email)

            messages.success(request, 'User Edited Successfully!')
            return render(request, 'dashboard/manage-user.html')
        else:
            messages.error(request, 'Enter fields carefully')

        return HttpResponseRedirect(reverse('dashboard_app_link:manage_user_view_link'))

class DeleteUser(generic.View):
    def get(self, request):
        user_instance = get_object_or_404(User, id=request.GET['user_id'])
        return render(request, 'dashboard/delete-user.html', {'user_instance': user_instance})

    def post(self, request):
        user_instance = get_object_or_404(User, email=request.GET['user_id'])
        User.objects.filter(email=user_instance).delete()
        return HttpResponseRedirect(reverse('dashboard_app_link:delete_user_view_link'))

class ManageProfileView(generic.View):

    def get(self, request, *args, **kwargs):
        form = PasswordForm(request.GET)
        return render(request, 'dashboard/manage-profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user_name = request.POST['user_name']
        print(user_name)
        email = request.POST['email']
        print(email)
        full_name = request.POST['full_name']
        print(full_name)
        phone_no = request.POST['phone_no']
        print(phone_no)
        address = request.POST['address']
        print(address)

        if User.objects.filter(email=email, user_name=user_name).update(full_name=full_name, phone_no=phone_no,
                                                                        address=address):
            messages.success(request, "Your Profile Updated Successfully.")
            return render(request, 'dashboard/dashboard.html')
        else:
            messages.error(request, "Username or Email filled id not correct.")
        return HttpResponseRedirect(reverse('dashboard_app_link:manage_profile_view_link'))


class PasswordUpdateView(generic.View):

    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.user, request.POST)
        print(form)
        if form.is_valid():
            print('hiiii')
            user = form.save()
            print(user)
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password updated Successfully !')
            return render(request, 'dashboard/manage-profile.html')
        else:
            print('Hi')
            messages.error(request, 'Please enter authenticated Password')
        return HttpResponseRedirect(reverse('dashboard_app_link:manage_profile_view_link'))


class CreateView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/create.html')

    def post(self, request):
        page_name = request.POST['page_name']
        coin_name = request.POST['coin_name']
        coin_logo = request.POST['coin_logo']
        new_coin = CreateNewPage(page_name=page_name, coin_name=coin_name, coin_logo=coin_logo)
        new_coin.save()
        return render(request, 'dashboard/create.html')


class MyPagesView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/my-pages.html')

# class PromotionView(generic.View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'dashboard/promotion.html')
