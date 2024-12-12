# Generated by Django 4.2.16 on 2024-11-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0005_remove_unit_conversion_to_grams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='default_cooked_weight',
            field=models.FloatField(blank=True, help_text='Дефолтный вес приготовленного продукта для данной единицы измерения', null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='default_raw_weight',
            field=models.FloatField(blank=True, help_text='Дефолтный вес сырого продукта для данной единицы измерения', null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='raw_weight',
            field=models.FloatField(blank=True, help_text='Вес сырого ингредиента в граммах', null=True),
        ),
    ]