# Generated by Django 4.2.1 on 2023-05-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parser', '0003_alter_info_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.CharField(default='New', max_length=25)),
            ],
            options={
                'verbose_name': 'Key',
                'verbose_name_plural': 'Keys',
            },
        ),
    ]
