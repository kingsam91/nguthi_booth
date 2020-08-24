from django.db import models

class Locatoin(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnself.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnself.name

class Image(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default=1)
    locatoin = models.ForeignKey(
        Locatoin, on_delete=models.SET_NULL, null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
