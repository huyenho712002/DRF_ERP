import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.role_name


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.permission_name


class Entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.entity_name


class RolePermission(models.Model):
    
    role = models.ForeignKey(Role, related_name='role_permissions', on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, related_name='role_permissions', on_delete=models.CASCADE)

    # Specific permissions
    view = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    full_access = models.BooleanField(default=False)

    class Meta:
        unique_together = ('role', 'entity')


# User model
class Users(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    tels = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.ForeignKey(Role, related_name='users', on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email


