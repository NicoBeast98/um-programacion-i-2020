from django.conf.urls import url, include

# Cualquier peticion que se haga este proyecto, anda a tutorials.urls
urlpatterns = [
    url(r'^', include('tutorials.urls')),
]
