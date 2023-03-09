from cgitb import text
from distutils.command.upload import upload
from django.db import models
from django.db import models
import datetime
import os
def filepath(request,filename):
    old_filename=filename
    timenow= datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename="%S%S" % (timenow,old_filename)
    return os.path.join('uploads/',filename)
# Create your models here.

class slide(models.Model):
    image=models.ImageField(upload_to="uploads/")
    text=models.TextField(max_length=1000)
    class meta:
            db_table="slide"
    def __str__(self):
       return self.text


class offerimg(models.Model):
    image= models.ImageField(upload_to = 'uploads')
    date=models.DateField(null=True)
    name=models.CharField(max_length=1000)
    class meta:
            db_table="offerimg"
    def __str__(self):
       return self.name

# class activtie(models.Model):
#      image= models.ImageField(upload_to = 'uploads')
#      descp=models.CharField(max_length=1000)
#      name=models.CharField(max_length=1000)

#      class meta:
#             db_table="activtie"

class activ(models.Model):
    image= models.ImageField(upload_to = 'uploads')
    descp=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    class meta:
            db_table="activ"

class servicename(models.Model):
    sname = models.CharField(max_length=50)
    slink = models.CharField(max_length=100)
    class meta:
            db_table="servicename"
    def __str__(self):
       return self.sname



