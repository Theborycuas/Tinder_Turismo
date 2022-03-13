from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=25, verbose_name = "Nombre de la Etiqueta")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de Creación")
    update = models.DateTimeField(auto_now = True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = "etiqueta"
        verbose_name_plural = "etiquetas"

    def __str__(self):
        return self.tag_name