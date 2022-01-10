"""ShillZone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('home.urls', 'home'), namespace='home_app_link')),
    path('account/', include(('accounts.urls', 'accounts'), namespace='accounts_app_link')),
    path('about/', include(('about_us.urls', 'about'), namespace='about_app_link')),
    path('feed/', include(('feed.urls', 'feed'), namespace='feed_app_link')),
    path('forum/', include(('forum.urls', 'forum'), namespace='forum_app_link')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard_app_link')),
    path('advertise_us/', include(('advertise.urls', 'advertise'), namespace='advertise_app_link')),
    path('our_policy/', include(('policy.urls', 'policy'), namespace='policy_app_link')),
    path('contact-us/', include(('contact.urls', 'contact'), namespace='contact_app_link')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)