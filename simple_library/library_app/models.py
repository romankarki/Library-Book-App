from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
   
    name = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.name
    


class Books(models.Model):
   
    title = models.CharField(max_length=500,unique=True)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title


class BookUser(models.Model):

    books = models.ForeignKey(Books,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default = timezone.now())

    

    def __str__(self):
        return  self.books.title 

    
    

 
        
    

    




    






    
     



    

