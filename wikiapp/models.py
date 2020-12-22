from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=10, null=True)
    birth = models.CharField(max_length=10, null=True)
    enabled = models.BooleanField(default=True)

    def _str_(self):
        return self.name
