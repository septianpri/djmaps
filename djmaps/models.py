from django.db import models

# Create your models here.
class djmaps(models.Model):
    gid = models.IntegerField()
    nama = models.CharField(max_length = 255, null=True)
    alamat = models.CharField(max_length = 255,null=True)
    kecamatan = models.CharField(max_length = 255,null=True)
    keterangan = models.CharField(max_length = 255,null=True)
    kategori = models.CharField(max_length = 255,null=True)
    kelurahan = models.CharField(max_length = 255,null=True)
    imgpath = models.CharField(max_length = 255,null=True)
    id_kec = models.CharField(max_length = 255,null=True)
    id_kel = models.CharField(max_length = 255,null=True)

    class Meta:
        managed = True
        db_table = '"data"."poi"'
