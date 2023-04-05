from django.db import models

# Create your models here.
class NagaData(models.Model):
    title = models.CharField(max_length=100,)
    description = models.TextField(unique=True)
    date = models.DateField()
    creater = models.CharField(max_length=20,default="null")

    def _str_(self):
        return self.title

class NagaName(models.Model):
    title = models.CharField(max_length=100)
    rest = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    