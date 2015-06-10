from django.db import models

class NModels(models.Model):
    model_name=models.TextField(max_length=30, default='DEFVAL')

class ModelRun(models.Model):
    currmodel= models.ForeignKey(NModels)
    run_name = models.TextField(max_length=20)

class ModelRegion(models.Model):
    model_run = models.ForeignKey(ModelRun)
    region = models.TextField(max_length=20)

class ModelImages(models.Model):
    model_region = models.ForeignKey(ModelRegion)
    map_type = models.TextField(max_length=20)
    map_path = models.TextField(max_length=20)
    timestep = models.TextField(max_length=6)

