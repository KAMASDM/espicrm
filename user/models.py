
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    created_by = models.ForeignKey('self', on_delete=models.CASCADE)