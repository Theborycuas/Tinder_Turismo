from django.db import models
from ciudades.models import City

class UserApp(models.Model):
    user_name = models.CharField("Nombres", max_length=200, blank = True, null = True)
    user_lastname = models.CharField("Apellidos", max_length=200, blank = True, null = True)
    username = models.CharField("Nombre de usuario", unique = True, max_length=100, blank = False, null = False)
    user_password = models.CharField("Contraseña", max_length=100, blank = False, null = False)
    user_email = models.EmailField("Correo Electrónico", unique = True, max_length=254, blank = False, null = False)    
    user_phone = models.CharField("Teléfono", max_length=200, blank = True, null = True)
    user_photo = models.ImageField("Imagen de perfil", upload_to='photo/', max_length=200, null = True, blank = True)
    user_birthdate = models.DateField("Fecha de nacimiento", blank = True, null = True)    
    city_id = models.ForeignKey(City, on_delete = models.CASCADE, null = False, blank = False, verbose_name="Ciudad")
    user_gender = models.CharField("Género", max_length=200, blank = True, null = True)    
    user_state = models.BooleanField(default = True, blank = True, null = True)    
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edición")


    class Meta:
        verbose_name = "Usuario App"
        verbose_name_plural = "Usuarios App"

    def __str__(self):
        return self.username