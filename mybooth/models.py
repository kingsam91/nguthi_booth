from django.db import models

class locatoin(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnself.name