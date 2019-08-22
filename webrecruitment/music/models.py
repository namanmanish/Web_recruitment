from django.db import models


class Person(models.Model):
 STATE_CHOICES =(
    ('Gujarat','Gujarat'),
    ('Maharashtra','Maharashtra'),
    ('Karnataka','Karnataka'),
 )
 CITY_CHOICES =(
    ('Bahavanagar','Bahavanagar'),
    ('Ahmedabad','Ahmedabad'),
    ('Baroda','Baroda'),
    ('Mumbai','Mumbai'),
    ('Nasik','Nasik'),
    ('Pune','Pune'),
    ('Suratkal','Suratkal'),
    ('Manglor','Manglor'),
    ('Banglore','Banglore'),
 )
 COLLEGE_CHOICES=(
    ('NITK','NITK'),
    ('D Y Patil','D Y Patil'),
    ('SVNIT','SVNIT'),
 )
 name = models.CharField(max_length=200)
 state = models.CharField(max_length=200, choices=STATE_CHOICES)
 city = models.CharField(max_length=200, choices=CITY_CHOICES)
 college = models.CharField(max_length=200, choices=COLLEGE_CHOICES)
 age = models.IntegerField(default=0)
 def __str__(self):
        return self.name

class State(models.Model):
 name = models.CharField(max_length=200)
 def __str__(self):
        return self.name

class City(models.Model):
 state_name = models.ForeignKey(State, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 def __str__(self):
        return self.name

class College(models.Model):
 name = models.CharField(max_length=200)
 def __str__(self):
        return self.name

