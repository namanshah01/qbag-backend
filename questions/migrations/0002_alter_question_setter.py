# Generated by Django 4.0.3 on 2022-03-23 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='setter',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
