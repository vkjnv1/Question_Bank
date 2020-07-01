# Generated by Django 3.0.6 on 2020-06-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='generator/images')),
            ],
        ),
    ]
