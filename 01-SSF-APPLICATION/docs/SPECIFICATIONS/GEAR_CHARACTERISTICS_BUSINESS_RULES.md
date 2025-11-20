# Business Rules: Fishing Gear Characteristics

**Document Owner**: Product Manager  
**Last Updated**: November 14, 2025  
**Version**: 1.0  
**Status**: Draft for Review

---

## 1. Overview & Context

### Purpose
This document defines the business rules for fishing gear characteristics registration in the SSF mobile application. It specifies which characteristics are required for each gear type and how the system should validate and handle this data.

### Scope
- Gear characteristic codes (MDR reference data)
- Gear type-specific requirements
- Form validation rules
- Dynamic form behavior
- Data entry guidelines

### Regulatory Context
Based on EU fishing regulation requirements and MDR (Master Data Register) standards for gear registration and reporting.

---

## 2. Gear Characteristic Codes Reference (MDR)

The following characteristic codes are defined in the MDR (Master Data Register) and used across the EU:

| Code | Name | Data Type | Description | Valid From |
|------|------|-----------|-------------|------------|
| **ME** | Mesh size | MEASURE | Size of mesh openings in the net | 1989-01-01 |
| **GD** | Gear description | TEXT | Free text description of the gear | 1989-01-01 |
| **DA** | Devices and gear attachments | CODE | Additional devices attached to gear | 2019-06-04 |
| **GO** | Gear bar distance | MEASURE | Distance between bars in the gear | 1989-01-01 |
| **TW** | Twine thickness | MEASURE | Thickness of twine used | 2020-01-01 |
| **TT** | Twine type | TEXT | Type/material of twine | 1989-01-01 |
| **MK** | Gear Marker | TEXT | Identification marking on gear | 1989-01-01 |
| **MS** | Mesh type | TEXT | Type of mesh construction | 1989-01-01 |
| **MT** | Model of trawl | TEXT | Specific trawl model designation | 1989-01-01 |
| **GM** | Gear dimension (length/width) | MEASURE | Length or width in metres | 1989-01-01 |
| **HE** | Height of the net | MEASURE | Net height in metres | 1989-01-01 |
| **GN** | Gear dimension by number | QUANTITY | Number of units (trawls, beams, etc.) | 1989-01-01 |
| **NI** | Number of lines | QUANTITY | Count of fishing lines | 1989-01-01 |
| **NL** | Nominal length of one net | MEASURE | Length of single net in fleet | 1989-01-01 |
| **NN** | Number of nets in fleet | QUANTITY | Total nets in the fleet | 1989-01-01 |
| **QG** | Quantity of gear on board | QUANTITY | Total gear units on vessel | 1989-01-01 |

### Data Type Definitions
- **MEASURE**: Numeric value with unit (metres, millimetres, etc.)
- **QUANTITY**: Integer count
- **TEXT**: Free text string
- **CODE**: Predefined code from MDR reference list

---

## 3. Gear Categories and Types

### Main Categories (9 total)

1. **TRAWLS** (10 types)
2. **SEINES** (6 types)
3. **SURROUNDING NETS** (5 types)
4. **LIFT NETS** (4 types)
5. **FALLING GEAR** (3 types)
6. **DREDGES** (4 types)
7. **GILLNETS AND ENTANGLING NETS** (8 types)
8. **TRAPS** (8 types)
9. **HOOKS AND LINES** (8 types)
10. **MISCELLANEOUS GEARS** (9 types)

**Total Gear Types**: 72

---

## 4. Gear Type-Specific Requirements Matrix

### 4.1 TRAWLS Category

#### Single Trawls
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Bottom otter trawl | OTB | Model of trawl (optional) + Perimeter of opening (mandatory) |
| Nephrops trawl | TBN | Model of trawl (optional) + Perimeter of opening (mandatory) |
| Shrimp trawl | TBS | Model of trawl (optional) + Perimeter of opening (mandatory) |
| Bottom pair trawl | PTB | Model of trawl (optional) + Perimeter of opening (mandatory) |

