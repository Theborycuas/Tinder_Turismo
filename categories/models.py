from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=25, verbose_name="Nombre de Categoría")
    category_state = models.BooleanField(default=False, verbose_name="Estado de la Categoría")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["order", "category_name"]

    def __str__(self):
        return self.category_name