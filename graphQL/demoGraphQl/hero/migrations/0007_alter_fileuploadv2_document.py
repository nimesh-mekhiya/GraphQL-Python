# Generated by Django 4.0.4 on 2022-04-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_delete_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploadv2',
            name='document',
            field=models.TextField(),
        ),
    ]