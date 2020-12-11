from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from installations.api.views import CreateUpdateInstallationView, ListRetrieveInstallationView

router = routers.DefaultRouter()
router.register(r'installations', ListRetrieveInstallationView)

urlpatterns = [
    path('', include(router.urls)),
    path('create/installation/', CreateUpdateInstallationView.as_view()),
    path('admin/', admin.site.urls),
]
