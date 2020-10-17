from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ["id"]


class Location(models.Model):
    location = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.location}"

    class Meta:
        ordering = ["id"]
