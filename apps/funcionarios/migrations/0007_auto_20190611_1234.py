# Generated by Django 2.2.2 on 2019-06-11 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_funcionario_doc_ident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='doc_ident',
            new_name='cpf',
        ),
    ]
