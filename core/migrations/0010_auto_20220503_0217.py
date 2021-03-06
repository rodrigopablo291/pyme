# Generated by Django 3.2.13 on 2022-05-03 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_categoriademandaoferta_nombrecategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriademandaoferta',
            name='nombrecategoria',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='DemandaPyme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('demandapyme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandaspyme', to='core.categoriademandaoferta', to_field='nombrecategoria')),
                ('idcategoriademaandaoferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriademandaoferta')),
                ('idpymed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pyme')),
            ],
            options={
                'verbose_name': 'DemandaPyme',
                'verbose_name_plural': 'DemandaPyme',
            },
        ),
    ]
