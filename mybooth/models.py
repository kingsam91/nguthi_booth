from django.db import models

class Locatoin(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnself.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        returnself.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default=1)
    locatoin = models.ForeignKey(
        Locatoin, on_delete=models.SET_NULL, null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_images(cls):
        images = cls.objects.filter()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images