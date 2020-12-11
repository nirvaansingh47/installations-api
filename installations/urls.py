from django.contrib import admin
from django.urls import path

from installations.api.views import CreateUpdateInstallationView

urlpatterns = [
    path('create/installation/', CreateUpdateInstallationView.as_view()),
    path('admin/', admin.site.urls),
]
