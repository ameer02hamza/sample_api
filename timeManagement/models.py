from django.db import models
from .constants import *


# Create your models here.
class timeSheet(models.Model):
    """
    this model class will create a database of timesheet for labours
    """
    Date = models.DateField()
    jobNumber = models.IntegerField()
    employeeName = models.CharField(max_length=35)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField()
    travelHours = models.IntegerField()
    numberOfBreaks = models.IntegerField()
    totalHours = models.IntegerField()
    comments = models.TextField()
    signOff = models.CharField(max_length=35)


class pileLogs(models.Model):
    """
    this model class will create a database for SteelBeam or TimberPole
    """
    jobNumber = models.IntegerField()
    weatherField = models.CharField(choices=weather, max_length=35)
    Date = models.DateField()
    wallNumber = models.IntegerField()
    pileNumber = models.IntegerField()
    augarDia = models.CharField(choices=Auger_Dia, max_length=35)
    wallType = models.CharField(max_length=35)
    casing = models.CharField(choices=casingType, max_length=45)
    extras = models.CharField(max_length=35)
    signoff = models.CharField(max_length=35)
