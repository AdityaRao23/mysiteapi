# Generated by Django 3.2.5 on 2021-09-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('Description', models.CharField(max_length=120)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
