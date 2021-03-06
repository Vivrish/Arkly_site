# Generated by Django 3.2.8 on 2021-11-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_auto_20211106_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='sort',
            field=models.CharField(choices=[('AP', 'ascending_price'), ('DP', 'descending_price'), ('AR', 'ascending_relevance'), ('DR', 'descending_relevance'), ('AD', 'ascending_date'), ('DD', 'descending_date')], default='DP', max_length=20),
        ),
    ]
