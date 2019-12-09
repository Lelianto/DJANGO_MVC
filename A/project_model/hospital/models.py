from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)
    bidang = models.CharField(max_length=200, default=None)
    jadwal_praktek = models.DateTimeField('jadwal praktek')

    def __str__(self):
        return "Dr. {}, Nomor Telepon : {}, Bidang : {}, Jadwal Praktek: {}".format(self.nama, self.nomor_telepon, self.bidang, self.jadwal_praktek)

class Pasien(models.Model):
    nama = models.CharField(max_length=200, default=None)
    nomor_telepon = models.CharField(max_length=200, default=None)    
    alamat = models.CharField(max_length=200, default=None)
    keluhan = models.CharField(max_length=200, default=None)

    def __str__(self):
        return "Pasien : {}, Nomor Telepon  : {}, Alamat : {}, Keluhan : {}".format(self.nama, self.nomor_telepon, self.alamat, self.keluhan)

class Resep(models.Model):
    nama = models.CharField(max_length=200, default=None)
    total_harga = models.IntegerField(default=0)
    kumpulan_obat = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return "Resep : {}, Total Harga: {}, Terdiri dari : {}".format(self.nama, self.total_harga, self.kumpulan_obat)

class Obat(models.Model):
    nama = models.CharField(max_length=200, default=None)
    kandungan = models.CharField(max_length=200, default=None)
    khasiat = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return "Nama Obat : {}, Kandung : {}, Khasiat : {}".format(self.nama, self.kandungan, self.khasiat)