**Business Rules**:
- Model of trawl (MT) is OPTIONAL
- Perimeter of opening (GM) is MANDATORY - measured in metres

#### Beam Trawls
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Beam trawl | TBB | Beam length of each beam + Number of beams towed |

**Business Rules**:
- Beam length (GM) is MANDATORY - per beam
- Number of beams (GN) is MANDATORY

#### Multiple Trawls
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Twin bottom otter trawl | OTT | Model (optional) + Perimeter per trawl + Number of trawls |
| Multiple bottom otter trawl | OTP | Model (optional) + Perimeter per trawl + Number of trawls |
| Bottom trawls (not specified) | TB | Model (optional) + Perimeter per trawl + Number of trawls |

**Business Rules**:
- Model of trawl (MT) is OPTIONAL
- Perimeter of opening (GM) is MANDATORY - per individual trawl
- Number of trawls (GN) is MANDATORY

#### Mid-water Trawls
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Mid-water otter trawl | OTM | Model of trawl (optional) + Perimeter of opening |
| Mid-water pair trawl | PTM | Model of trawl (optional) + Perimeter of opening |

**Business Rules**:
- Model of trawl (MT) is OPTIONAL
- Perimeter of opening (GM) is MANDATORY

---

### 4.2 SEINES Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Danish anchor seine | SDN | Overall length + Maximum height of seine lines |
| Scottish seine (fly dragging) | SSC | Overall length + Maximum height of seine lines |
| Pair seine | SPR | Overall length + Maximum height of seine lines |
| Seine nets (not specified) | SX | Overall length + Maximum height of seine lines |
| Boat or vessel seine | SV | Overall length + Maximum height of seine lines |
| Beach seine | BS | Overall length + Maximum height of seine lines |

**Business Rules**:
- Overall length (GM) is MANDATORY
- Maximum height (HE) is MANDATORY
- Both measured in metres

---

### 4.3 SURROUNDING NETS Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Purse seine | PS | Length + (Maximum) height of nets |
| One boat operated purse seine | PS1 | Length + (Maximum) height of nets |
| Two boat operated purse seine | PS2 | Length + (Maximum) height of nets |
| Without purse lines (lampara) | LA | Length + (Maximum) height of nets |
| Surrounding nets (not specified) | SUX | Length + (Maximum) height of nets |

**Business Rules**:
- Length (GM) is MANDATORY
- Maximum height (HE) is MANDATORY
- Both measured in metres

---

### 4.4 LIFT NETS Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Portable lift nets | LNP | Maximum perimeter per net + Number of nets (if >1) |
| Boat-operated lift nets | LNB | Maximum perimeter per net + Number of nets (if >1) |
| Shore-operated stationary lift nets | LNS | Maximum perimeter per net + Number of nets (if >1) |
| Lift nets (not specified) | LN | Maximum perimeter per net + Number of nets (if >1) |

**Business Rules**:
- Maximum perimeter (GM) is MANDATORY - per individual net
- Number of nets (GN) is MANDATORY if more than 1 net used
- Number of nets (GN) is OPTIONAL if only 1 net used

---

### 4.5 FALLING GEAR Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Cast nets | FCN | Maximum perimeter per net/device + Number (if >1) |
| Cover pots/Lantern nets | FCO | Maximum perimeter per net/device + Number (if >1) |
| Falling gear (not specified) | FG | Maximum perimeter per net/device + Number (if >1) |

**Business Rules**:
- Maximum perimeter (GM) is MANDATORY - per device
- Number of devices (GN) is MANDATORY if more than 1 used
- Number of devices (GN) is OPTIONAL if only 1 used

---

### 4.6 DREDGES Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Towed dredge | DRB | Width of each dredge + Number of dredges (if >1) |
| Hand dredge | DRH | Width of each dredge + Number of dredges (if >1) |
| Mechanized dredge | DRM | Width of each dredge + Number of dredges (if >1) |
| Dredge (not specified) | DRX | Width of each dredge + Number of dredges (if >1) |

