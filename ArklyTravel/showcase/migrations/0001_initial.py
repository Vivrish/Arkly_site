# Generated by Django 3.2.8 on 2021-10-24 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=4)),
                ('type', models.CharField(max_length=30)),
                ('quantity', models.SmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('is_available', models.BooleanField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Showcase.stock')),
            ],
        ),
    ]
