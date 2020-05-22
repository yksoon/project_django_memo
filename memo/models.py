from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    
    def update(self):
        self.update_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
    