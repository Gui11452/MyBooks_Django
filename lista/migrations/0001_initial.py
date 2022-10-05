# Generated by Django 4.1 on 2022-09-29 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_livro', models.CharField(max_length=255)),
                ('avaliacao', models.IntegerField(blank=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('resenha', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lista.usuario')),
            ],
        ),
    ]