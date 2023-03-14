# Generated by Django 4.1.7 on 2023-03-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('inputEmail4', models.CharField(max_length=120)),
                ('floatingTextarea', models.TextField()),
            ],
        ),
    ]
