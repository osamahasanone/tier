from django.db import models


class Visit(models.Model):
    url = models.ForeignKey(
        'URL', on_delete=models.CASCADE, related_name='visits')
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url}:{self.requested_at}'
