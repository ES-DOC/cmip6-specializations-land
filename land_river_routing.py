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
DESCRIPTION = 'Land surface river routing'

# --------------------------------------------------------------------
# RIVER ROUTNG: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'TODO',
    'properties' : [
        ('tiling', 'str', '0.1',
             'Describe the river routing, if any.'),
        ('grid_inherited_from_land_surface', 'bool', '1.1',
             'Is the grid inherited from land surface?'),
        ('grid_description', 'str', '1.1',
             'General description of grid, if not inherited from land surface'),
        ('number_of_reservoirs', 'int', '1.1',
             'Enter the number of reservoirs'),
        ('prognostic_variables', 'ENUM:prognostic_Variable_types', '1.N',
             'Specify the prognostic variables within the river routing scheme'),
        ('water_re-evaporation', 'ENUM:water_re-evaporation_types', '1.N',
             'TODO'),
        ('coupled_to_atmosphere', 'bool', '0.1',
             'Is river routing coupled to the atmosphere model component?'),
        ('quantities_exchanged_with_atmosphere', 'ENUM:quantities_exchanged_with_atmosphere_types', '0.N',
             'If couple to atmosphere, which quantities are exchanged between river routing and the atmosphere model components?'),
        ('basin_flow_direction_map', 'ENUM:basin_flow_direction_map_types', '1.1',
             'What type of basin flow direction map is being used?'),
    ],
}

# --------------------------------------------------------------------
# CARBON CYCLE: process
# --------------------------------------------------------------------
DETAILS['oceanic_discharge'] = {
    'description': 'TODO',
    'properties' : [
        ('discharge_type', 'ENUM:discharge_types', '1.1',
             'Specify how rivers are discharged to the ocean'),
        ('quantities_transported', 'ENUM:quantities_transported_types', '1.N',
             'Quantities that are exchanged from river-routing to the ocean model component'),
    ]
}

# --------------------------------------------------------------------
# CARBON CYCLE: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['allocation_bin_types'] = {
    'description': 'Specify the allocation of vegetation carbon bins',
    'is_open': True,
    'members': [
        ('leaves + stems + roots', None),
        ('leaves + stems + roots (leafy + woody)', None),
        ('leaves + fine roots + coarse roots + stems', None),
        ('whole plant (no distinction)', None),
        ]
    }

ENUMERATIONS['allocation_fraction_types'] = {
    'description': 'Describe how the fractions of allocation are calculated',
    'is_open': True,
    'members': [
        ('fixed', None),
        ('function of vegetation type', None),
        ('function of plant allometry', None),
        ('explicitly calculated', None),
    ]
}
