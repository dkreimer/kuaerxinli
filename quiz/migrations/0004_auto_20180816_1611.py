# Generated by Django 2.1 on 2018-08-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20180816_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(blank=True, null=True, to='quiz.Question'),
        ),
    ]