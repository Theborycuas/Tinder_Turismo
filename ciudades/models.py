from django.db import models
from provinces.models import Province

class City(models.Model):
    city_name = models.CharField(max_length=25, verbose_name="Nombre de la Ciudad")
    city_state = models.BooleanField(default=False, verbose_name="Estado de la Ciudad")
    province_id = models.ForeignKey(Province, on_delete = models.CASCADE, null = False, blank = False, verbose_name="Provincia")
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"

    def __str__(self):
        return self.city_name