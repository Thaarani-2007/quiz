from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.name

class Question(models.Model):
    class_name_choices = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12")
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=2, choices=class_name_choices)
    question_text = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_answer = models.CharField(max_length=1, choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')])

    def __str__(self):
        return self.question_text


class studentdetails(models.Model):
    Admission_No= models.CharField(max_length=7, primary_key=True)
    Student_name= models.CharField(max_length=50)
    password= models.CharField(max_length=50)


class result(models.Model):
    admission_no=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    section=models.CharField(max_length=50, default="Not Updated",)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    score=models.IntegerField()