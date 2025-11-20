#!/usr/bin/env python3
"""
Balsamiq Wireframe Generator for Fishing Gear Characteristics
Automatically generates mobile wireframes for all gear types based on MDR data
"""

import pandas as pd
import os
from typing import Dict, List, Tuple

# Field descriptions mapping
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

# Unit mappings
UNIT_MAP = {
    'MTR': 'm',
    'MMT': 'mm',
    'C62': 'pieces'
}

# Field type specific units
FIELD_UNITS = {
    'GM': 'm', 'GM2': 'm', 'HE': 'm', 'HE2': 'm', 'NL': 'm',
    'ME': 'mm', 'HS': 'mm', 'TW': 'mm', 'GO': 'mm',
    'GN': 'pieces', 'NN': 'pieces', 'QG': 'pieces',
    'NI': 'lines',
    'GN_HOOKS': 'hooks'  # Special case for longlines
}

def get_gear_name(gear_code: str) -> str:
    """Map gear codes to readable names"""
    gear_names = {
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
    return gear_names.get(gear_code, gear_code)

def create_balsamiq_wireframe(gear_type: str, gear_name: str, 
                              mandatory_fields: List[Dict], 
                              optional_fields: List[Dict],
                              file_num: int) -> str:
    """Generate Balsamiq XML for a gear type"""
    
    y_position = 60
    control_id = 0
    controls = []
    
    # iPhone frame
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::iPhone" x="0" y="0" w="-1" h="-1" measuredW="378" measuredH="814" zOrder="0" locked="false" isInGroup="-1">
      <controlProperties>
        <model>IPhoneX</model>
      </controlProperties>
    </control>''')
    control_id += 1
    
    # Title
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::Title" x="20" y="{y_position}" w="-1" h="-1" measuredW="335" measuredH="33" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <size>20</size>
        <text>Gear%20Characteristics</text>
      </controlProperties>
    </control>''')
    control_id += 1
    y_position += 40
    
    # Gear Type Label
    gear_label = f"Gear Type: {gear_type} - {gear_name}".replace(' ', '%20')
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::Label" x="20" y="{y_position}" w="-1" h="-1" measuredW="300" measuredH="21" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text>{gear_label}</text>
      </controlProperties>
    </control>''')
    control_id += 1
    y_position += 30
    
    # Horizontal rule
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::HRule" x="20" y="{y_position}" w="335" h="-1" measuredW="100" measuredH="10" zOrder="{control_id}" locked="false" isInGroup="-1"/>''')
    control_id += 1
    y_position += 15
    
    # Mandatory Fields Section
    if mandatory_fields:
        controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::SubTitle" x="20" y="{y_position}" w="-1" h="-1" measuredW="226" measuredH="24" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <size>16</size>
        <text>MANDATORY%20FIELDS</text>
      </controlProperties>
    </control>''')
        control_id += 1
        y_position += 35
        
        for field in mandatory_fields:
            y_position, control_id = add_field_control(controls, field, y_position, control_id, True)
    
    # Horizontal rule before optional
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::HRule" x="20" y="{y_position}" w="335" h="-1" measuredW="100" measuredH="10" zOrder="{control_id}" locked="false" isInGroup="-1"/>''')
    control_id += 1
    y_position += 15
    
    # Optional Fields Section
    if optional_fields:
        controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::SubTitle" x="20" y="{y_position}" w="-1" h="-1" measuredW="201" measuredH="24" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <size>16</size>
        <text>OPTIONAL%20FIELDS</text>
      </controlProperties>
    </control>''')
        control_id += 1
        y_position += 35
        
        for field in optional_fields:
            y_position, control_id = add_field_control(controls, field, y_position, control_id, False)
    
    # Info note
    y_position += 10
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::Label" x="20" y="{y_position}" w="-1" h="-1" measuredW="277" measuredH="21" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <color>6710886</color>
        <size>11</size>
        <text>*%20Required%20fields%20must%20be%20completed%20before%20saving</text>
      </controlProperties>
    </control>''')
    control_id += 1
    y_position += 140
    
    # Buttons
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::Button" x="20" y="{y_position}" w="150" h="45" measuredW="66" measuredH="28" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text>Cancel</text>
      </controlProperties>
    </control>''')
    control_id += 1
    
    controls.append(f'''    <control controlID="{control_id}" controlTypeID="com.balsamiq.mockups::Button" x="185" y="{y_position}" w="170" h="45" measuredW="90" measuredH="28" zOrder="{control_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <color>2848996</color>
        <text>Save%20Gear</text>
      </controlProperties>
    </control>''')
    
    total_height = y_position + 50
    
    # Build complete XML
    controls_xml = '\n'.join(controls)
    xml = f'''<mockup version="1.0" skin="sketch" fontFace="Balsamiq Sans" measuredW="375" measuredH="{total_height}">
  <controls>
{controls_xml}
  </controls>
