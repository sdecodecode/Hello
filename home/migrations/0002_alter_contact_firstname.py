# Generated by Django 4.1.7 on 2023-03-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='firstName',
            field=models.CharField(max_length=60, null=True),
        ),
    ]