# Generated by Django 2.1.7 on 2019-10-02 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('descrip', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('slug', models.SlugField(max_length=30)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]