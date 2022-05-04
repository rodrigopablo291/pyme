# Generated by Django 3.2.13 on 2022-05-03 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_industriapyme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pyme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepyme', models.CharField(max_length=50)),
                ('rutpyme', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('whatsapp', models.CharField(max_length=15)),
                ('telegram', models.CharField(max_length=20)),
                ('idindustriapyme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.industriapyme')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
            options={
                'verbose_name': 'Pyme',
                'verbose_name_plural': 'Pyme',
            },
        ),
    ]
