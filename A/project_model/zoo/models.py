from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=200, default=None)
    species = models.CharField(max_length=200, default=None)
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)

    def __str__(self):
        return "Hewan : {}, Species : {}, Berat : {}, Umur: {}".format(self.nama, self.species, self.berat, self.umur)

class Kandang(models.Model):
    nama = models.CharField(max_length=200, default=None)
    isi_kandang = models.CharField(max_length=200, default=None)
    luas_kandang = models.IntegerField(default=0)
    
    def __str__(self):
        return "Kandang : {}, Berisi : {}, dengan luas area : {} meter persegi".format(self.nama, self.isi_kandang, self.luas_kandang)

class Penjaga(models.Model):
    nama = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)
    jadwal_jaga = models.DateTimeField('jadwal jaga')

    def __str__(self):
        return "Penjaga : {}, dengan nomor telepon : {}, memiliki jadwal jaga : {}".format(self.nama, self.nomor_telepon, self.jadwal_jaga)

class Pengunjung(models.Model):
    nama = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)
    hari_berkunjung = models.DateTimeField('hari berkunjung')

    def __str__(self):
        return "Pengunjung : {}, dengan nomor telepon : {}, berkunjung pada hari/tanggal : {}".format(self.nama, self.nomor_telepon, self.hari_berkunjung)
