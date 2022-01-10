from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import ContactUs
from django.template.loader import render_to_string, get_template
from django.conf import settings
import smtplib
import email.message
from django.contrib import messages


class ContactUsView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact/contactus.html')

    def post(self, request, *args, **kwargs):

        name = request.POST['name']
        user_email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        if len(phone) == 10 and len(comment) < 100:
        ############################################### EMAL SEND CODE START ##############
            data_content = {"name": name, "user_email": user_email, "comment": comment, "phone": phone,
                            "BASE_URL": settings.BASE_URL}
            email_content = render_to_string('email_templates/email_send_for_contact_us.html', data_content)
            msg = email.message.Message()
            msg['Subject'] = str(name)+ 'Wants to contact you.'

            msg['From'] = email.utils.formataddr((settings.SENDER_NAME, settings.DEFAULT_FROM_EMAIL))
            msg['To'] = settings.EMAIL_HOST_USER
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            s.sendmail(settings.DEFAULT_FROM_EMAIL, [msg['To']], msg.as_string())
        ############################################### EMAL SEND CODE END ##############
            contact = ContactUs(name=name, user_email=user_email, phone=phone, comment=comment)
            contact.save()
            messages.success(request, "Your Comment submitted Successfully")
            return render(request, 'contact/contactus.html')
        else:
            messages.error(request, "Send your comment properly")
            return render(request, 'contact/contactus.html')
######################################################################################################################
    # def post(self, request, *args, **kwargs):
    #     if 'name' and 'email' and 'message' in request.POST:
    #         name = request.POST['name']
    #         email = request.POST['email']
    #         phone = request.POST['phone']
    #         comment = request.POST['comment']
    #
    #         data_content = {"username": name,
    #                         "email": email,
    #                         "phone": phone,
    #                         "comment": comment}
    #         email_content = 'email_templates/email_send_for_contact_us.html'
    #
    #         email_template = get_template(email_content).render(data_content)
    #         # reciver_email = 'shiveshbhardwaj149@gmail.com'
    #
    #         Subject = "You've got a new user query"
    #
    #         if Email_Setting.objects.filter(status=True).exists():
    #             email_data = Email_Setting.objects.filter(status=True)
    #             for data in email_data:
    #                 EMAIL_HOST = data.smtp_host
    #                 EMAIL_PORT = data.smtp_port
    #                 EMAIL_HOST_USER = data.smtp_username
    #                 EMAIL_HOST_PASSWORD = data.smtp_password
    #         email_msg = EmailMessage(Subject, email_template, EMAIL_HOST_USER, [EMAIL_HOST_USER],
    #                                  reply_to=[EMAIL_HOST_USER])
    #         email_msg.content_subtype = 'html'
    #         email_msg.send(fail_silently=False)
    #         contactusdata = ContactUs(name=name, email=email, phone=phone, comment=comment)
    #         contactusdata.save()
    #         messages.success(request, 'Message successfully sent')
    #     else:
    #         messages.error(request, 'Something going wrong')
    #     return HttpResponseRedirect(reverse('contactus:Contact'))

    #########################################################################################################


