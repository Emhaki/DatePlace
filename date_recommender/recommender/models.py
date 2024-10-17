from django.db import models
from accounts.models import KakaoUser
from django.contrib.auth.models import User

# Create your models here.

class DatePlace(models.Model):
    CATEGORY_CHOICES = [
        ('restaurant', '식당'),
        ('cafe', '카페'),
        ('park', '공원'),
        ('movie', '영화관'),
        ('activity', '액티비티'),
        ('other', '기타'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=500)
    description = models.TextField()
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='date_places/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(KakaoUser, on_delete=models.CASCADE)
    date_place = models.ForeignKey(DatePlace, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s review for {self.date_place.name}"

class DateCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class DateCoursePlace(models.Model):
    date_course = models.ForeignKey(DateCourse, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    visit_time = models.TimeField()
    order = models.IntegerField()
    cost = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']
