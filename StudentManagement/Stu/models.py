from django.db import models

class StudentInfo(models.Model):
    User_Name = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    Role = models.CharField(max_length=20)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=20)
    Phone_Number = models.IntegerField()
    Student_Id = models.IntegerField()
    Address = models.CharField(max_length=50)
    Pin_Code = models.IntegerField()

    def __str__(self):
        return self.First_Name
# Create your models here.
