from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=200)    
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"User {self.firstName} {self.lastName} with email {self.email}"
    
class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name