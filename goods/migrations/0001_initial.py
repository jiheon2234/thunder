# Generated by Django 4.0.6 on 2022-08-01 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import goods.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('is_new', models.BooleanField()),
                ('can_change', models.BooleanField()),
                ('where', models.TextField()),
                ('image', goods.fields.ThumbnailImageField(upload_to='goods/%Y/%m', verbose_name='IMAGE')),
                ('price', models.PositiveIntegerField()),
                ('already_sell', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]