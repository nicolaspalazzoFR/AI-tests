#!/usr/bin/env python3
"""
Create a proper Balsamiq .bmpr project file
A .bmpr is a zip with specific structure including project metadata
"""

import os
import json
import zipfile
from datetime import datetime

def create_bmpr_project():
    """Create a proper .bmpr project file with all mockups"""
    
    # Project metadata
    project_info = {
        "ID": "0",
        "mockups": []
    }
    
    # Get all .bmml files
    bmml_files = sorted([f for f in os.listdir('.') if f.endswith('.bmml')])
    
    print(f"Creating .bmpr project with {len(bmml_files)} mockups...")
    
    # Create project structure
    with zipfile.ZipFile('Gear_Characteristics_Wireframes.bmpr', 'w', zipfile.ZIP_DEFLATED) as bmpr:
        
        # Add each mockup
        for idx, bmml_file in enumerate(bmml_files):
            mockup_id = str(idx)
            
            # Read the bmml content
            with open(bmml_file, 'r', encoding='utf-8') as f:
                bmml_content = f.read()
            
            # Extract mockup name from filename (remove .bmml extension)
            mockup_name = bmml_file.replace('.bmml', '')
            
            # Add mockup to project
            mockup_path = f"mockups/{mockup_id}.bmml"
            bmpr.writestr(mockup_path, bmml_content)
            
            # Add to project info
            project_info["mockups"].append({
                "ID": mockup_id,
                "Name": mockup_name,
                "ResourceID": mockup_id
            })
            
            print(f"  ✓ Added: {mockup_name}")
        
        # Create project info
        info_json = {
            "Version": "1.0",
            "Project": {
                "ID": "0",
                "Name": "Gear Characteristics Wireframes",
                "Description": "Mobile wireframes for fishing gear characteristics data entry - All 64 gear types from MDR IGv3",
                "Author": "SSF Team",
                "Created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                "Modified": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            },
            "Mockups": project_info["mockups"]
        }
        
        # Write project info
        bmpr.writestr('info.json', json.dumps(info_json, indent=2))
        
        print(f"\n✅ Created Gear_Characteristics_Wireframes.bmpr")
        print(f"   Contains {len(bmml_files)} mockups")
        print(f"\nTo use: Open the .bmpr file directly in Balsamiq Mockups")

if __name__ == '__main__':
    create_bmpr_project()
