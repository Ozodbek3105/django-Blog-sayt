from django.db import models

# Create your models here.



class About(models.Model):

    title = models.CharField(max_length=300 )
    discription = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
    

class Social_links(models.Model):

    name = models.CharField(max_length=100)
    link = models.URLField(unique=True )
    def __str__(self) -> str:
        return self.name
    