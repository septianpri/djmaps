# Generated by Django 3.1.3 on 2020-11-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djmaps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.IntegerField()),
                ('nama', models.CharField(max_length=255, null=True)),
                ('alamat', models.CharField(max_length=255, null=True)),
                ('kecamatan', models.CharField(max_length=255, null=True)),
                ('keterangan', models.CharField(max_length=255, null=True)),
                ('kategori', models.CharField(max_length=255, null=True)),
                ('kelurahan', models.CharField(max_length=255, null=True)),
                ('imgpath', models.CharField(max_length=255, null=True)),
                ('id_kec', models.CharField(max_length=255, null=True)),
                ('id_kel', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': '"data"."poi"',
                'managed': True,
            },
        ),
    ]
