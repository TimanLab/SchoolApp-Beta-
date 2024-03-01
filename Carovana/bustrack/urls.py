from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import send_feedback
from .views import bus_tracking
from .views import operator_dashboard, add_child, add_bus_stop, pop_register
from .views import admin_landing
from .views import add_remove_parent
from .views import feedback_inbox
from .views import bus_mileage
from .views import register_management, exclusion_management, add_operator
from .views import login, custom_logout, admin_dashboard, parent_dashboard

app_name = 'bustrack'

urlpatterns = [
    path('', login, name='login'),
    path('custom_logout', custom_logout, name='custom_logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('operator_dashboard/', operator_dashboard, name='operator_dashboard'),
    path('parent_dashboard/', parent_dashboard, name='parent_dashboard'),
    path('register_management/', register_management, name='register_management'),
    path('exclusion_management/', exclusion_management, name='exclusion_management'),
    path('bus_mileage/', bus_mileage, name='bus_mileage'),
    path('feedback_inbox/', feedback_inbox, name='feedback_inbox'),
    path('add_remove_parent/', add_remove_parent, name='add_remove_parent'),
    path('admin_landing/', admin_landing, name='admin_landing'),
    path('operator_dashboard/', operator_dashboard, name='operator_dashboard'),
    path('add_child/', add_child, name='add_child'),
    path('add_operator/', add_operator, name='add_operator'),
    path('add_bus_stop/', add_bus_stop, name='add_bus_stop'),
    path('pop_register/', pop_register, name='pop_register'),
    path('bus_tracking/', bus_tracking, name='bus_tracking'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('send_feedback/', send_feedback, name='send_feedback'),
    # Add other URL patterns for different views
]
