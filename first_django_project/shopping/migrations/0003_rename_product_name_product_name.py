# Generated by Django 5.2 on 2025-04-06 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
