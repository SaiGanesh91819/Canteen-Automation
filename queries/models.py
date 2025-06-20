from django.db import models

# Create your models here.
class Query(models.Model):
    username = models.TextField(max_length=30,default=None , null=True)
    topic = models.TextField(max_length=300)
    description = models.TextField(max_length = 600)
