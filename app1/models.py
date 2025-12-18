from django.db import models

class Root(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=100)
    mark = models.IntegerField()
    sub = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sno} - {self.name}"
