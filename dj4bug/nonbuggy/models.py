from django.db import models


class ModelA(models.Model):
    name = models.CharField(max_length=1024)

    class Meta:
        ordering = ('name', )


class ModelB(models.Model):
    ref = models.ForeignKey(ModelA, on_delete=models.CASCADE)
