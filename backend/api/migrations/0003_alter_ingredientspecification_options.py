# Generated by Django 3.2.3 on 2023-07-25 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientspecification',
            options={'ordering': ('name',), 'verbose_name': 'Свойства ингредиента', 'verbose_name_plural': 'Свойства ингредиентов'},
        ),
    ]