</mockup>'''
    
    return xml

def add_field_control(controls: List[str], field: Dict, y_pos: int, 
                     ctrl_id: int, is_mandatory: bool) -> Tuple[int, int]:
    """Add a field control (label + input) to the wireframe"""
    
    code = field['code']
    data_type = field['data_type']
    unit = field.get('unit', '')
    
    # Get readable description
    desc = FIELD_DESCRIPTIONS.get(code, code)
    label_text = f"{desc}%20%28{code}%29"
    if is_mandatory:
        label_text += "%20*"
    
    # Label
    controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::Label" x="20" y="{y_pos}" w="-1" h="-1" measuredW="300" measuredH="21" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text>{label_text}</text>
      </controlProperties>
    </control>''')
    ctrl_id += 1
    y_pos += 25
    
    # Input field based on type
    if data_type == 'CODE':
        # Dropdown
        if code == 'DA':
            placeholder = 'Select%20attachments...'
        elif code == 'MS':
            placeholder = 'Select%20mesh%20type'
        elif code == 'TT':
            placeholder = 'Select%20twine%20type'
        else:
            placeholder = 'Select...'
        
        controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::ComboBox" x="20" y="{y_pos}" w="335" h="-1" measuredW="150" measuredH="26" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text>{placeholder}</text>
      </controlProperties>
    </control>''')
        ctrl_id += 1
        y_pos += 40
        
    elif data_type == 'TEXT' and code == 'GD':
        # Text area for description
        controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::TextArea" x="20" y="{y_pos}" w="335" h="80" measuredW="200" measuredH="63" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text/>
      </controlProperties>
    </control>''')
        ctrl_id += 1
        y_pos += 95
        
    elif data_type == 'TEXT':
        # Single line text input
        controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::TextInput" x="20" y="{y_pos}" w="335" h="-1" measuredW="79" measuredH="27" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text/>
      </controlProperties>
    </control>''')
        ctrl_id += 1
        y_pos += 40
        
    else:
        # Numeric input with unit
        controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::TextInput" x="20" y="{y_pos}" w="280" h="-1" measuredW="79" measuredH="27" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text/>
      </controlProperties>
    </control>''')
        ctrl_id += 1
        
        if unit:
            unit_display = unit.replace(' ', '%20')
            controls.append(f'''    <control controlID="{ctrl_id}" controlTypeID="com.balsamiq.mockups::Label" x="310" y="{y_pos+3}" w="-1" h="-1" measuredW="40" measuredH="21" zOrder="{ctrl_id}" locked="false" isInGroup="-1">
      <controlProperties>
        <text>{unit_display}</text>
      </controlProperties>
    </control>''')
            ctrl_id += 1
        
        y_pos += 40
    
    return y_pos, ctrl_id

def main():
    """Main function to generate all wireframes"""
    
    # Read the gear characteristics data
    xlsx_path = '../MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx'
    df = pd.read_excel(xlsx_path, sheet_name='GEAR_CHARACT_BY_GEAR_TYPE')
    
    # Get unique gear types
    gear_types = df['GEAR_TYPE'].unique()
    
    print(f"Generating wireframes for {len(gear_types)} gear types...")
    
    for idx, gear_type in enumerate(sorted(gear_types), start=5):
        # Get all characteristics for this gear
        gear_data = df[df['GEAR_TYPE'] == gear_type]
        
        mandatory_fields = []
        optional_fields = []
        
        for _, row in gear_data.iterrows():
            field_info = {
                'code': row['GEAR_CHARACT'],
                'data_type': row['UN_DATA_TYPE'],
                'unit': FIELD_UNITS.get(row['GEAR_CHARACT'], UNIT_MAP.get(row['UNITS'], ''))
            }
            
            # Special case for hooks in longlines
            if gear_type in ['LL', 'LLD', 'LLS', 'LHM', 'LHP', 'LTL', 'LVT', 'LX'] and field_info['code'] == 'GN':
                field_info['unit'] = 'hooks'
            
            if row['MANDATORY'] == 'YES':
                mandatory_fields.append(field_info)
            else:
                optional_fields.append(field_info)
        
        # Generate wireframe
        gear_name = get_gear_name(gear_type)
        xml_content = create_balsamiq_wireframe(
            gear_type, gear_name, mandatory_fields, optional_fields, idx
        )
        
        # Save file
        filename = f"{idx:02d}_{gear_type}_{gear_name.replace(' ', '_').replace('/', '_')}.bmml"
        filepath = os.path.join('.', filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"✓ Created: {filename}")
    
    print(f"\n✅ Successfully generated {len(gear_types)} wireframes!")
    print("\nTo view: Import .bmml files into Balsamiq Mockups")

if __name__ == '__main__':
    main()
