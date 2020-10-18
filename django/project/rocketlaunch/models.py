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


class Status(models.Model):
    PARTIAL_FAILURE = 1
    SUCCESS = 2
    PRELAUNCH_FAILURE = 3
    FAILURE = 4

    status = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.status}"

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ["id"]


class Launch(models.Model):
    name = models.CharField(max_length=128)
    cost = models.IntegerField(null=True)
    time_date = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Launches"
        ordering = ["id"]