**Business Rules**:
- Width (GM) is MANDATORY - per individual dredge
- Number of dredges (GN) is MANDATORY if more than 1 used
- Number of dredges (GN) is OPTIONAL if only 1 used

---

### 4.7 GILLNETS AND ENTANGLING NETS Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Gillnets (not specified) | GN | Overall length(¹) + Height of nets |
| Gillnets anchored (set) | GNS | Overall length(¹) + Height of nets |
| Gillnets (drift) | GND | Overall length(¹) + Height of nets |
| Gillnets (circling) | GNC | Overall length(¹) + Height of nets |
| Gillnets fixed (on stakes) | GNF | Overall length(¹) + Height of nets |
| Combined gillnets-trammel nets | GTN | Overall length(¹) + Height of nets |
| Trammel nets | GTR | Overall length(¹) + Height of nets |
| Gillnets and entangling nets (not specified) | GEN | Overall length(¹) + Height of nets |

**Business Rules**:
- Overall length (GM) is MANDATORY
- Height (HE) is MANDATORY
- Both measured in metres
- (¹) See "Aggregated Reporting Rule" below

---

### 4.8 TRAPS Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Pots | FPO | Number of pots (e.g., creels) used(¹) |
| Fyke nets | FYK | Overall length + Height of wings/leaders per net + Number of nets |
| Stow nets | FSN | Length + Height of frame |
| Barriers, fences, weirs | FWR | Total length + Height |
| Aerial traps | FAR | Length + Height underwater + Length + Height aerial |
| Stationary uncovered pound nets | FPN | Overall length + Height of wings and leaders |
| Traps (not specified) | FIX | Dimensions and description + Number of gears |

**Business Rules - Pots (FPO)**:
- Number of pots (GN) is MANDATORY
- (¹) See "Aggregated Reporting Rule" below

**Business Rules - Fyke Nets (FYK)**:
- Overall length (GM) is MANDATORY - per net
- Height (HE) is MANDATORY - of wings and leaders per net
- Number of fyke nets (GN) is MANDATORY

**Business Rules - Stow Nets (FSN)**:
- Length (GM) is MANDATORY
- Height (HE) is MANDATORY

**Business Rules - Barriers/Fences/Weirs (FWR)**:
- Total length (GM) is MANDATORY
- Height (HE) is MANDATORY

**Business Rules - Aerial Traps (FAR)**:
- 4 measurements MANDATORY:
  - Length underwater (GM)
  - Height underwater (HE)
  - Length aerial (GM)
  - Height aerial (HE)
- System must capture and distinguish between underwater and aerial measurements

**Business Rules - Stationary Pound Nets (FPN)**:
- Overall length (GM) is MANDATORY
- Height (HE) is MANDATORY - of wings and leaders

**Business Rules - Traps Not Specified (FIX)**:
- Dimensions (GM) is MANDATORY
- Description (GD) is MANDATORY - free text
- Number of gears (GN) is MANDATORY

---

### 4.9 HOOKS AND LINES Category

#### Handlines and Pole Lines
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Handlines and pole lines (hand operated) | LHP | Total number of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Lines and pole lines (mechanised) | LHM | Total number of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Vertical lines | LVT | Total number of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Trolling lines | LTL | Total number of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Hooks and lines (not specified) | LX | Total number of lines(¹) + Total number of hooks(¹) + Size of hooks |

**Business Rules**:
- Total number of lines (NI) is MANDATORY
- Total number of hooks (GN) is MANDATORY
- Size of hooks (ME) is MANDATORY
- (¹) See "Aggregated Reporting Rule" below

#### Longlines
| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Set longlines | LLS | Overall length of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Drifting longlines | LLD | Overall length of lines(¹) + Total number of hooks(¹) + Size of hooks |
| Longlines (not specified) | LL | Overall length of lines(¹) + Total number of hooks(¹) + Size of hooks |

**Business Rules**:
- Overall length of lines (GM) is MANDATORY
- Total number of hooks (GN) is MANDATORY
- Size of hooks (ME) is MANDATORY
- (¹) See "Aggregated Reporting Rule" below

