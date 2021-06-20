from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    rating = models.IntegerField(null=True)
    category = models.CharField(max_length=100)

class UserData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=50)
    photo = models.BinaryField(null=True)

class UserLibraryMapping(models.Model):
    userid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    libraryid = models.ForeignKey(Library, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)