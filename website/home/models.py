from django.db import models

# Create your models here.
class Sponsor(models.Model):
    name = models.TextField(max_length=150, blank=False, null=False)
    website = models.URLField()
    description = models.TextField(max_length=500, blank=True, null=True)
    logo_image = models.FileField(upload_to='sponsor/')
    sponsorship_level = models.TextField(max_length=50)

    def __str__(self):
        return self.name