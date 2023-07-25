# Generated by Django 3.2.3 on 2023-07-25 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField(error_messages={'validators': 'Введите число от 0 до 10000'}, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='IngredientSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, verbose_name='Название')),
                ('measurement_unit', models.CharField(max_length=16, verbose_name='Размерность')),
            ],
            options={
                'verbose_name': 'Свойства ингредиента',
                'verbose_name_plural': 'Свойства ингредиентов',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('text', models.TextField(max_length=1024, verbose_name='Описание')),
                ('cooking_time', models.SmallIntegerField(error_messages={'validators': 'Введите число от 1 до 300'}, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='recipes/images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='Название')),
                ('color', models.CharField(max_length=16, verbose_name='Цвет')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='TagRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Теги рецепта',
                'verbose_name_plural': 'Теги рецептов',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='UserFavoritedRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Любимый рецепт',
                'verbose_name_plural': 'Любимые рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='UserShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Рецепт в корзине',
                'verbose_name_plural': 'Корзины',
                'ordering': ('-id',),
            },
        ),
    ]
