from unittest import mock
from django.db import models

# Create your models here.
class log(models.Model):
    uname=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    class meta:
            db_table="log"
    def __str__(self):
       return self.uname


class registration(models.Model):
    uname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=100)
    RPassword=models.CharField(max_length=100)
    class meta:
            db_table="registration"
    def __str__(self):
       return self.uname

class contact(models.Model):
    Yourname=models.CharField(max_length=100)
    YourEmail=models.EmailField(max_length=20)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)
    class meta:
            db_table="contact"
    def __str__(self):
       return self.Yourname
# class Contact(models.Model):
#     name = models.CharField(max_length=50,null=True)
#     email = models.CharField(max_length=122,null=True)
#     subject = models.CharField(max_length=122,null=True)
#     msg = models.TextField(max_length=122,null=True)
#     class meta:
#             db_table="contact"
#     def __str__(self):
#         return self.name            

class appoint_beauty(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=122, null=True)
    service = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    class meta:
          db_table="appoint"
    def __str__(self):
        return self.name 
# class Appoint(models.Model):  
#     name = models.CharField(max_length=50,null=True )
#     email = models.EmailField(max_length=122)
#     phone = models.CharField(max_length=12)
#     desc = models.TextField(max_length=122, null=True)
#     service = models.CharField(choices=(
#             ('Tinting', "Tinting"),
#             ('Treading', "Threading"),
#             ('Facial', "Facial"),
#             ('Eyelash', "Eyelash"),
#             ('Contact Lenses', "Contact Lenses"),
#             ('Waxing', "Waxing"),
#             ('Massage', "Massage"),
#             ('Acylic Tips', "Acylic Tips"),
#             ('Nail Treatment', "Nail Treatment"),
#             ('Shellac', "Shellac"),
#             ('SNS', "SNS"),
#             ('Gel powder Tips', "Gel powder Tips"),
#             ('Ombré Tips', "Ombré Tips"),
#             ('Manicure', "Manicure"),
#             ('Pedicure', "Pedicure"),
#             ),max_length=15,null=True)
#     date = models.DateField(null=True)
#     time = models.TimeField(null=True)
#     def __str__(self):
#         return self.name

