from django.db import models
from dev.utils.base import BaseModel

class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='contact_images/', null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')  

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
