
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "ROSHAN ICE CREAM"
admin.site.site_title = "ROSHAN ICE CREAM Admin Portal"
admin.site.index_title = "Welcome to Roshan ice cream"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
