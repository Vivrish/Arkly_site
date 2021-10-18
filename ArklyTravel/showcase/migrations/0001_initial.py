# Generated by Django 3.2.8 on 2021-10-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='C:/Users/kolya/Documents/GitHub/Arkly_site/Uploads')),
                ('is_available', models.BooleanField()),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]