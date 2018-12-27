# Generated by Django 2.1.4 on 2018-12-27 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, default='/static/images/default.jpg', upload_to='photo/%Y', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='book_liked', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]