---

### 4.10 MISCELLANEOUS GEARS Category

| Gear Type | Code | Required Dimensions/Characteristics |
|-----------|------|-------------------------------------|
| Harpoons | HAR | Dimensions and description + Number of gears |
| Hand implements | MHI | Dimensions and description + Number of gears |
| Pumps | MPM | Dimensions and description + Number of gears |
| Pushnets | MPN | Dimensions and description + Number of gears |
| Scoopnets | MSP | Dimensions and description + Number of gears |
| Drive-in nets | MDR | Dimensions and description + Number of gears |
| Diving | MDV | Dimensions and description + Number of gears |
| Harvesting machines (not specified) | HMX | Dimensions and description + Number of gears |
| Gear (not specified) | MIS | Dimensions and description + Number of gears |

**Business Rules - ALL Miscellaneous Gears**:
- Dimensions (GM) is MANDATORY
- Description (GD) is MANDATORY - free text field
- Number of gears (GN) is MANDATORY

---

## 5. Critical Business Rules

### 5.1 Aggregated Reporting Rule

**Rule**: When the fisher is reporting aggregated catches covering multiple fishing operations (hauls), the information on gear dimensions must be **cumulated** (summed).

**Applies to**:
- Gillnets overall length (¹)
- Number of pots (¹)
- Number of lines (¹)
- Number of hooks (¹)
- Overall length of lines (¹)

**Example**:
- Haul 1: Used 50 pots
- Haul 2: Used 30 pots
- Haul 3: Used 45 pots
- **Reported value**: 125 pots (50 + 30 + 45)

**Implementation Note**: System should allow fishers to report per-haul OR cumulative, with clear indication of which method is being used.

---

### 5.2 Optional vs Mandatory Characteristics

#### MANDATORY Characteristics
- Must be provided before gear can be registered
- System must prevent submission if missing
- Display clear validation error messages

#### OPTIONAL Characteristics
- Can be left blank
- System should indicate they are optional in UI
- No validation errors if omitted

**Characteristic Type Matrix**:

| Characteristic | Mandatory For | Optional For |
|----------------|---------------|--------------|
| Model of trawl (MT) | None | All trawl types |
| Perimeter/Length (GM) | Most gear types | None |
| Height (HE) | Seines, Nets, Traps | None |
| Number of units (GN) | Multiple gear types | Single unit gears |
| Number of lines (NI) | Hooks & lines | None |
| Number of hooks (GN) | Hooks & lines | None |
| Size of hooks (ME) | Hooks & lines | None |
| Description (GD) | Miscellaneous gears, FIX | All other types |

---

### 5.3 Dynamic Form Behavior

**Rule**: The gear registration form must display **only the characteristics required** for the selected gear type.

**Implementation**:
1. Fisher selects gear type from dropdown
2. System identifies gear type code (e.g., "OTB")
3. System looks up required characteristics for that code
4. System dynamically shows/hides form fields based on requirements
5. Only required fields are marked as mandatory
6. Optional fields are clearly marked as optional

**Example Flow**:
```
Fisher selects: "Bottom otter trawl (OTB)"
↓
System displays:
- Model of trawl [Optional text field]
- Perimeter of opening [Mandatory number field] (metres)
↓
System hides all other characteristic fields
```

---

### 5.4 Unit of Measurement Rules

**Default Units by Measurement Type**:
- **Length/Width/Height/Perimeter**: Metres (m)
- **Mesh Size**: Millimetres (mm)
- **Thickness**: Millimetres (mm)
- **Quantities**: Integer count (no decimals)

**Validation Rules**:
- Length measurements: Must be positive decimal numbers
- Quantities: Must be positive integers
- Mesh size: Must be positive decimal numbers
- No negative values allowed
- Zero values not permitted for mandatory fields

---

### 5.5 Data Persistence Rules

**On Gear Registration**:
1. All mandatory characteristics must be provided
2. System validates data types and ranges
3. Data is saved to local database (offline-first)
4. Sync with backend when connection available
5. Gear receives unique identifier (UUID)

