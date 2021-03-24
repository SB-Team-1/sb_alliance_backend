from django.db import models
from api.models import User
from django.contrib.auth import get_user_model


class Business(models.Model):
    # choices for the category
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100,required=True)

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
        required=True
    )

    description = models.TextField(max_length=750)
    website = models.URLField(max_length=200)
    favorite = models.BooleanField()
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

class Alliance(models.Model):
    user = models.ManyToManyField(User, on_delete=models.CASCADE, primary_key=True)
    business = models.ManyToManyField(Business, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100,required=True)
    location = models.CharField(max_length=100, required=True)
    description = models.TextField(max_length=750, required=True)

class Perks(models.Model):
    alliance = models.ForeignKey(Alliance, related_name='perks', on_delete=models.CASCADE)
    discounts = models.TextField(max_length=750,required=True)