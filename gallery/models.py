from django.db import models
from core import settings

class Picture(models.Model):
    """
    This class holds the picture model. 
    Attributes:
        name: CharField which holds the name.
        upload: UploadField, should be an option to upload a picture.
        available: BooleanField, Admin can turn this on or off to showcase the image on the site.
    """
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='img', max_length=100, blank=True)
    available = models.BooleanField(default=True)
	
    def __str__(self):
        """
        This method displays the name of the current picture.
        """
        return self.name