# Generated by Django 4.1.7 on 2023-03-24 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_choice_product_standart_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='standart_weight',
        ),
    ]
