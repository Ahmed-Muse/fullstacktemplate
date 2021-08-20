
from django.contrib import admin
from django.urls import path, include#this for the urls to work

#start of media image libraries
from django.conf.urls.static import static#this is for the images urls and pth
from django.conf import settings #will enable you to access MEDIA_URL in settings.py #this is also for the images urls and path
#end of media images libraries


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('allifmaalwebapp.urls')), #to point the root URLconf at the polls.urls module
    #path('customers/',include('allifmaalwebapp.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

