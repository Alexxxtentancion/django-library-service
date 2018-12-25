# Generated by Django 2.1.4 on 2018-12-25 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_book_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.ManyToManyField(blank=True, related_name='book_got', to=settings.AUTH_USER_MODEL),
        ),
    ]