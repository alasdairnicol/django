from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include([
        # include a pattern that should trigger warning to test that
        # we check the resolver recursively
        url(r'^include-with-dollar$', include([])),
    ])),
]
