# Generated by Django 4.2.16 on 2024-11-28 20:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0003_recipeingredient_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('conversion_to_grams', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, 'Conversion rate must be positive.')])),
            ],
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='unit',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='cooked_weight',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.1, message='Cooked weight must be a positive number.')]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='cooking_time',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, message='Cooking time cannot be negative.')]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='cost',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, message='Cost must be a positive number.')]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Name should be a string value.', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='raw_weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, message='Raw weight must be a positive number.')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe_catalog.RecipeIngredient', to='recipe_catalog.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(message='Title should be a string value.', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.FloatField(help_text='Количество ингредиента в рецепте.', validators=[django.core.validators.MinValueValidator(0.1, 'Quantity must be positive.')]),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe_catalog.unit'),
        ),
    ]