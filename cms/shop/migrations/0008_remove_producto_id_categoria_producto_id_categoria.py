# Generated by Django 4.2.1 on 2023-06-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='id_categoria',
            field=models.ManyToManyField(to='shop.categoria'),
        ),
    ]
