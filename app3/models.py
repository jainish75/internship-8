import datetime
import os
from django.db import models

# Create your models here.
class Detail(models.Model):
  image= models.ImageField(upload_to = 'uploads/detail')
  text= models.CharField(max_length=200)
  class meta:
      db_table="detail"
  def __str__(self):
       return self.text

def filepath(request,filename):
    old_filename=filename
    timenow= datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename="%S%S" % (timenow,old_filename)
    return os.path.join('uploads/',filename)

class navbar(models.Model):
  name= models.CharField(max_length=200)
  link= models.CharField(max_length=2000)

# from django.db import models


# Create your models here.
class main_menu(models.Model):
    mainmenu_id = models.AutoField(primary_key=True)
    menuname = models.CharField(max_length=50)
    menulink = models.CharField(max_length=100)
    def __str__(self):
       return self.menuname

class sub_menu(models.Model):
    submenu_id = models.AutoField(primary_key=True)
    mainmenu_id = models.IntegerField()
    submenu_name = models.CharField(max_length=50)
    submenu_link = models.CharField(max_length=100)
    def __str__(self):
       return self.submenu_name


class meta:
        db_table="navbar"


def __str__(self):
    return self.name
  
