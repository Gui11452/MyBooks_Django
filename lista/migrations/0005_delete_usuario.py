# Generated by Django 4.1 on 2022-09-30 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_alter_livros_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
