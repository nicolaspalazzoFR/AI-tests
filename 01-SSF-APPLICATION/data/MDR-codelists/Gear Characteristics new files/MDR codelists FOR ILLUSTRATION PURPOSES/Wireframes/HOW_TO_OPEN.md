# How to Open the Wireframes

## 🎯 Quick Start - Open the Project File

### Step 1: Open Balsamiq Mockups
Download Balsamiq Mockups if you don't have it:
- Desktop: https://balsamiq.com/wireframes/desktop/
- Cloud: https://balsamiq.com/wireframes/cloud/

### Step 2: Open the Project
1. Launch Balsamiq Mockups
2. Go to **File → Open Project**
3. Navigate to this folder
4. Select **`Gear_Characteristics_Wireframes.bmpr`**
5. Click Open

### Step 3: Browse Wireframes
- All 68 wireframes will appear in the left sidebar
- Click any mockup name to view it
- Use arrow keys to navigate between them

---

## 📋 What You'll See

The project contains **68 mobile wireframes** organized as:

### Files 01-04: Example Wireframes
- Hand-crafted to showcase different UI patterns
- Best starting point for review

### Files 05-68: Complete Gear Type Set
- Auto-generated from MDR data
- Covers all 64 gear types
- Consistent structure and layout

---

## ✅ Verification

The `.bmpr` file should:
- ✅ Open without errors in Balsamiq
- ✅ Show 68 mockups in the sidebar
- ✅ Display project name: "Gear Characteristics Wireframes"
- ✅ Show proper wireframe structure with iPhone frame
- ✅ Display all field labels with codes (GM, HE, ME, etc.)

---

## 🆘 Troubleshooting

### If the .bmpr file won't open:

**Option 1: Use Individual .bmml Files**
- Import files 01-04 first to see examples
- Then import specific gear types as needed
- File → Import → Mockup JSON
- Select .bmml files

**Option 2: Regenerate the .bmpr**
```bash
cd "Wireframes folder path"
python3 create_bmpr.py
```

### If mockups appear blank:
- Try zooming out (View → Zoom → Fit to Window)
- Check that all mockup elements loaded
- Re-import the specific .bmml file

---

## 📁 File Structure Reference

The `.bmpr` file internally contains:
```
Gear_Characteristics_Wireframes.bmpr/
├── mockups/
│   ├── 0.bmml   (01_DRB_Dredges_Boat)
│   ├── 1.bmml   (02_GNS_Set_Gillnets)
│   ├── 2.bmml   (03_LL_Longlines)
│   ├── 3.bmml   (04_OTB_Bottom_Trawls)
│   ├── 4.bmml   (05_DRB_Boat_Dredges)
│   └── ... (64 more)
└── info.json (Project metadata)
```

---

## 🎨 Using the Wireframes

### For Review/Discussion:
1. Open wireframes 01-04 first (examples)
2. Navigate through different gear categories
3. Note mandatory vs optional field patterns
4. Use for stakeholder presentations

### For Implementation:
1. Reference field codes map to MDR database
2. Use README.md for field definitions
3. Each wireframe = validation rule set
4. Generate UI from wireframe specs

---

**Need Help?** Check README.md for complete documentation
