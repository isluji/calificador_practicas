from django.conf.urls import url

from calif_practicas_app import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        # ... your url patterns
]
