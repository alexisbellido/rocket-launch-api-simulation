# Generated by Django 3.1.2 on 2020-10-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocketlaunch', '0002_auto_20201017_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
