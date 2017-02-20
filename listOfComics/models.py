from django.db import models


# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length = 40)
    cover = models.ImageField(blank=True, ) #blank makes this optional
    publisher = models.CharField(max_length = 30)
    issue = models.CharField(max_length = 20)
    writer_artist = models.TextField(default="Please add names of writers and artists")
    releaseDate = models.DateField()
    
    def __str__(self):
        return '%s %s' % (self.title, self.issue)