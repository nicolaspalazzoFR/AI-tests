# Fishing Gear Characteristics Wireframes

## Overview

This folder contains **68 mobile wireframes** (4 manually created + 64 automatically generated) representing the gear characteristics data entry forms for all fishing gear types defined in the MDR (Master Data Registry) code lists.

### Files Available

- **Individual .bmml files** (68 files) - Import separately into Balsamiq
- **Gear_Characteristics_Wireframes.bmpr** - Complete project file with all 68 wireframes bundled together (recommended for easy import)

## Purpose

These wireframes illustrate how fishers will enter gear characteristic data during:
- **Haul declarations** - Recording gear details per fishing operation
- **Departure reports** - Registering gear on board before departure

## File Organization

### Manually Created Examples (01-04)
These showcase different UI patterns and complexity levels:
- `01_DRB_Dredges_Boat.bmml` - Simple gear with 2 mandatory fields
- `02_GNS_Set_Gillnets.bmml` - Gillnets with mesh requirements
- `03_LL_Longlines.bmml` - Highlights NEW hook size requirement (2026)
- `04_OTB_Bottom_Trawls.bmml` - Complex gear with optional technical fields

### Auto-Generated Wireframes (05-68)
All remaining gear types, generated from MDR data:
- Files numbered 05-68
- Named: `{number}_{GEAR_CODE}_{Gear_Name}.bmml`
- Example: `32_LL_Longlines.bmml`

## Wireframe Structure

Each wireframe follows this consistent structure:

### Header
- Title: "Gear Characteristics"
- Gear type identifier: "{CODE} - {Name}"

### Mandatory Fields Section
- Clearly marked with "*" asterisk
- Red/bold visual treatment
- Fields required by EU Regulation 2025/2196

### Optional Fields Section
- Clearly separated from mandatory
- Lighter visual weight
- Can be collapsed in implementation

### Field Types

**1. Numeric Inputs (with units)**
- Measurements: `m` (meters), `mm` (millimeters)
- Quantities: `pieces`, `hooks`, `lines`

**2. Dropdown Selections (CODE fields)**
- Mesh Type: Square or Diamond
- Devices & Attachments: 30+ options
- Twine Type: Material options

**3. Text Inputs**
- Gear Description: Multi-line text area
- Model of Trawl: Single-line text
- Gear Marker: Identification text

### Footer
- Required field disclaimer
- Cancel button
- Save Gear button (primary action)

## Key Features

### Mandatory vs Optional
- **Mandatory fields** vary by gear type
- Based on GEAR_CHARACT_BY_GEAR_TYPE MDR code list
- Enforced by EU fishing regulations

### Context-Aware Units
- Dimensions in meters (m)
- Mesh sizes in millimeters (mm)
- Special case: Hooks in longlines show "hooks" not "pieces"

### 2026 Changes
- Hook Size (HS) is NEW mandatory for longlines
- Effective date: January 10, 2026
- See wireframe 03 for annotation

## Gear Type Categories

### Dredges (05-08)
DRB, DRH, DRM, DRX - Simple dimension + number

### Gillnets (19-26)
GEN, GN, GNC, GND, GNF, GNS, GTN, GTR - Require mesh specifications

### Longlines (30-34, 39-41)
LL, LLD, LLS, LHM, LHP, LTL, LVT, LX - Require hook specifications

### Trawls (49-52, 56-57, 65-68)
OTB, OTM, OTP, OTT, PTB, PTM, TB, TBB, TBN, TBS - Complex mesh + optional technical

### Seines (53-55, 58-64)
PS, PS1, PS2, SB, SDN, SPR, SSC, SUX, SV, SX - Dimension + mesh requirements

### Traps (13-18)
FIX, FPN, FPO, FSN, FWR, FYK - Variable complexity

### Miscellaneous (27-28, 42-48)
HAR, HMX, MDR, MDV, MHI, MIS, MPM, MPN, MSP - Simplified forms

