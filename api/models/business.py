from django.db import models
from api.models import User
from django.contrib.auth import get_user_model
from django.conf import settings


class Business(models.Model):
    # choices for the category
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    CATEGORY_CHOICES = [
    ("1", "Electronics"),
    ("2", "Auto"),
    ("3", "Food/Beverage"),
    ("4", "Health/Fitness"),
    ("5", "Apparel"),
    ("6", "Furniture"),
    ("7", "Sporting goods"),
    ("8", "Home Improvement"),
    ("9", "Misc")
    ]
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField(max_length=750)
    website = models.URLField(max_length=200)
    favorite = models.BooleanField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class Alliance(models.Model):
    user = models.ManyToManyField(User)
    business = models.ManyToManyField(Business)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=750)

class Perks(models.Model):
    alliance = models.ForeignKey(Alliance, related_name='perks', on_delete=models.CASCADE)
    discounts = models.TextField(max_length=750)