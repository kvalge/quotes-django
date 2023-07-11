from django.db import models

class Quote(models.Model):
    author = models.CharField(max_length=250, unique=False)
    quote = models.CharField(max_length=4500, unique=False)
    years = models.CharField(max_length=250, unique=False)
    area = models.CharField(max_length=150, unique=False)
    image = models.CharField(max_length=5000, unique=False)

    def __str__(self):
        return self.author
