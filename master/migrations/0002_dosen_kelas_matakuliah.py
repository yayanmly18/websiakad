# Generated by Django 2.0.3 on 2018-04-03 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('nidn', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=150)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.TextField()),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('no_telepon', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('nama_kelas', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('kode_matkul', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_matkul', models.CharField(max_length=150)),
                ('sks', models.IntegerField()),
                ('kelompok_matkul', models.CharField(choices=[('A', 'MPK-Pengembangan Kepribadian'), ('B', 'MKK-Keilmuan dan Ketrampilan'), ('C', 'MKB-Keahlian Berkarya'), ('D', 'MPB-Perilaku Berkarya'), ('E', 'MBB-Berkehidupan Bermasyarakat'), ('F', 'MKU/MKDU'), ('G', 'MKDK'), ('H', 'MKK')], max_length=10)),
                ('progdi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.ProgramStudi')),
            ],
        ),
    ]
