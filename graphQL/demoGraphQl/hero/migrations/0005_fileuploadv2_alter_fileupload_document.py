# Generated by Django 4.0.4 on 2022-04-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_delete_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.BinaryField()),
            ],
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='document',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]