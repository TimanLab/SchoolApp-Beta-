# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _


class Exclusion(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    reason = models.TextField()


class BusMileage(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE)
    initial_mileage = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed


class Parent(models.Model):
    name = models.CharField(max_length=100)
    bus = models.CharField(max_length=100)
    # Add other fields as needed


class Operator(models.Model):
    name = models.CharField(max_length=100)
    bus = models.CharField(max_length=100)
    # Add other fields as needed


class Bus(models.Model):
    number = models.CharField(max_length=20)
    # Add other fields as needed


class BusTrack(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # Add other fields as needed


class Feedback(models.Model):
    message = models.TextField()
    # Add other fields as needed


class PopRegister(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    operator = models.ForeignKey('Operator', on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    timestamp = models.DateTimeField(auto_now_add=True)


class Child(models.Model):
    name = models.CharField(max_length=100)
    ucs_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)


class BusStop(models.Model):
    bus_stage_name = models.CharField(max_length=100)
    pick_drop_time = models.TimeField()


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        # Your existing implementation
        pass

    def create_superuser(self, email, password=None):
        # Your existing implementation
        pass

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add more fields as needed...

    # Relationships
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='bustrack_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='bustrack_user_permissions',
        related_query_name='user',
    )

    # Custom methods
    def has_permission(self, permission_name):
        """
        Check if the user has a specific permission.

        Args:
            permission_name (str): The name of the permission.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        return self.user_permissions.filter(name=permission_name).exists()

    def has_group(self, group_name):
        """
        Check if the user belongs to a specific group.

        Args:
            group_name (str): The name of the group.

        Returns:
            bool: True if the user belongs to the group, False otherwise.
        """
        return self.groups.filter(name=group_name).exists()

    # Add more custom methods...
