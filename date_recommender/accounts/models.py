from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class KakaoUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='kakao_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='kakao_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    kakao_id = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100)
    profile_image = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username
