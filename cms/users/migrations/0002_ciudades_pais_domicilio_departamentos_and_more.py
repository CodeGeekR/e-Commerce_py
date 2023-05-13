# Generated by Django 4.2.1 on 2023-05-12 14:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCiudad', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePais', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=50)),
                ('id_status', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ciudades')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreDepartamento', models.CharField(max_length=50)),
                ('indicativo', models.IntegerField(default=0)),
                ('id_status', models.BooleanField(default=True)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.pais')),
            ],
        ),
        migrations.AddField(
            model_name='ciudades',
            name='id_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.departamentos'),
        ),
    ]
