# Generated by Django 2.1.7 on 2019-10-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]