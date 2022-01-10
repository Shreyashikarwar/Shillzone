# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from custom_user.models import User
#
# class ContactForm(UserCreationForm):
#
#     name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Name"}))
#     phone_number = forms.IntegerField(label="Phone number", help_text='Email.',widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Phone number"}))
#     email = forms.EmailField(label="Email", max_length=254, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Email"}))
#     comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Comment"}))
#
#     class Meta:
#         model = User
#         fields = ('name', 'phone_number', 'email', 'comment')