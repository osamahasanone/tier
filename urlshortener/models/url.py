import secrets
from django.db import models
from . import Visit
from ..constants import BASE_URL, HASH_NBYTES
from django.db.models.signals import post_save


class URL(models.Model):
    long_text = models.URLField(max_length=1000)
    hash = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.short_text

    @property
    def short_text(self):
        return f'{BASE_URL}{self.hash}'

    @property
    def visits_count(self):
        return self.visits.count()

    def set_hash(self):
        hash = secrets.token_urlsafe(HASH_NBYTES)
        if not URL.objects.filter(hash=hash).exists():
            self.hash = hash
            return
        self.set_hash()

    def visit(self):
        visit = Visit(url=self)
        visit.save()


def post_save_url(sender, instance, created, ** kwargs):
    if created:
        instance.set_hash()
        instance.save()


post_save.connect(post_save_url, URL)
