# Generated by Django 3.2.8 on 2021-10-24 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0011_alter_goods_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='goods',
        ),
    ]
