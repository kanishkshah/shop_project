# Generated by Django 2.1.7 on 2019-10-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20191013_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='Users.Product'),
        ),
    ]
