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
        '''generated short url'''
        return f'{BASE_URL}{self.hash}'

    @property
    def visits_count(self):
        '''received SHORTEN requests count'''
        return self.visits.count()

    def set_hash(self):
        '''generate a unique Base64 hash'''
        hash = secrets.token_urlsafe(HASH_NBYTES)
        if not URL.objects.filter(hash=hash).exists():
            self.hash = hash
            return
        self.set_hash()

    def visit(self):
        '''add a visit'''
        visit = Visit(url=self)
        visit.save()


def post_save_url(sender, instance, created, ** kwargs):
    '''generate a hash right after CREATING a url'''
    if created:
        instance.set_hash()
        instance.save()


post_save.connect(post_save_url, URL)
