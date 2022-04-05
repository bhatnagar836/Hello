from django.db import models


# Create your models here
# Class is like table and firstname, lastname etc. are like columns
# python manage.py make migrations - telling django to create changes and store in a file
# you have to register model in admin.py

class Contact(models.Model):
    firstname = models.CharField(max_length=61)
    lastname = models.CharField(max_length=61)
    contact_num = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateField()

    # migrate : apply the pending changes created by makemigrations (write in database)
    # Tables will be formed when we run python manage.py migrate command (applying changes)
    # We have to write the logic in views - contact method

    def __str__(self):
        self.name = self.firstname + self.lastname
        return self.name
