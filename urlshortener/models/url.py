from django.db import models


class URL(models.Model):
    long_text = models.CharField(max_length=1000, unique=True)
    hash = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f'https://tier.app/{self.hash}'
