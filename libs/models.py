from django.db import models


class CommonInfo(models.Model):
    fecha_de_creación = models.DateTimeField(default=timezone.now)
    fecha_de_publicación = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BoleanField(default=False)


    class Meta:
        abstract = True
