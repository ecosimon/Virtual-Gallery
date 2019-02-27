from django.db import models

class Picture(models.Model):
    """
    This class holds the picture model. 
    Attributes:
        name: CharField which holds the name.
        url: UrlField which is the link to the picture and to our heroku database.
        available: BooleanField, Admin can turn this on or off to showcase the image on the site.
    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    available = models.BooleanField(default=True)
	
    def __str__(self):
        """
        This method displays the name of the current picture.
        """
        return self.name