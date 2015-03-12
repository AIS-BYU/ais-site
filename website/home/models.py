from django.db import models

# Create your models here.
class Sponsor(models.Model):
    company_name = models.TextField(max_length=150, blank=False, null=False)
    website = models.URLField()
    logo_image = models.FileField(upload_to='sponsor/')

    def __str__(self):
        return self.company_name