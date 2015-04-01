from django.db import models
from django.contrib.auth.models import AbstractUser

class Sponsor(models.Model):
    name              = models.TextField(max_length=150, blank=False, null=False)
    website           = models.URLField()
    description       = models.TextField(max_length=500, blank=True, null=True)
    logo_image        = models.FileField(upload_to='sponsor/')
    sponsorship_level = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class SiteUser(AbstractUser):
    fullname   = models.TextField(blank=True, null=True)
    phone      = models.TextField(blank=True, null=True)
    byu_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.id, self.fullname)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        return self.fullname

class AisEvent(models.Model):
    title    = models.TextField(max_length=150)
    location = models.CharField(max_length=100, blank=True, null=True)
    sponsor  = models.ForeignKey(Sponsor)
    start    = models.DateTimeField()
    end      = models.DateTimeField()

class AisOfficer(models.Model):
    user = models.ForeignKey(SiteUser)
    title = models.TextField()