## Technical Details

### Data Source
- MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx
- EU Regulation 2025/2196 Annexes XV & XVI
- Effective date: January 10, 2026

### Field Codes Reference

| Code | Description | Data Type | Common Units |
|------|-------------|-----------|--------------|
| GM | Gear Dimension - Length/Width/Perimeter | MEASURE | m |
| GM2 | Additional Length/Width | MEASURE | m |
| HE | Height | MEASURE | m |
| HE2 | Additional Height | MEASURE | m |
| GN | Gear Dimension - Number | QUANTITY | pieces/hooks |
| ME | Mesh Size | MEASURE | mm |
| MS | Mesh Type | CODE | - |
| HS | Hook Size (NEW 2026) | MEASURE | mm |
| DA | Devices & Gear Attachments | CODE | - |
| GD | Gear Description | TEXT | - |
| NI | Number of Lines | QUANTITY | lines |
| NL | Nominal Length of One Net | MEASURE | m |
| NN | Number of Nets in Fleet | QUANTITY | pieces |
| QG | Quantity of Gear on Board | QUANTITY | pieces |
| MT | Model of Trawl | TEXT | - |
| TT | Twine Type | CODE | - |
| TW | Twine Thickness | MEASURE | mm |
| GO | Gear Bar Distance | MEASURE | mm |
| MK | Gear Marker | TEXT | - |

## Implementation Guidelines

### Mobile-First Design
- iPhone X resolution (375x812px)
- Touch-friendly input sizes (min 44x44px)
- Scrollable content areas
- Sticky action buttons

### Progressive Disclosure
- Show mandatory fields first
- Collapse optional fields by default
- "Show optional fields (n)" expandable section

### Validation
- Real-time validation on input
- Clear error messages
- Field-specific help tooltips (ⓘ icons)
- Prevent submission if mandatory fields missing

### Data Entry Efficiency
- Remember previous entries
- "Copy from last haul" option
- Default values from vessel profile
- Auto-complete for text fields

## Usage

### For Designers
1. Import `.bmml` files into Balsamiq Mockups
2. Use as reference for high-fidelity designs
3. Adapt layouts for your design system
4. Consider responsive breakpoints

### For Developers
1. Use wireframes to understand data requirements
2. Map field codes to database schema
3. Implement validation rules per gear type
4. Reference field types and units

### For Product Owners
1. Review user flows with stakeholders
2. Validate regulatory compliance
3. Prioritize gear types by user frequency
4. Plan phased rollout strategy

## Generator Script

The `generate_all_wireframes.py` script can regenerate all wireframes if the MDR data is updated:

```bash
python3 generate_all_wireframes.py
```

**Requirements:**
- Python 3.9+
- pandas
- openpyxl

## Related Files

- **MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx** - Source data
- **MDR_FA_GEAR_CHARACTERISTIC-IGv3-update-v2025-11-04.xlsx** - Field definitions
- **MDR_FA_DEVICE_GEAR_ATTACHMENT-IGv3-update-v2025-11-04.xls** - Attachment options
- **MDR_MESH_TYPE-IGv3-new-v2025-11-04.xlsx** - Mesh type options

## Support

For questions about:
- **Wireframe design**: Review the manually created examples (01-04)
- **MDR code lists**: Refer to the parent folder documentation
- **Regulatory requirements**: Consult EU Regulation 2025/2196
- **Implementation**: Use the generator script as reference

## Version History

- **v1.0** (2025-11-19): Initial wireframe set
  - 4 manually created examples
  - 64 auto-generated wireframes
  - Covers all 64 gear types in MDR IGv3
  - Mobile-first design
  - Full regulatory compliance

---

**Created:** November 19, 2025  
**Format:** Balsamiq Mockups (.bmml)  
**Target Platform:** Mobile (iOS/Android)  
**Regulation:** EU 2025/2196 Annexes XV & XVI
