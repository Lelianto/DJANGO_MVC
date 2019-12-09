from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=200, default=None)
    no_telepon = models.CharField(max_length=200, default=None)
    jabatan = models.CharField(max_length=200, default=None)

    def __str__(self):
        return "Nama Lengkap Direksi : {}, Nomor Telepon : {}, Jabatan : {}".format(self.nama_lengkap, self.no_telepon, self.jabatan)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)
    nomor_absen = models.IntegerField(default=0)
    nilai_rata_rata = models.FloatField(default=0)

    def __str__(self):
        return "Mentee: {}, Nomor Telepon : {}, Nomor Absen : {}, Nilai Rata-rata : {}".format(self.nama_lengkap, self.nomor_telepon, self.nomor_absen, self.nilai_rata_rata)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=200, default=None)
    jadwal_dimulai = models.DateTimeField('jadwal dimulai')
    jadwal_berakhir = models.DateTimeField('jadwal berakhir')

    def __str__(self):
        return "{}, Dimulai : {}, Berakhir : {}".format(self.nama_pelajaran, self.jadwal_dimulai, self.jadwal_berakhir)

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)
    jabatan = models.CharField(max_length=200, default=None)
    mata_pelajaran = models.ForeignKey(MataPelajaran,on_delete=models.CASCADE)

    def __str__(self):
        return "Mentor : {}, Nomor Telepon : {}, Jabatan : {}, Mata Pelajaran : {}".format(self.nama_lengkap, self.nomor_telepon, self.jabatan, self.mata_pelajaran)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=200, default=None)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.IntegerField(default=0)
    mata_pelajaran = models.ForeignKey(MataPelajaran,on_delete=models.CASCADE)

    def __str__(self):
        return "Nama Challenge : {}, Banyak Soal : {}, Bobot Nilai : {}, Mata Pelajaran : {}".format(self.nama_challenge, self.banyak_soal, self.bobot_nilai, self.mata_pelajaran)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=200, default=None)
    banyak_soal = models.IntegerField(default=0)
    bobot_nilai = models.IntegerField(default=0)
    tanggal_pelaksanaan = models.DateTimeField('tanggal pelaksanaan')
    mata_pelajaran = models.ForeignKey(MataPelajaran,on_delete=models.CASCADE)

    def __str__(self):
        return "Nama Live Code : {}, Banyak Soal : {}, Bobot Nilai : {}, Tanggal Pelaksanaan : {}, Mata Pelajaran : {}".format(self.nama_live_code, self.banyak_soal, self.bobot_nilai, self.tanggal_pelaksanaan, self.mata_pelajaran)

