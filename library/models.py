from django.db import models

class librarian(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class categorys(models.Model):
    name=models.CharField(max_length=50)

class books(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    category=models.ForeignKey(categorys,on_delete=models.CASCADE)
    description=models.CharField(max_length=50)
    coverphoto=models.FileField()
    No_of_copies=models.PositiveIntegerField()
