from django.db import models


class ModelA(models.Model):
    name = models.CharField(max_length=1024)

    class Meta:
        ordering = (models.functions.Lower('name'), )


class ModelB(models.Model):
    name = models.CharField(max_length=1024)  # this masks the FieldError
    ref = models.ForeignKey(ModelA, on_delete=models.CASCADE)
