# MDR Data Files for SSF Application

**Downloaded**: November 7, 2025  
**Source**: [EU CircaBC MDR Matrix Index](https://circabc.europa.eu/webdav/CircaBC/MARE/MDR/Information/MDR_MatrixIndex.html)  
**Purpose**: Master Data Register code lists for SSF (Small Scale Fisheries) mobile application data models

---

## 📋 Overview

This folder contains 19 essential MDR (Master Data Register) code list files downloaded from the EU's CircaBC platform. These files contain standardized fisheries codes and data structures required for the SSF mobile application to comply with EU fishing regulations.

**Total Files Downloaded**: 19  
**Total Size**: ~10 MB  
**Format**: Microsoft Excel (.xls)

---

## 🎯 Files by SSF Application Feature

### 1️⃣ **Gear Management** (Epic: Gear Management - 33 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_Gear_Type.xls` | 42 KB | Complete list of fishing gear types (nets, lines, traps, etc.) | **UC-SSF-0201**: Register new gear |
| `MDR_FA_Gear_Characteristic.xls` | 28 KB | Gear characteristics (mesh size, length, dimensions, etc.) | **UC-SSF-0201**: Gear properties and specifications |
| `MDR_FA_Device_Gear_Attachment.xls` | 29 KB | Devices that can be attached to fishing gear | **UC-SSF-0201**: Gear configuration details |
| `MDR_FA_Gear_Problem.xls` | 27 KB | Types of gear problems/losses | **UC-SSF-0405**: Lost fishing gear reporting |

**Key for Development**:
- Gear dropdowns in registration form
- Validation of gear characteristics
- Lost gear type classification

---

### 2️⃣ **Species & Catches** (Epic: Hauls - 28 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_FAO_species.xls` | 2.8 MB | Complete FAO species codes (fish, crustaceans, mollusks) | **UC-SSF-0402**: Catches and discards declaration |
| `MDR_FA_Catch_Type.xls` | 28 KB | Catch type codes (landed, discarded, used as bait, etc.) | **UC-SSF-0402**: Catch type selection |
| `MDR_FA_Reason_Discard.xls` | 27 KB | Reasons for discarding catches (undersized, damaged, etc.) | **UC-SSF-0402**: Discard reasons |
| `MDR_Fish_Presentation.xls` | 32 KB | Fish presentation codes (whole, gutted, filleted, etc.) | **UC-SSF-0602**: Landing declaration presentation |
| `MDR_Fish_Preservation.xls` | 27 KB | Preservation state codes (fresh, frozen, salted, etc.) | **UC-SSF-0602**: Landing declaration preservation |

**Key for Development**:
- Species autocomplete/search
- Catch type validation
- Discard reason selection
- Landing presentation forms

---

### 3️⃣ **Ports & Locations** (Epic: Departure/Landing - 38 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_Vessel_Port.xls` | 851 KB | All EU fishing ports with codes | **UC-SSF-0301**: Departure port selection |
| `MDR_Location.xls` | 5.4 MB | All location codes (ports, areas, zones) | **UC-SSF-0601**: Return to port selection |
| `MDR_FAO_Fishing_Area.xls` | 78 KB | FAO fishing area codes | **UC-SSF-0401**: Fishing operation location |
| `MDR_Territory.xls` | 61 KB | Territory/country codes | **UC-SSF-0303/0304**: Third party waters |

**Key for Development**:
- Port selection dropdowns
- Location autocomplete
- Fishing area validation
- Third party water identification

---

### 4️⃣ **Trip Management** (Epic: Fishing Trips - 13 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_FA_Trip_Id_Type.xls` | 27 KB | Trip identifier types | **Fishing Trips**: Trip ID management |
| `MDR_FA_Reason_Departure.xls` | 27 KB | Reasons for departure from port | **UC-SSF-0301**: Departure declaration |
| `MDR_FA_Reason_Arrival.xls` | 27 KB | Reasons for arrival at port | **UC-SSF-0601**: Return to port reasons |

**Key for Development**:
- Trip lifecycle management
- Departure/arrival reason codes
- Trip identifier validation

---

### 5️⃣ **Effort Zones & Waters** (Epic: Third Party Waters - 22 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_Effort_Zone.xls` | 35 KB | Fishing effort zone codes | **UC-SSF-0303/0304**: Entry/exit effort zones |

**Key for Development**:
- Effort zone selection
- Entry/exit event validation
- Zone-based restrictions

---

### 6️⃣ **Data Exchange (FLUX)** (Epic: Data Exchange FMC - 21 SP)

| File | Size | Purpose | SSF Feature Mapping |
|------|------|---------|-------------------|
| `MDR_FLUX_FA_Type.xls` | 29 KB | FLUX Fishing Activity message types | **Data Exchange**: Message type codes |
| `MDR_FLUX_GP_Party.xls` | 30 KB | FLUX party codes (member states, authorities) | **Data Exchange**: Sender/recipient codes |

**Key for Development**:
- FMC data exchange messages
- Message type validation
- Party identification for data exchange

---

## 🗂️ File Structure & Content

All MDR files follow a consistent Excel format:

### Common Columns
- **Code**: The standardized code (e.g., "GN", "FRE", "COD")
- **Description**: Full description in multiple languages (EN, FR, ES, etc.)
- **Start Date**: When the code became valid
- **End Date**: When the code became invalid (if applicable)
- **Additional Metadata**: Varies by file type

### Example: MDR_Gear_Type.xls
```
Code | Description (EN) | Description (FR) | Start Date | End Date
-----|-----------------|------------------|------------|----------
GN   | Gillnets        | Filets maillants | 2010-01-01 | NULL
LL   | Longlines       | Palangres        | 2010-01-01 | NULL
PS   | Purse seines    | Sennes coulissantes | 2010-01-01 | NULL
```

---

## 🔧 Technical Implementation Guide

### 1. Data Model Creation

Each MDR file should be converted to a Flutter/Dart data model:

```dart
// Example: Gear Type Model
class GearType {
  final String code;
  final Map<String, String> descriptions; // Multi-language
  final DateTime startDate;
  final DateTime? endDate;
  
  bool get isValid => endDate == null || DateTime.now().isBefore(endDate!);
}
```

### 2. Database Schema

**Recommended Approach**: Store MDR data in local SQLite database for offline access

```sql
CREATE TABLE gear_types (
  code TEXT PRIMARY KEY,
  description_en TEXT NOT NULL,
  description_fr TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  is_active BOOLEAN DEFAULT 1
);
```

### 3. Data Loading Strategy

**Option A**: Bundle with app (recommended for MVP)
- Convert XLS to JSON/CSV during build
- Load into SQLite on first app launch
- ~10 MB storage required

**Option B**: Remote sync
- Store on backend server
- Periodic updates via API
- Better for large datasets (Location, Species)

### 4. UI Components

Create reusable dropdown/autocomplete components:

```dart
// Example: Gear Type Selector
class GearTypeSelector extends StatelessWidget {
  Widget build(BuildContext context) {
    return FutureBuilder<List<GearType>>(
      future: _loadGearTypes(),
      builder: (context, snapshot) {
        return DropdownButton<GearType>(
          items: snapshot.data?.map((gear) => 
            DropdownMenuItem(
              value: gear,
              child: Text(gear.getDescription(locale))
            )
          ).toList(),
          onChanged: (value) => onGearSelected(value),
        );
      },
    );
  }
}
```

---

## 📊 Data Size Analysis

| Category | Files | Total Size | Records (approx) |
|----------|-------|------------|------------------|
| **Large** (>500 KB) | 3 | 9.1 MB | 50,000+ |
| **Medium** (50-500 KB) | 2 | 893 KB | 5,000-10,000 |
| **Small** (<50 KB) | 14 | 450 KB | <1,000 each |

### Large Files Require Special Handling:
1. **MDR_Location.xls** (5.4 MB) - Consider pagination/lazy loading
2. **MDR_FAO_species.xls** (2.8 MB) - Implement search/filter
3. **MDR_Vessel_Port.xls** (851 KB) - Group by country for better UX

---

## 🌍 Multi-Language Support

All MDR files include translations in multiple EU languages:
- 🇬🇧 English (EN)
- 🇫🇷 French (FR)
- 🇪🇸 Spanish (ES)
- 🇩🇪 German (DE)
- 🇮🇹 Italian (IT)
- 🇵🇹 Portuguese (PT)
- ...and more

### Implementation Strategy:
```dart
class MDRItem {
  final String code;
  final Map<String, String> descriptions;
  
  String getDescription(String locale) {
    return descriptions[locale] ?? descriptions['EN'] ?? code;
  }
}
```

---

## 🔄 Data Update Strategy

### MDR Data Versioning
- MDR codes are updated periodically by EU authorities
- Each file includes a **History Log** on CircaBC
- **Recommendation**: Check for updates quarterly

### Update Process:
1. Download latest MDR files from CircaBC
2. Compare version numbers/dates
3. Update app's embedded data
4. Release app update or push data update

### Version Tracking:
```json
{
  "mdr_version": "2025-11-07",
  "files": {
    "gear_type": "v1.5",
    "fao_species": "v2.3",
    "vessel_port": "v1.8"
  }
}
```

---

## 🔗 Related Documentation

### SSF Project Documents
- `PROJECT_CONTEXT.md` - Project overview and context
- `DESCOPING_STRATEGY_V2.md` - Feature scope decisions
- `Backlog SSF ALT - V003.xlsx` - Complete backlog with MDR references

### EU Regulation Documents
- `/SSF DOCS/2025_Guidelines_for_partners.pdf` - Partner guidelines
- `/SSF DOCS/DOCS VARY/SSF_Law_18_09_25.pdf` - Legal framework
- `/SSF DOCS/DOCS VARY/IFDM_Rec_191-Impl_Doc_Vessel_v3.3 - adopted.pdf` - Implementation docs

### Use Cases
- All use cases in `/SSF DOCS/USE CASES/` reference MDR codes
- Example: `UC-SSF-0201_Register new gear.pdf` uses `MDR_Gear_Type.xls`

---

## 🎯 Priority for PI 01-02 Development

### 🔴 **Critical for PI 01** (Nov 2025 - Feb 2026)
1. ✅ `MDR_Gear_Type.xls` - Gear Management (Sprint 7-8)
2. ✅ `MDR_FA_Gear_Characteristic.xls` - Gear Management (Sprint 7-8)

### 🟡 **Critical for PI 02** (Mar - May 2026)
3. ✅ `MDR_Vessel_Port.xls` - Departure Declaration (Sprint 7-8)
4. ✅ `MDR_FAO_species.xls` - Hauls (Sprint 9-10)
5. ✅ `MDR_FA_Catch_Type.xls` - Hauls (Sprint 9-10)
6. ✅ `MDR_Location.xls` - Multiple features (Sprint 7-10)

### 🟢 **Critical for PI 03** (Jun - Aug 2026)
7. ✅ `MDR_FA_Reason_Discard.xls` - Hauls (Sprint 9-10)
8. ✅ `MDR_FA_Trip_Id_Type.xls` - Fishing Trips (Sprint 9-10)
9. ✅ `MDR_FAO_Fishing_Area.xls` - Hauls (Sprint 9-10)

### 🔵 **Critical for PI 04** (Sep - Dec 2026)
10. ✅ `MDR_Fish_Presentation.xls` - Landing Declaration (Sprint 15-16)
11. ✅ `MDR_FLUX_FA_Type.xls` - Data Exchange (Sprint 17-18)
12. ✅ `MDR_Effort_Zone.xls` - Third Party Waters (Sprint 15-16)

---

## 🧪 Testing Requirements

### Data Validation Tests
- ✅ Verify all codes load correctly
- ✅ Check multi-language support
- ✅ Validate date ranges (start/end dates)
- ✅ Test inactive code filtering

### Integration Tests
- ✅ Gear selection with MDR_Gear_Type
- ✅ Port selection with MDR_Vessel_Port
- ✅ Species autocomplete with MDR_FAO_species
- ✅ Catch type validation with MDR_FA_Catch_Type

### Performance Tests
- ✅ Large file loading (MDR_Location - 5.4 MB)
- ✅ Species search with 10,000+ records
- ✅ Offline access speed
- ✅ Memory usage with all MDR data loaded

---

## 📞 Support & Updates

### MDR Data Source
- **Website**: https://circabc.europa.eu/
- **Direct Link**: [MDR Matrix Index](https://circabc.europa.eu/webdav/CircaBC/MARE/MDR/Information/MDR_MatrixIndex.html)
- **Updates**: Check quarterly for new versions
- **History Log**: [MDRUpdates.xls](https://circabc.europa.eu/d/a/workspace/SpacesStore/a5ca768b-9b4e-4c9b-9fc9-95211a860ee3/MDRUpdates.xls)

### Technical Questions
- Contact DG MARE Data Management working group
- Reference FLUX standards documentation
- Check EU-ERS and NOR-ERS specifications

---

## 📝 Notes

### Important Considerations
1. **Regulatory Compliance**: All codes used in SSF app must come from official MDR files
2. **No Manual Changes**: Never modify MDR codes manually - always use official sources
3. **Version Control**: Track which MDR version is used in each app release
4. **Backward Compatibility**: Handle deprecated codes gracefully in production

### Known Issues
- Some MDR files may have encoding issues (UTF-8 vs ISO-8859-1)
- Large files (Location, Species) may need chunked loading on older devices
- Occasional duplicate entries in older MDR versions - filter by latest start_date

---

**Last Updated**: November 7, 2025  
**Next Review**: February 2026 (before PI 02 Sprint 7)  
**Maintained By**: SSF Development Team
