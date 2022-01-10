
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import generic
from .models import AdvertiseWithUs
from django.conf import settings
import smtplib
import email.message
from django.contrib import messages


class AdvertiseView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'advertise/advertise.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            banner = request.POST['banner']
            redirection_link = request.POST['redirection_link']

            if len(phone_number) == 10:
                ############################################### EMAL SEND CODE START ##############
                data_content = {"name": name, "email": email, "phone_number": phone_number,
                                "banner": banner, "redirection_link": redirection_link, "BASE_URL": settings.BASE_URL}
                email_content = render_to_string('email_templates/email_send_for_advertise_us.html', data_content)
                msg = email.message.Message()
                msg['Subject'] = str(name) + 'Wants to advertise with you.'

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
                advertise = AdvertiseWithUs(name=name, email=email, phone_number=phone_number,
                                            banner=banner, redirection_link=redirection_link)
                advertise.save()
                messages.success(request, "Your Comment submitted Successfully")
                return render(request, 'contact/contactus.html')
            else:
                messages.error(request, "Send your comment properly")
                return render(request, 'contact/contactus.html')

        #     ################################################ EMAL SEND CODE START ##############
        #     data_content = {"name": name, "email": email, "banner": banner, "phone_number": phone_number,
        #                     "redirection_link": redirection_link, "BASE_URL": settings.BASE_URL}
        #     email_content = render_to_string('email_templates/email_send_for_contact_us.html', data_content)
        #     msg = name.message.Message()
        #     msg['Subject'] = str(name) + " want's to advertise with you. "
        #     msg['From'] = settings.EMAIL_HOST_USER
        #     password = settings.EMAIL_HOST_PASSWORD
        #     msg.add_header('Content-Type', 'text/html')
        #     msg.set_payload(email_content)
        #     send = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        #     send.starttls()
        #     send.login(msg['From'], password)
        #     send.sendmail(msg['From'], [msg['To']], msg.as_string())
        #     ################################################ EMAIL SEND CODE END ##############
        #     if len(request.FILES) != 0:
        #         banner_img = request.FILES['img_logo']
        #         advertise = AdvertiseWithUs(name=name, phone_number=phone_number, email=email, banner=banner,
        #                                     banner_img=banner_img, redirection_link=redirection_link)
        #         advertise.save()
        #         messages.success(request, "Query related to advertisement submitted successfully")
        #     return redirect('/')
        #
        # return render(request, 'advertise/advertise.html')
