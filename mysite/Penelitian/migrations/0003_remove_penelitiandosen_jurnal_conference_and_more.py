# Generated by Django 5.1.1 on 2024-10-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Penelitian', '0002_penelitiandosen_jurnal_conference_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penelitiandosen',
            name='jurnal_conference',
        ),
        migrations.RemoveField(
            model_name='penelitiandosen',
            name='nama_dosen',
        ),
        migrations.RemoveField(
            model_name='penelitiandosen',
            name='tahun_publikasi',
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='abstract',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='sumber',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='tanggal_publikasi',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='tipe_publikasi',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='penelitiandosen',
            name='judul',
            field=models.CharField(max_length=100),
        ),
    ]