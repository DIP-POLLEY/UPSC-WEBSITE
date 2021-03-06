# Generated by Django 3.0.3 on 2020-11-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practice1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='picUploads')),
                ('chk1', models.BooleanField(default=False)),
                ('pdf', models.FileField(upload_to='pdfUploads')),
                ('chk2', models.BooleanField(default=False)),
            ],
        ),
    ]
