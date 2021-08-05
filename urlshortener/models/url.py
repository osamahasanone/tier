import secrets
from django.db import models
from django.db.utils import IntegrityError
from . import Visit
from ..constants import HASH_NBYTES
from ..constants import BASE_URL


class URL(models.Model):
    long_text = models.URLField(max_length=1000, unique=True)
    hash = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.short_text

    @property
    def short_text(self):
        return f'{BASE_URL}{self.hash}'

    def _set_hash(self):
        hash = secrets.token_urlsafe(HASH_NBYTES)
        if not URL.objects.filter(hash=hash).exists():
            self.hash = hash
            return
        self.generate_hash()

    def visit(self):
        visit = Visit(url=self)
        visit.save()

    def save(self, *args, **kwargs):
        self._set_hash()
        super(URL, self).save(*args, **kwargs)
