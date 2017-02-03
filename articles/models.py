from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as tz

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category
        

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name = 'articles')
    published = models.DateTimeField(default  = tz.now)
    body = models.TextField()
    hero_image = models.FileField(max_length=500, upload_to="images")
    extra_image = models.FileField(max_length=500, null=True, blank=True, upload_to="images")
    
    def author_full_name(self):
        return " ".join([self.author.first_name, self.author.last_name])
    
    def __str__(self):
        title = self.title[:50]
        if len(self.title)> 50:
            title += "..."
        return title
    
    
