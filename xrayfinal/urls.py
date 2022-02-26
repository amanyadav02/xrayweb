
from django.contrib import admin
from django.urls import path,include
admin.site.site_header="Covid Detector"
admin.site.site_title="Covid Detector Database"
admin.site.index_title="Covid detector contacts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('xray.urls'))
]
