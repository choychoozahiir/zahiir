from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    NumofStudents = models.IntegerField()
    Category = models.CharField(max_length=100)
    Duration = models.IntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return self.name