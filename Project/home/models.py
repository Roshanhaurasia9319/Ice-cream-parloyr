from django.db import models

# # Create your models here.
# makemigration -create changes and store in a file
#migrate -apply the pending changes created makemigrations
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):#how to see user details by his name or email
       return self.name
