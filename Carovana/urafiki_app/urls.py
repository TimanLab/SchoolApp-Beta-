# urafiki_app/urls.py

from django.contrib import admin
from django.urls import path, include
from bustrack.views import login  # Imports the login view from bustrack app

urlpatterns = [
    path('', login, name='login'),  # Empty path will redirect to the login view in bustrack app
    path('admin/', admin.site.urls),
    path('bustrack/', include('bustrack.urls')),
]

