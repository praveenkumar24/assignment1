# Generated by Django 3.0 on 2022-05-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t1app', '0002_rename_photo_img_photo_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]