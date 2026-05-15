from django.db import models

# Create your models here.
class Student(models.Model): 
    name = models.CharField(max_length=100) 
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_code = models.CharField(max_length=10) 
    course_name = models.CharField(max_length=100)  
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
    
class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)  
    
    class Meta:
        unique_together = ['student', 'course'] 
    
    def __str__(self):
        return f"{self.student.name} - {self.course.course_code}"