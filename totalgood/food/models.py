"""
Food Data
All units in SI (kg, m, s, m^3 (1000 L))
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Substance(models.model):
    name = models.CharField(max_length=64, 
        help_text=_('Common English name for a chemical compound, food item, or food component.'))
    component = models.ManyToManyField(through='SubstanceComponent')

class Name(models.model):
    name = models.CharField(max_length=64, 
        help_text=_('Alternative name (slang, foreign language, scientific) for a food iterm or component.'))
    substance = models.ForeignKey(Substance)
    scientific = models.BooleanField(
        help_text=_('Whether the name is a scientific chemical name.'))


class SubstanceComponent(models.model):
    substance = models.ForeignKey(Substance)
    component = models.ForeignKey(Substance)
    portion = models.FloatField(
        help_text=_('Fraction or portion of a substance (0 < fraction < 1), by weight, made up of the component.'))

class Nutrient(models.model):
    """Vitamin, Mineral or other chemical compound with generally positive nutritional value and a nonzero US RDA"""
    name = models.CharField(max_length=64, 
        help_text=_('Common English name for a chemical compound, food item, or food component.'))
    rda = models.FloatField( 
        help_text=_("United States Food and Drug Administration's recommended Daily Allowance in kilograms."))
    substance = ForeignKey(Substance)
