# Generated by Django 3.2.5 on 2021-09-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_dataio_col_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataio',
            name='id',
        ),
        migrations.AddField(
            model_name='dataio',
            name='index',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
