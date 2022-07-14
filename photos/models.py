from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name_en = models.CharField(max_length=100, null=False, blank=False)
    name_ru = models.CharField(max_length=100, null=False, blank=False)

    # def set_attributes_from_name(self, name):
    #     self.name_en = name
    #
    #     models.TextField.set_attributes_from_name()

    def __str__(self):
        return self.name_en


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image_url = models.TextField(null=False, blank=False)
    description_en = models.TextField(null=False, blank=True)
    description_ru = models.TextField(null=False, blank=True)

    camera_name = models.CharField(max_length=100, null=False, blank=True)
    aperture = models.CharField(max_length=10, null=False, blank=True)
    shutter_speed = models.CharField(max_length=10, null=False, blank=True)
    focal_length = models.CharField(max_length=10, null=False, blank=True)

    def __str__(self):
        return self.description_en
