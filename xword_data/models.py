from django.db import models

# Create your models here.
class Puzzle(models.Model):

    # Fields
    title = models.CharField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True,blank=False)
    byline = models.CharField(max_length=255, blank=False)
    publisher = models.CharField(max_length=12, blank=False)
    
   
    # Model Functions
    def __str__(self):
        return str(self.publisher)


