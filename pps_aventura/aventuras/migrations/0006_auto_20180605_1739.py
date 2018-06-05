# Generated by Django 2.0.5 on 2018-06-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aventuras', '0005_auto_20180605_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='evento',
            name='ubicacionLat',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='ubicacionLng',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]