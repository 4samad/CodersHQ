from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class Company(models.Model):
    """Main company model"""
    name = models.CharField(_("Comany name"), max_length=100)
    # logo size https://www.logaster.com/blog/logo-sizes/#company2
    logo = models.ImageField(_("Company logo"), upload_to='logos/', height_field=100, width_field=200, max_length=100)
    website = models.URLField(_("Company website"), max_length=200)


class SponsorshipTypes(models.Model):
    """Company sponsor types"""
    sponsorship_type = models.CharField(_("Company sponsorship type"), max_length=100)
    sponsorship_description = models.CharField(_("Company sponsorship description"), max_length=250)


class Sponsorships(models.Model):
    """Company sponsorship detail and value"""
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
    )
    sponsorship_type = models.OneToOneField(
        SponsorshipTypes,
        on_delete=models.CASCADE,
    )
    sponsorship_value = models.PositiveIntegerField(
        _("Sponsorship Value"),
        default=0,
        validators=[MaxValueValidator(10000000)]
    )
