from typing import Iterable
from django.db import models
from django. contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    created = models.DateTimeField(
        auto_now=False, auto_now_add=False
        )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural ="Categories"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"category for {self.name}"    



class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ForeignKey(
        "project.Category",
        verbose_name=("Product Categories"),
         on_delete=models.CASCADE, null=True, blank=True
    )

    User = models.ForeignKey(User, verbose_name=_("User"), null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=39, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)