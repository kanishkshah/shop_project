# Generated by Django 2.1.7 on 2019-10-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]