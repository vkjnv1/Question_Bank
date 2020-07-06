from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_id=models.AutoField
    faculty_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
    image = models.ImageField(upload_to='generator/images', default="")

    def __str__(self):
        return self.faculty_name

class add(models.Model):
    #LEVEL = (
        #('Easy', 'Easy'),
        #('Medium', 'Medium'),
        #('Difficult', 'Difficult'),
    #)

    #UNIT = (
        #('1', '1'),
        #('2', '2'),
        #('3', '3'),
    #)

    questionId=models.AutoField(primary_key=True)
    EnterTheQuestion = models.CharField(max_length=200, null=True)
    Subject = models.CharField(max_length=200, null=True)
    DifficultLevel =  models.CharField(max_length=200, null=True)
    unitNo =  models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    Marks_alloted = models.CharField(max_length=200, null=True)
    Module = models.CharField(max_length=200, null=True)
    Semester = models.CharField(max_length=200, null=True)
    Subject_code = models.CharField(max_length=200, null=True)





