from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=20)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=50)

class Albom(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateField()
    rasm = models.FileField(null=True, blank=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi,on_delete=models.CASCADE)


class Qoshiq(models.Model):
    nom = models.CharField(max_length=40)
    janr = models.CharField(max_length=30)
    davomiylik = models.DurationField()
    fayl = models.FileField(null=True,blank=True)
    albom = models.ForeignKey(Albom,on_delete=models.CASCADE)







