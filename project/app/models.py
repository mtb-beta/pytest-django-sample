from django.db import models

class MyAppModel(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255)

