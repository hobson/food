"""
Food Data
All units in SI (kg, m, s, m^3 (1000 L))
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

def representation(model, field_names=[]):
    """
    Unicode representation of a particular model instance (object or record or DB table row)
    """
    if not field_names:
        field_names = getattr(model, 'IMPORTANT_FIELDS', ['pk'])
    retval = model.__class__.__name__ + u'('
    retval += ', '.join("%s" % (repr(getattr(model, s, '') or '')) for s in field_names[:min(len(field_names), representation.max_fields)])
    return retval + u')'
representation.max_fields = 5


class Substance(models.Model):
    name = models.CharField(max_length=64,
        help_text=_('Common English name for a chemical compound, food item, or food component.'))
    component = models.ManyToManyField('Substance', through='SubstanceComponent', symmetrical=False, related_name='components')
    synonym = models.ManyToManyField('Name', through='SubstanceName', related_name='synonyms')
 
    def __unicode__(self):
        return representation(self)


class SubstanceComponent(models.Model):
    # to avoid the target model having a reverse relationship to this one set related_name='+' or end the related_name with a +
    substance = models.ForeignKey(Substance, related_name='substance+')
    component = models.ForeignKey(Substance, related_name='component+')
    portion = models.FloatField(
        help_text=_('Fraction or portion of a substance (0 < fraction < 1), by weight, made up of the component.'))


class Name(models.Model):
    name = models.CharField(max_length=64, 
        help_text=_('Alternative name (slang, foreign language, scientific) for a food iterm or component.'))
    substance = models.ForeignKey(Substance, related_name='substances')
    scientific = models.BooleanField(
        help_text=_('Whether the name is a scientific chemical name.'))


class SubstanceName(models.Model):
    # to avoid the target model having a reverse relationship to this one set related_name='+' or end the related_name with a +
    substance = models.ForeignKey(Substance)
    name = models.ForeignKey(Name)
    portion = models.FloatField(
        help_text=_('Fraction or portion of a substance (0 < fraction < 1), by weight, made up of the component.'))


class Nutrient(models.Model):
    """Vitamin, Mineral or other chemical compound with generally positive nutritional value and a nonzero US RDA"""
    name = models.CharField(max_length=64, 
        help_text=_('Common English name for a chemical compound, food item, or food component.'))
    rda = models.FloatField( 
        help_text=_("United States Food and Drug Administration's recommended Daily Allowance in kilograms."))
    substance = models.ForeignKey(Substance)
