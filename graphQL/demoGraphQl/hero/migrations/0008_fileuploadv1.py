# Generated by Django 4.0.4 on 2022-04-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0007_alter_fileuploadv2_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadv1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
