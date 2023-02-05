from django.db import models




class Student(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True, verbose_name='Id')
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)