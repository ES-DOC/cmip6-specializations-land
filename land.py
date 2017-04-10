"""A realm sepecialization.

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
AUTHORS = 'David Hassell, Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version, Rich Ellis (CEH), Phillipe Peylin (IPSL)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-04-05", "David Hassell",
        "Initialised from CMIP5 mind map + incorporating initital feedback from Rich Ellis and Pillipe Peylin"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Land Surface Realm'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'land_grid'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'land_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'land_soil',
    'land_snow',
    'land_vegetation',
    'land_energy_balance',
    'land_albedo',
#    'land_carbon_cycle',
#    'land_nitrogen_cycle',
#    'land_river_routing',
#    'land_lakes',
    ]

# --------------------------------------------------------------------
# DETAILS: top level realm details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS: top level realm enumerations
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
