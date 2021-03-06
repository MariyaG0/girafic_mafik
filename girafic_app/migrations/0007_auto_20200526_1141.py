# Generated by Django 3.0.6 on 2020-05-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girafic_app', '0006_auto_20200522_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='Фамилия, Имя, Очество')),
                ('post_address', models.CharField(max_length=200, verbose_name='Адрес доставки')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
