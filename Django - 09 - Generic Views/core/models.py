from tabnanny import verbose
from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-post_date']
        
    def __str__(self):
      return f'{self.title}'
  
  