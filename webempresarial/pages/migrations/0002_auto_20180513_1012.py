# Generated by Django 2.0.2 on 2018-05-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['orden', 'title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'Las Paginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='orden',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]