from django.db import models

class School(models.Model):
  
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    
class Class(models.Model):

    ID = models.AutoField(primary_key=True)
    Class = models.CharField(max_length=100)

class Assesment_Areas(models.Model):

    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

class Student(models.Model):

    ID = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=100)

class Answers(models.Model):

    ID = models.AutoField(primary_key=True)
    Answers = models.CharField(max_length=100)

class Awards(models.Model):

    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

class Subject(models.Model):

    ID = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=100)
    Subject_score =  models.DecimalField(max_digits=5, decimal_places=2)  # This field is not used in the original database schema, but it

class Summery(models.Model):

    School_Id = models.ForeignKey(School, on_delete=models.CASCADE)
    Sydney_Participants = models.IntegerField()
    Sydney_Percentile = models.IntegerField()
    Assesment_Area_Id = models.ForeignKey(Assesment_Areas, on_delete=models.CASCADE)
    Award_Id = models.ForeignKey(Awards, on_delete=models.CASCADE)
    Class_Id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Correct_answer_precentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    Correct_Answer = models.CharField(max_length=1)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Participant = models.IntegerField()
    Student_score = models.DecimalField(max_digits=5, decimal_places=2)
    Subject_Id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Category_Id = models.CharField(max_length=100)
    Year_level_name =models.CharField(max_length=100)
    Answer_Id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    Correct_answer_id = models.CharField(max_length=1)

# Create your models here.
