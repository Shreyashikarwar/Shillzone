# Import Python Package Start
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy
from .models import User


# Import Developer Package Start
# Register User model created by developer
#  Function for Display Model into superuser page
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password','full_name', 'phone_no', 'address')}),
        (ugettext_lazy('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
                                                   'otp')}),
        (ugettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined', 'update_dt')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff')  # display field for admin
    search_fields = ('email',)  # search field for admin
    ordering = ('date_joined',)  # table order order admin
