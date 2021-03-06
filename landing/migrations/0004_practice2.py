# Generated by Django 3.0.3 on 2020-11-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20201128_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practice2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=250)),
                ('File', models.FileField(upload_to='media')),
                ('check_if_image', models.BooleanField(default=False)),
                ('check_if_pdf', models.BooleanField(default=False)),
            ],
        ),
    ]
