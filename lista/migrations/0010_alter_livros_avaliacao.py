# Generated by Django 4.1 on 2022-09-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0009_alter_livros_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='avaliacao',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
    ]
