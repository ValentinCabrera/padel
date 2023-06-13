# Generated by Django 4.1.2 on 2023-06-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cancha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "cancha",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                ("apellido", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.CharField(blank=True, max_length=50, null=True)),
                ("numerotelefono", models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "cliente",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Estadocancha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "estadocancha",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Estadocliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "estadocliente",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Horario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("horainicio", models.TimeField(blank=True, null=True)),
                ("horafin", models.TimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "horario",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Turno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": "turno",
                "managed": False,
            },
        ),
    ]