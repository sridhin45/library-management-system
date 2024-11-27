from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


    def __str__ (self):
        return self.name

class booking(models.Model):
    booking_id=models.ForeignKey("library.books",on_delete=models.CASCADE)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    return_date=models.DateField(blank=True,null=True)
    status=models.CharField( max_length=50,default='pending')
    booking_date=models.DateField()




