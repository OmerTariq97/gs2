from django.db import models

# Create your models here.
class Student(models.Model):
    name    = models.CharField(max_length=100)
    roll    = models.IntegerField()
    city    = models.CharField(max_length=100)



class Instructor(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()

class Course(models.Model):
    title    = models.CharField(max_length=100)
    Total_Students  = models.IntegerField()
    Instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True)

class Singer(models.Model):
    name    =models.CharField(max_length=100)
    gender  =models.CharField(max_length=50)

class Song(models.Model):
    title   =models.CharField(max_length=100)
    Singer  =models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    duration    =models.IntegerField()

    def __str__(self):
        return self.title
