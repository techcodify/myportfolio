# Generated by Django 2.1.4 on 2019-01-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='categories',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='consult',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='consult',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consult',
            name='details',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]