from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

url(r'^$',views.home,name='home'),
url(r'^event$',views.event,name='event'),
url(r'^projects$',views.project,name='project'),
url(r'^plans$',views.future_plan,name='plan'),
url(r'^news$',views.news,name='news'),
url(r'^bursaries$',views.bursary,name='bursary'),
url(r'^contact$',views.contact,name='contact'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)