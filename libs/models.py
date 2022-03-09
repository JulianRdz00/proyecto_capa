from django.db import models
from django.utils import timezone


class CommonInfo(models.Model):
    fecha_de_creación = models.DateTimeField(auto_now_add=True, null=True)
    fecha_de_publicación = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
