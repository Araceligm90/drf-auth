from django.db import models
from django.contrib.auth import get_user_model


class City(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=250, default="no description provided")

    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

