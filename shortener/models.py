from hashlib import md5
from django.db import models
from datetime import datetime


class VisitorUrl(models.Model):
    unique_visitor = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    origin_url = models.URLField(verbose_name='origin_url')
    url_hash = models.CharField(max_length=6)

    class Meta:
        verbose_name = 'Visitor link'
        verbose_name_plural = 'Visitor links'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url_hash = md5(self.origin_url.encode()).hexdigest()[:6]
        super().save(*args, **kwargs)
