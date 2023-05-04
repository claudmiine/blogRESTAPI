from django.db import models

# Create your models here.
class Article(models.Model):
    CATEGORIES = (
        ('1', 'Eco'),
        ('2', 'Sustainability'),
    )
    category = models.CharField(max_length=250, choices=CATEGORIES)
    title = models.CharField(max_length=250)
    img_name = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.title