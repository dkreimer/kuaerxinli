# Generated by Django 2.1 on 2018-08-16 08:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180816_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(blank=True, to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]