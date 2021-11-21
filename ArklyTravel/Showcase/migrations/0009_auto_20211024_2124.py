# Generated by Django 3.2.8 on 2021-10-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0008_alter_goods_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='/Uploads'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
