from django.db import models
class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__ (self):
        return self.title
    
# Create your models here.
