# Generated by Django 3.1.7 on 2021-03-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20210304_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='arquivo',
            field=models.FileField(default='', upload_to='documentos'),
            preserve_default=False,
        ),
    ]
