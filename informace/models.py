from django.db import models
from django.db.models.expressions import SQLiteNumericMixin
from django.db.models.fields import BooleanField

# Create your models here.

class Zvire(models.Model):
    jmeno = models.CharField(max_length=30)
    vaha = models.IntegerField()
    barva = models.CharField(max_length=20, default="")
    zije = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.jmeno} ({self.vaha}) {self.barva} výpis pomocí __str__"


#MVC = model / view / controller

#MTV = model / template / view


#SQL -MySQL, MSSQL, PostgreSQL, SQLLite

#NoSQL - MongoDB