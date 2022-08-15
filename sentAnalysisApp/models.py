from django.db import models

# Create your models here.


class sentimentAnalysis(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title[0:50]
