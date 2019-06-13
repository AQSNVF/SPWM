# Generated by Django 2.2.2 on 2019-06-12 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0007_auto_20190611_1234'),
        ('documentosfunc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentofunc',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentosfunc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentofunc',
            name='proprietariofunc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
