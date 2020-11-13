from django.db import models

# Create your models here.
class SCB(models.Model):
    """
    Modelo que representa las SCBs posibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el modelo de la SCB")
    capacidad = models.IntegerField(help_text="Capacidad en Gbps/slot")
    precio = models.FloatField(help_text="Precio de la tarjeta SCB en Euros")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

class RE(models.Model):
    """
    Modelo que representa las RoutingEngine posibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el modelo de la RE")
    precio = models.FloatField(help_text="Precio de la RE en Euros")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

class Licencias(models.Model):
    """
    Modelo que representa las Licencias disponibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el nombre de la licencia")
    precio = models.FloatField(help_text="Precio de la licencia en Euros")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

class MPC(models.Model):
    """
    Modelo que representa las MPC posibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el modelo de la MPC")
    capacidad = models.IntegerField(help_text="Capacidad en Gbps")
    licencias = models.ManyToManyField(Licencias, help_text="Seleccione las posibles licencias", blank=True)
    mics = models.BooleanField(default=True, help_text="Acepta MICs")
    precio = models.FloatField(help_text="Precio de la tarjeta MPC en Euros")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

class MIC(models.Model):
    """
    Modelo que representa las MIC posibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el modelo de la MIC")
    zocalos = models.IntegerField (help_text="Numero de zocalos para opticas")
    precio = models.FloatField(help_text="Precio de la tarjeta MIC en Euros")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

class Optics(models.Model):
    """
    Modelo que representa las Opticas posibles en SB
    """
    modelo = models.CharField(max_length=20, help_text="Ingrese el modelo de la Optica")
    bandwidth = models.IntegerField(help_text="Ingrese el ancho de banda de la Optica en Gbps")
    precio = models.FloatField(help_text="Precio de la Optica")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.modelo

from django.db import connections

class showmpc(models.Model):
    mpc=models.CharField(max_length=100)

class showscb(models.Model):
    scb=models.CharField(max_length=100)

class showre(models.Model):
    re=models.CharField(max_length=100)

class showmic(models.Model):
    mic=models.CharField(max_length=100)

class showlicense(models.Model):
    mic=models.CharField(max_length=100)