**On Gear Modification**:
1. Existing characteristics can be updated
2. Mandatory fields cannot be cleared
3. Validation rules still apply
4. Modification timestamp recorded
5. Original creation date preserved

---

## 6. Validation Rules

### 6.1 Data Type Validation

| Data Type | Validation Rule | Error Message |
|-----------|----------------|---------------|
| MEASURE | Must be positive decimal number | "Please enter a valid measurement greater than 0" |
| QUANTITY | Must be positive integer | "Please enter a whole number greater than 0" |
| TEXT | Max 500 characters | "Description must be less than 500 characters" |
| CODE | Must match MDR code list | "Please select a valid option from the list" |

### 6.2 Business Logic Validation

**Rule 1: Multiple Unit Gears**
- IF gear requires "number of units" AND number > 1
- THEN dimensions must be specified "per unit"
- Display helper text: "Specify dimension for each individual [gear type]"

**Rule 2: Aggregated Reporting**
- IF reporting cumulative catches across hauls
- THEN dimensions are summed totals
- Display helper text: "Total across all hauls in this reporting period"

**Rule 3: Conditional Mandatory Fields**
- IF gear type has "(if >1)" condition
- AND user enters number > 1
- THEN related dimension becomes MANDATORY

Example:
```
Gear: Towed dredge (DRB)
IF number of dredges > 1
THEN width per dredge is MANDATORY
```

### 6.3 Cross-Field Validation

**Rule 1: Aerial Traps (FAR)**
- Must have 4 dimensions provided
- Underwater length + underwater height + aerial length + aerial height
- All four must be present to pass validation

**Rule 2: Multiple Trawls**
- IF gear type = OTT, OTP, or TB
- THEN perimeter AND number of trawls both MANDATORY

**Rule 3: Fyke Nets (FYK)**
- Length, height, AND number of nets all MANDATORY

---

## 7. Data Entry Guidelines for Users

### 7.1 General Instructions

**For Fishers**:
1. Select your gear type from the dropdown list
2. Fill in all required fields marked with *
3. Optional fields can help with record-keeping but are not mandatory
4. Use the correct unit of measurement (shown next to each field)
5. For multiple units of the same gear, specify dimensions per individual unit
6. Save draft if you need to come back later

### 7.2 Common Scenarios

**Scenario 1: Single Gear**
```
Gear: Bottom otter trawl (OTB)
Action: Enter the perimeter of the trawl opening in metres
Optionally: Enter the model name if you know it
```

**Scenario 2: Multiple Identical Gears**
```
Gear: Beam trawl (TBB)
Action: 
- Enter the length of ONE beam
- Enter the total number of beams you're using
```

**Scenario 3: Reporting Across Multiple Hauls**
```
Gear: Pots (FPO)
Action:
- Add up all pots used across all hauls
- Enter the TOTAL number
Example: 50 pots + 30 pots + 45 pots = 125 pots
```

**Scenario 4: Complex Gear (Aerial Traps)**
```
Gear: Aerial traps (FAR)
Action: Enter FOUR measurements:
1. Length of trap underwater (metres)
2. Height of trap underwater (metres)
3. Length of trap above water (metres)
4. Height of trap above water (metres)
```

---

## 8. Error Handling

### 8.1 Validation Error Messages

**Missing Mandatory Field**:
```
"[Field name] is required for [Gear type name]. Please provide a value."
```

**Invalid Data Type**:
```
"[Field name] must be a valid [number/whole number/text]. Please check your entry."
```

**Out of Range Value**:
```
"[Field name] must be greater than 0. Please enter a positive value."
```

**Conditional Field Missing**:
```
"When using multiple [gear units], you must specify the dimension for each unit."
```

### 8.2 System Error Handling

**If MDR reference data fails to load**:
- Display cached/offline version
- Show warning: "Using offline data. Sync when connection available."
- Allow gear registration to continue

**If validation rules cannot be determined**:
- Fall back to basic validation (data type only)
- Log error for investigation
- Allow user to proceed with warning

