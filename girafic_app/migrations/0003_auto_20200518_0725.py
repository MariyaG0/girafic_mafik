# Generated by Django 3.0.5 on 2020-05-18 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girafic_app', '0002_auto_20200517_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name': 'Коробка', 'verbose_name_plural': 'Коробки'},
        ),
        migrations.AlterModelOptions(
            name='boxorder',
            options={'verbose_name': 'Заказ коробок'},
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталоги'},
        ),
        migrations.AlterModelOptions(
            name='dreamcatcher',
            options={'verbose_name': 'Ловец снов', 'verbose_name_plural': 'Ловцы снов'},
        ),
        migrations.AlterModelOptions(
            name='dreamcatcherorder',
            options={'verbose_name': 'Заказ ловцов снов'},
        ),
        migrations.AlterModelOptions(
            name='letter',
            options={'verbose_name': 'Конверт', 'verbose_name_plural': 'Конверты'},
        ),
        migrations.AlterModelOptions(
            name='letterorder',
            options={'verbose_name': 'Заказ письма'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
