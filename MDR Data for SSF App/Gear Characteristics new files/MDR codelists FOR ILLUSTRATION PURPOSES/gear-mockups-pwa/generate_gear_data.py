#!/usr/bin/env python3
"""Generate JavaScript gear data from MDR Excel file"""

import pandas as pd
import json

# Read the MDR data
xlsx_path = '../MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx'
df = pd.read_excel(xlsx_path, sheet_name='GEAR_CHARACT_BY_GEAR_TYPE')

# Field descriptions
FIELD_DESCRIPTIONS = {
    'GM': 'Gear Dimension - Length/Width/Perimeter',
    'GM2': 'Gear Dimension - Additional Length/Width',
    'HE': 'Height',
    'HE2': 'Height - Additional Dimension',
    'GN': 'Gear Dimension - Number',
    'ME': 'Mesh Size',
    'MS': 'Mesh Type',
    'HS': 'Hook Size',
    'DA': 'Devices & Gear Attachments',
    'GD': 'Gear Description',
    'NI': 'Number of Lines',
    'NL': 'Nominal Length of One Net',
    'NN': 'Number of Nets in Fleet',
    'QG': 'Quantity of Gear on Board',
    'MT': 'Model of Trawl',
    'TT': 'Twine Type',
    'TW': 'Twine Thickness',
    'GO': 'Gear Bar Distance',
    'MK': 'Gear Marker'
}

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
        field = {
            'code': row['GEAR_CHARACT'],
            'description': FIELD_DESCRIPTIONS.get(row['GEAR_CHARACT'], row['GEAR_CHARACT']),
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
