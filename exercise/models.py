from django.db import models


class Person(models.Model):
    fist_name = models.DateTimeField(null=False)
    last_name = models.DateTimeField(null=False)
    
    class Meta:
        abstract = True


class Student(Person):
    course = models.TextField(null=False)
    hasScholarship = models.BooleanField(null=False)

    class Meta:
        db_table = "students"    


class Teacher(Person):
    qualification  = models.TextField(null=False)
    salary = models.FloatField(null=False)

    class Meta:
        db_table = "teachers"    

