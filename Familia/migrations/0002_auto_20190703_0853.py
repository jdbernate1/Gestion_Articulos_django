# Generated by Django 2.2.2 on 2019-07-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='id',
        ),
        migrations.AddField(
            model_name='familia',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='codigo',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
