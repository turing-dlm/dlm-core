from django.db import models

class Library(models.Model):
    name = models.CharField()
    address = models.CharField()
    rating = models.IntegerField(null=True)
    category = models.CharField()

class UserData(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    email = models.EmailField()
    address = models.CharField()
    mobile = models.CharField()
    photo = models.BinaryField(null=True)

class UserLibraryMapping(models.Model):
    userid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    libraryid = models.ForeignKey(Library, on_delete=models.CASCADE)
    status = models.CharField()