---

## 9. Technical Implementation Notes

### 9.1 Data Model

**Gear Characteristic Record**:
```json
{
  "gear_id": "uuid",
  "characteristic_code": "ME|GD|DA|...",
  "characteristic_name": "Mesh size",
  "value_numeric": 120.5,
  "value_text": null,
  "unit": "mm",
  "is_mandatory": true,
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

### 9.2 Dynamic Form Configuration

System should maintain a configuration mapping:
```json
{
  "OTB": {
    "name": "Bottom otter trawl",
    "category": "TRAWLS",
    "characteristics": [
      {
        "code": "MT",
        "name": "Model of trawl",
        "data_type": "TEXT",
        "mandatory": false,
        "unit": null
      },
      {
        "code": "GM",
        "name": "Perimeter of opening",
        "data_type": "MEASURE",
        "mandatory": true,
        "unit": "metres"
      }
    ]
  }
}
```

### 9.3 Frontend Validation Sequence

1. On field blur: Validate individual field
2. On form submission: Validate all mandatory fields present
3. On form submission: Validate data types
4. On form submission: Run cross-field validation rules
5. If any validation fails: Prevent submission and show errors
6. If all validation passes: Proceed with save

---

## 10. Testing Scenarios

### 10.1 Basic Validation Tests

| Test Case | Input | Expected Result |
|-----------|-------|----------------|
| TC-01 | Select OTB, enter perimeter = 50m | Accept |
| TC-02 | Select OTB, leave perimeter blank | Reject with error |
| TC-03 | Select OTB, enter perimeter = -10m | Reject with error |
| TC-04 | Select OTB, enter perimeter = 0m | Reject with error |
| TC-05 | Select OTB, enter model text (optional) | Accept |
| TC-06 | Select OTB, leave model blank | Accept |

### 10.2 Complex Validation Tests

| Test Case | Input | Expected Result |
|-----------|-------|----------------|
| TC-10 | Select DRB, enter 3 dredges, enter width per dredge | Accept |
| TC-11 | Select DRB, enter 3 dredges, leave width blank | Reject with error |
| TC-12 | Select DRB, enter 1 dredge, leave width blank | Reject with error (width always mandatory) |

### 10.3 Dynamic Form Tests

| Test Case | Action | Expected Result |
|-----------|--------|----------------|
| TC-20 | Change gear type from OTB to LLS | Form fields update dynamically |
| TC-21 | Select gear type with 2 fields | Only 2 characteristic fields shown |
| TC-22 | Select gear type with optional field | Optional field clearly marked |

---

## 11. Future Considerations

### 11.1 Potential Enhancements

1. **Pre-filled Templates**: Save common gear configurations as templates
2. **Photo Attachment**: Allow photo upload of gear for verification
3. **Gear History**: Track changes to gear characteristics over time
4. **Fleet Management**: Manage multiple vessels and their gear inventories
5. **QR Code Scanning**: Scan gear markings for auto-population

### 11.2 Regulatory Updates

- Monitor MDR updates from EU for new characteristic codes
- Track changes to gear type requirements
- Update validation rules when regulations change
- Maintain backward compatibility with historical data

---

## 12. Document Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-14 | Product Manager | Initial draft for PI 02 Sprint preparation |

---

## 13. References

- **MDR_FA_Gear_Characteristic.xls**: Master data register for characteristic codes
- **fishing gear categorisation.xlsx**: EU gear type requirements (Annex XVI)
- **UC-SSF-0201_Register new gear.pdf**: Use case documentation
- **SSF_Law_18_09_25.pdf**: EU fishing regulation 2028

---

## 14. Approval & Review

**Document Status**: Draft for Technical Review

**Required Approvals**:
- [ ] Tech Lead Review
- [ ] Business Analyst Review  
- [ ] Client/DG MARE Review
- [ ] Development Team Review

**Review Notes**: 
_[To be added after review sessions]_

---

*This document is part of the Gear Management epic (PI 02) and supports user stories SSF-141 through SSF-152.*
