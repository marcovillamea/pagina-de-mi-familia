from django.db import models



class familia(models.Model):
    name = models.CharField(max_length=20)
    tipo_de_familia = models.CharField(max_length=20)
    age = models.FloatField()

    def __str__(self):
        return self.name

