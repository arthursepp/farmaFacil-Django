# Generated by Django 5.0.6 on 2024-07-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0002_remove_usuario_telefone_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='codigo_hex',
            field=models.CharField(default='5a1f97c2247e46e789aeae8a689eac31', editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
