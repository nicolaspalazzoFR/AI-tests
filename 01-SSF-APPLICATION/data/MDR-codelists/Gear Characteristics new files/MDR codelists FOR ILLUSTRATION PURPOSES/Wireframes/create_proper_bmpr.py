#!/usr/bin/env python3
"""
Create proper Balsamiq .bmpr with exact format specification
Based on Balsamiq Cloud format
"""

import os
import json
import zipfile
from datetime import datetime
import uuid

def create_proper_bmpr():
    """Create .bmpr with Balsamiq Cloud format"""
    
    # Get all .bmml files
    bmml_files = sorted([f for f in os.listdir('.') if f.endswith('.bmml')])
    
    print(f"Creating proper .bmpr with {len(bmml_files)} mockups...")
    
    # Create the zip
    with zipfile.ZipFile('Gear_Characteristics_Wireframes.bmpr', 'w', zipfile.ZIP_DEFLATED) as bmpr:
        
        # Create proper info structure
        project_data = {
            "branchID": "Master",
            "branchName": "Master",
            "mockups": [],
            "thumbnails": [],
            "resources": [],
            "attributes": {
                "name": "Gear Characteristics Wireframes",
                "notes": "Mobile wireframes for fishing gear characteristics - All 64 gear types from MDR IGv3",
                "project": {
                    "fonts": []
                }
            }
        }
        
        # Add each mockup
        for bmml_file in bmml_files:
            # Generate UUID for this mockup
            mockup_uuid = str(uuid.uuid4())
            
            # Read the bmml content
            with open(bmml_file, 'r', encoding='utf-8') as f:
                bmml_content = f.read()
            
            # Extract name
            mockup_name = bmml_file.replace('.bmml', '')
            
            # Add to zip with UUID as filename
            bmpr.writestr(f"{mockup_uuid}.bmml", bmml_content)
            
            # Add to project data
            project_data["mockups"].append({
                "id": mockup_uuid,
                "name": mockup_name,
                "branchID": "Master",
                "width": 375,
                "height": 812,
                "measuredWidth": 375,
                "measuredHeight": 812,
                "mockupW": 375,
                "mockupH": 812,
                "version": 1,
                "created": int(datetime.now().timestamp()),
                "modified": int(datetime.now().timestamp()),
                "resourceID": mockup_uuid
            })
            
            print(f"  ✓ Added: {mockup_name}")
        
        # Write project data as .bmpr.json (this is the key!)
        bmpr.writestr('.bmpr.json', json.dumps(project_data, indent=2))
        
        print(f"\n✅ Created proper Gear_Characteristics_Wireframes.bmpr")
        print(f"   Contains {len(bmml_files)} mockups")
        print(f"   Format: Balsamiq Cloud compatible")

if __name__ == '__main__':
    create_proper_bmpr()
