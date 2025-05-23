from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name',max_length=50, )
    anons = models.CharField('Anons',max_length=256, )
    full_text = models.TextField('Text')
    date = models.DateTimeField('date of publication')

    """def __str__(self):
        return self.title"""
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    




