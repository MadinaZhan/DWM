from django.db import models
class Mainapp(models.Model):
    title=models.CharField(max_length=100,verbose_name='dance')
    content=models.TextField(blank=True,verbose_name='content')
    photo=models.ImageField(upload_to='images/%Y/%m/%d/',verbose_name='image')
