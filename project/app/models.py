from django.db import models

# Create your models here.


class Laptop(models.Model):
    Modelname=models.CharField(max_length=20)
    Company=models.CharField(max_length=20)
    Ram=models.FloatField()
    Rom=models.FloatField()
    Weight=models.FloatField()
    Processor=models.CharField(max_length=5)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.Modelname




    


