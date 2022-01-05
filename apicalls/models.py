from django.db import models
class test(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
      return self.name
    email=models.EmailField()
    address=models.TextField()


# Create your models here.
