# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cancha(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estadocancha = models.ForeignKey('Estadocancha', models.DO_NOTHING, db_column='estadocancha', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancha'

    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    numerotelefono = models.BigIntegerField(blank=True, null=True)
    estadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='estadocliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido


class Estadocancha(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocancha'

    def __str__(self) -> str:
        return self.nombre


class Estadocliente(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocliente'

    def __str__(self) -> str:
        return self.nombre


class Horario(models.Model):
    horainicio = models.TimeField(blank=True, null=True)
    horafin = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


    def __str__(self) -> str:
        return str(self.horainicio) + ' - ' + str(self.horafin)


class Turno(models.Model):
    fecha = models.DateField(blank=True, null=True)
    cancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='cancha', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente', blank=True, null=True)
    horario = models.ForeignKey(Horario, models.DO_NOTHING, db_column='horario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno'

    def __str__(self) -> str:
        return str(self.fecha) + ' / ' + self.horario.__str__()
