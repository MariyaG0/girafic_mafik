# Generated by Django 3.0.5 on 2020-05-17 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girafic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'ordering': ['name'], 'verbose_name': 'Коробка', 'verbose_name_plural': 'Коробки'},
        ),
    ]
