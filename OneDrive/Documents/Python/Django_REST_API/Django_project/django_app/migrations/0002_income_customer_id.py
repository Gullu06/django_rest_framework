# Generated by Django 4.2.2 on 2023-12-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='customer_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
