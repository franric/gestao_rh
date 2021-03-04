# Generated by Django 3.1.7 on 2021-03-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20210304_1529'),
        ('documentos', '0002_documento_pertence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
