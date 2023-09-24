from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from .views import TestPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cookies/", include("cookie_consent.urls")),
    path("", TestPageView.as_view(), name="test_page"),
    path(
        "legacy/",
        TestPageView.as_view(template_name="legacy_test_page.html"),
        name="legacy_test_page",
    ),
]

urlpatterns += staticfiles_urlpatterns()
