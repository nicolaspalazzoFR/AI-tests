#!/usr/bin/env python3
"""Generate JavaScript gear data from MDR Excel file"""

import pandas as pd
import json

# Read the MDR data
xlsx_path = '../MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx'
df = pd.read_excel(xlsx_path, sheet_name='GEAR_CHARACT_BY_GEAR_TYPE')

# Gear-specific field descriptions based on ANNEX XVI - Commission Implementing Regulation
# Format: {GEAR_CODE: {FIELD_CODE: 'Description from ANNEX XVI'}}
GEAR_SPECIFIC_DESCRIPTIONS = {
    # TRAWLS
    'OTB': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'TBN': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'TBS': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'PTB': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'TBB': {'GM': 'Beam length of each beam', 'GN': 'Number of beams towed by the vessel'},
    'OTT': {'GM': 'Perimeter of the opening of each trawl', 'GN': 'Number of trawls simultaneously towed', 'MT': 'Model of trawl (optional)'},
    'OTP': {'GM': 'Perimeter of the opening of each trawl', 'GN': 'Number of trawls simultaneously towed', 'MT': 'Model of trawl (optional)'},
    'TB': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'OTM': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    'PTM': {'GM': 'Perimeter of the opening', 'MT': 'Model of trawl (optional)'},
    
    # SEINES
    'SDN': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    'SSC': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    'SPR': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    'SX': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    'SV': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    'SB': {'GM': 'Overall length of seine lines', 'HE': 'Maximum height of seine lines'},
    
    # SURROUNDING NETS
    'PS': {'GM': 'Length of nets', 'HE': '(Maximum) height of nets'},
    'PS1': {'GM': 'Length of nets', 'HE': '(Maximum) height of nets'},
    'PS2': {'GM': 'Length of nets', 'HE': '(Maximum) height of nets'},
    'LA': {'GM': 'Length of nets', 'HE': '(Maximum) height of nets'},
    'SUX': {'GM': 'Length of nets', 'HE': '(Maximum) height of nets'},
    
    # LIFT NETS
    'LNP': {'GM': 'Maximum perimeter of each net', 'GN': 'Number of nets used'},
    'LNB': {'GM': 'Maximum perimeter of each net', 'GN': 'Number of nets used'},
    'LNS': {'GM': 'Maximum perimeter of each net', 'GN': 'Number of nets used'},
    'LN': {'GM': 'Maximum perimeter of each net', 'GN': 'Number of nets used'},
    
    # FALLING GEAR
    'FCN': {'GM': 'Maximum perimeter of each net/device', 'GN': 'Number of nets/devices used'},
    'FCO': {'GM': 'Maximum perimeter of each net/device', 'GN': 'Number of nets/devices used'},
    'FG': {'GM': 'Maximum perimeter of each net/device', 'GN': 'Number of nets/devices used'},
    
    # DREDGES
    'DRB': {'GM': 'Width of each dredge', 'GN': 'Number of dredges used'},
    'DRH': {'GM': 'Width of each dredge', 'GN': 'Number of dredges used'},
    'DRM': {'GM': 'Width of each dredge', 'GN': 'Number of dredges used'},
    'DRX': {'GM': 'Width of each dredge', 'GN': 'Number of dredges used'},
    
    # GILLNETS
    'GN': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GNS': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GND': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GNC': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GNF': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GTN': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GTR': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    'GEN': {'GM': 'Overall length of nets', 'HE': 'Height of nets'},
    
    # TRAPS
    'FPO': {'GN': 'Number of pots (e.g. creels) used'},
    'FYK': {'GM': 'Overall length of wings and leaders', 'GM2': 'Overall length of wings and leaders', 
            'HE': 'Height of wings', 'HE2': 'Height of leaders', 'GN': 'Number of fyke nets used'},
    'FSN': {'GM': 'Length of frame', 'HE': 'Height of frame'},
    'FWR': {'GM': 'Total length', 'HE': 'Height'},
    'FAR': {'GM': 'Length underwater', 'GM2': 'Length aerial', 'HE': 'Height underwater', 'HE2': 'Height aerial'},
    'FPN': {'GM': 'Overall length of wings and leaders', 'GM2': 'Overall length of wings and leaders',
            'HE': 'Height of wings', 'HE2': 'Height of leaders'},
    'FIX': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    
    # HOOKS AND LINES
    'LHP': {'NI': 'Total number of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LHM': {'NI': 'Total number of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LVT': {'NI': 'Total number of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LTL': {'NI': 'Total number of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LX': {'NI': 'Total number of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LLS': {'GM': 'Overall length of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LLD': {'GM': 'Overall length of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    'LL': {'GM': 'Overall length of lines', 'GN': 'Total number of hooks', 'HS': 'Size of hooks'},
    
    # MISCELLANEOUS
    'HAR': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MHI': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MPM': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MPN': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MSP': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MDR': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MDV': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'HMX': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
    'MIS': {'GD': 'Dimensions and description of each gear', 'GN': 'Number of the gears used'},
}

# Default field descriptions (fallback when gear-specific not available)
DEFAULT_FIELD_DESCRIPTIONS = {
    'GM': 'Gear dimension',
    'GM2': 'Additional gear dimension',
    'HE': 'Height',
    'HE2': 'Additional height',
    'GN': 'Number',
    'ME': 'Mesh size',
    'MS': 'Mesh type',
    'HS': 'Hook size',
    'DA': 'Devices & gear attachments',
    'GD': 'Gear description',
    'NI': 'Number of lines',
    'NL': 'Nominal length of one net',
    'NN': 'Number of nets in fleet',
    'QG': 'Quantity of gear on board',
    'MT': 'Model of trawl',
    'TT': 'Twine type',
    'TW': 'Twine thickness',
    'GO': 'Gear bar distance',
    'MK': 'Gear marker'
}

def get_field_description(gear_code, field_code):
    """Get gear-specific description or fall back to default"""
    if gear_code in GEAR_SPECIFIC_DESCRIPTIONS:
        if field_code in GEAR_SPECIFIC_DESCRIPTIONS[gear_code]:
            return GEAR_SPECIFIC_DESCRIPTIONS[gear_code][field_code]
    return DEFAULT_FIELD_DESCRIPTIONS.get(field_code, field_code)

# Gear names
GEAR_NAMES = {
    'DRB': 'Boat Dredges', 'DRH': 'Hand Dredges', 'DRM': 'Mechanized Dredges',
    'DRX': 'Other Dredges', 'FAR': 'Barriers/Fences/Weirs', 'FCN': 'Cast Nets',
    'FCO': 'Cover Pots/Lantern Nets', 'FG': 'Stationary Gillnets on Stakes',
    'FIX': 'Fixed Traps', 'FPN': 'Stationary Uncovered Pound Nets',
    'FPO': 'Pots', 'FSN': 'Stow Nets', 'FWR': 'Barriers/Fences/Weirs for Fish',
    'FYK': 'Fyke Nets', 'GEN': 'Gillnets (Generic)', 'GN': 'Gillnets',
    'GNC': 'Gillnets Combined', 'GND': 'Drift Gillnets', 'GNF': 'Fixed Gillnets',
    'GNS': 'Set Gillnets', 'GTN': 'Trammel Nets', 'GTR': 'Gill/Trammel Nets Combined',
    'HAR': 'Harpoons', 'HMX': 'Hooks and Lines (Mixed)', 'LA': 'Lampara Nets',
    'LHM': 'Hand Lines - Mechanized', 'LHP': 'Hand Lines - Powered',
    'LL': 'Longlines', 'LLD': 'Drifting Longlines', 'LLS': 'Set Longlines',
    'LN': 'Lift Nets', 'LNB': 'Boat-Operated Lift Nets', 'LNP': 'Portable Lift Nets',
    'LNS': 'Shore-Operated Lift Nets', 'LTL': 'Troll Lines', 'LVT': 'Vertical Lines',
    'LX': 'Hooks and Lines (Other)', 'MDR': 'Mechanized Dredges',
    'MDV': 'Miscellaneous Devices', 'MHI': 'Harvesting Machines',
    'MIS': 'Miscellaneous Gear', 'MPM': 'Manual Pumps', 'MPN': 'Mechanical Pumps',
    'MSP': 'Scraping/Suction Pumps', 'OTB': 'Bottom Trawls',
    'OTM': 'Midwater Trawls', 'OTP': 'Pair Trawls', 'OTT': 'Twin Trawls',
    'PS': 'Purse Seines', 'PS1': 'Purse Seines - One Boat',
    'PS2': 'Purse Seines - Two Boats', 'PTB': 'Bottom Pair Trawls',
    'PTM': 'Midwater Pair Trawls', 'SB': 'Beach Seines', 'SDN': 'Danish Seines',
    'SPR': 'Pair Seines', 'SSC': 'Scottish Seines', 'SUX': 'Surrounding Nets',
    'SV': 'Boat Seines', 'SX': 'Seines (Other)', 'TB': 'Beam Trawls',
    'TBB': 'Bottom Beam Trawls', 'TBN': 'Bottom Nephrops Trawls',
    'TBS': 'Bottom Shrimp Trawls'
}

# Build gear definitions
gear_data = {}

for gear_type in sorted(df['GEAR_TYPE'].unique()):
    gear_info = df[df['GEAR_TYPE'] == gear_type]
    
    mandatory = []
    optional = []
    
    for _, row in gear_info.iterrows():
        field_code = row['GEAR_CHARACT']
        field = {
            'code': field_code,
            'description': get_field_description(gear_type, field_code),
            'type': row['UN_DATA_TYPE'],
            'unit': row['UNITS'] if pd.notna(row['UNITS']) else None
        }
        
        # Special case for hooks
        if gear_type in ['LL', 'LLD', 'LLS', 'LHM', 'LHP', 'LTL', 'LVT', 'LX'] and field['code'] == 'GN':
            field['unit'] = 'hooks'
        
        if row['MANDATORY'] == 'YES':
            mandatory.append(field)
        else:
            optional.append(field)
    
    gear_data[gear_type] = {
        'name': GEAR_NAMES.get(gear_type, gear_type),
        'code': gear_type,
        'mandatory': mandatory,
        'optional': optional
    }

# Write as JavaScript
with open('gear-data.js', 'w') as f:
    f.write('// Auto-generated from MDR_GEAR_CHARACT_BY_GEAR_TYPE\n')
    f.write('// Date: 2025-11-19\n\n')
    f.write('const GEAR_DATA = ')
    f.write(json.dumps(gear_data, indent=2))
    f.write(';\n\n')
    
    # Add mesh types
    f.write('const MESH_TYPES = ["Square", "Diamond"];\n\n')
    
    # Add device attachments (abbreviated list for demo)
    f.write('const DEVICES_ATTACHMENTS = [\n')
    f.write('  "BSC - Bottom-side chafer",\n')
    f.write('  "SRP - Strengthening ropes",\n')
    f.write('  "TQT - Torquette",\n')
    f.write('  "FLT - Float",\n')
    f.write('  "SPG - Separation Grids",\n')
    f.write('  "SMP - Square mesh panel",\n')
    f.write('  "BAC - Bacoma exit window",\n')
    f.write('  "TOR - Tori line (bird scaring)",\n')
    f.write('  "ADD - Acoustic deterrent device",\n')
    f.write('  "OTH - Other"\n')
    f.write('];\n')

print(f'✅ Generated gear-data.js with {len(gear_data)} gear types')
