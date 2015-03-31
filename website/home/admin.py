from django.contrib import admin
from django import forms
from home.models import *

# Customized admin form
class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = [ 'name', 'website', 'description', 'logo_image', 'sponsorship_level' ]

        SPONSORSHIP_LEVELS = (
            ('platinum', 'platinum'),
            ('gold', 'gold'),
            ('silver', 'silver'),
        )

        widgets = {
            'sponsorship_level': forms.Select(choices=SPONSORSHIP_LEVELS)
        }

class SponsorAdmin(admin.ModelAdmin):
    form = SponsorForm

# Register your models here.
admin.site.register( Sponsor, SponsorAdmin )
admin.site.register( SiteUser )
admin.site.register( AisEvent )