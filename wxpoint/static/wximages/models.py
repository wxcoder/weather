from django.db import models

class NModels(models.Model):
    model_name=models.CharField(max_length=30)

class Modelrun(models.Models):
    currmodel = models.ForeignKey(NModels)
    run_name = models.CharField(maxlength=20)

class MRegion(models.Models):
    model_run = models.ForeignKey(Modelrun)
    region = models.CharField(max_length=20)

class ModelImages(models.Model):
    finalmodel = Models.ForeignKey(MRegion)
    timestep = models.IntegerField(max_value=3)
    picture = models.ImageField(upload_to:pathtomyimagefiles)
