from django.db import models


# Create your models here.
class Comics(models.Model):
    title = models.CharField(max_length = 40)
    publisher = models.CharField(max_length = 30)
    issue = models.CharField(max_length = 20)
    writer_artist = models.TextField(default="Please add names of writers and artists")
    releaseDate = models.DateField()
    
    def __str__(self):
        return str(self.title, self.issue)