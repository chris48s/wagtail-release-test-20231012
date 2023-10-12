from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(packages=["wagtail_release_test_20231012"]),
            name="javascript_catalog",
        ),
        # Add your other URLs here, and they will appear under `/admin/release_test_20231012/`
        # Note: you do not need to check for authentication in views added here, Wagtail does this for you!
    ]

    return [
        path(
            "release_test_20231012/",
            include(
                (urls, "wagtail_release_test_20231012"),
                namespace="wagtail_release_test_20231012",
            ),
        )
    ]
