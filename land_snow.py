"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land surface snow'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Properties of land surface snow scheme',
    'properties': [
        ('tiling', 'str', '0.1',
             'Describe the snow tiling, if any.'),
        ('number_of_snow_layers', 'int', '1.1',
             'The number of snow levels used in the land surface scheme/model'),
        ('albedo', 'ENUM:snow_albedo_methods', '1.1',
             'Description of the treatment of snow albedo'),
        ('density', 'ENUM:snow_density_methods', '1.1',
             'Description of the treatment of snow density'),
        ('water_equivalent', 'ENUM:snow_water_equivalent_methods', '1.1',
             'Description of the treatment of the snow water equivalent'),
        ('heat_content', 'ENUM:snow_heat_content_methods', '1.1',
             'Description of the treatment of the heat content of snow'),
        ('temperature', 'ENUM:snow_temperature_methods', '1.1',
             'Description of the treatment of snow temperature'),
        ('liquid_water_content', 'ENUM:snow_liquid_water_content_methods', '1.1',
             'Description of the treatment of snow liquid water'),
        ('snow_cover_fractions', 'ENUM:snow_cover_fraction_types', '1.N',
             'Specify cover fractions used in the surface snow scheme'),
        ('processes', 'ENUM:snow_processes', '1.N',
             'Snow related processes in the land surface scheme'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['snow_albedo_methods'] = {
    'description': 'Treatment of snow albedo',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ('constant', None),
    ]
}

ENUMERATIONS['snow_density_methods'] = {
    'description': 'Treatment of snow density',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('constant', None),
    ]
}

ENUMERATIONS['snow_water_equivalent_methods'] = {
    'description': 'Treatment of snow water equivalent',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_heat_content_methods'] = {
    'description': 'Treatment of snow heat content',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_temperature_methods'] = {
    'description': 'Treatment of snow temperature',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}


ENUMERATIONS['snow_liquid_water_content_methods'] = {
    'description': 'Treatment of snow liquid water',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_cover_fraction_types'] = {
    'description': 'Snow cover fraction types',
    'is_open': True,
    'members': [
        ('ground snow fraction', None),
        ('vegetation snow fraction', None),
    ]
}

ENUMERATIONS['snow_processes'] = {
    'description': 'Snow-related processes',
    'is_open': True,
    'members': [
        ('snow interception', None),
        ('snow melting', None),
        ('snow freezing', None),
        ('blowing snow', None),
    ]
}

