# Generated by Django 5.0.2 on 2024-04-05 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_formulario_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulario',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]
