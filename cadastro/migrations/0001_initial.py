# Generated by Django 4.2.6 on 2023-10-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cracha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'cadastro',
                'verbose_name_plural': 'cadastros',
            },
        ),
    ]
