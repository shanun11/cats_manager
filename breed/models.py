from django.db import models

# Create your models here.


class Breed(models.Model):
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

