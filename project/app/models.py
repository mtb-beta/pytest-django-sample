from django.db import models

class MyAppModel(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255, default="")

    @property
    def is_empty(self):
        return bool(self.content)
