# Gear Registration Data Model

**Purpose**: Visual and technical specification of the two-level data structure for gear registration  
**Version**: 1.0  
**Created**: November 14, 2025  
**Status**: Ready for Implementation

---

## Overview

The gear registration system uses a **two-level hierarchical data model** that separates gear sets (parent) from individual gear units (children). This structure supports both simple gear types (single record) and complex multi-unit gear types (parent + multiple children).

---

## Data Model Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     VESSEL (existing)                        │
│  - id (UUID)                                                 │
│  - vessel_name                                               │
│  - cfr (vessel registration)                                 │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ 1:N (One vessel has many gear sets)
                 ↓
┌─────────────────────────────────────────────────────────────┐
│               GEAR_SETS (Level 1 - Parent)                   │
├─────────────────────────────────────────────────────────────┤
│  PRIMARY KEY: id (UUID)                                      │
│  FOREIGN KEY: vessel_id → vessels.id                         │
│                                                               │
│  Metadata:                                                   │
│  - gear_type_code (VARCHAR(10))      e.g., "LLS", "FPO"     │
│  - gear_name (VARCHAR(255))          e.g., "Longline 1"     │
│  - all_units_identical (BOOLEAN)     default: false         │
│                                                               │
│  Characteristics (JSONB):                                    │
│  - Flexible schema per gear type                             │
│  - Example FPO: {"number_of_pots": 50}                      │
│  - Example LLS: {"number_of_lines": 3}                      │
│                                                               │
│  Timestamps:                                                 │
│  - created_at (TIMESTAMP)                                    │
│  - updated_at (TIMESTAMP)                                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ 1:N (One gear set has many units)
                 │ (OPTIONAL - only for multi-unit gear types)
                 ↓
┌─────────────────────────────────────────────────────────────┐
│              GEAR_UNITS (Level 2 - Children)                 │
├─────────────────────────────────────────────────────────────┤
│  PRIMARY KEY: id (UUID)                                      │
│  FOREIGN KEY: gear_set_id → gear_sets.id (ON DELETE CASCADE)│
│                                                               │
│  Unit Identification:                                        │
│  - unit_number (INTEGER)             1, 2, 3, ...           │
│                                                               │
│  Characteristics (JSONB):                                    │
│  - Per-unit measurements                                     │
│  - Example TBB: {"beam_length_m": 8.0}                      │
│  - Example LLS: {                                            │
│      "length_m": 1400,                                       │
│      "number_of_hooks": 50,                                  │
│      "hook_size": 4                                          │
│    }                                                          │
│                                                               │
│  Timestamps:                                                 │
│  - created_at (TIMESTAMP)                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Model Patterns by Gear Type

### Pattern A: Simple Count Only (No Units)

**Example**: Pots (FPO)

```
gear_sets
├─ id: "550e8400-e29b-41d4-a716-446655440001"
├─ vessel_id: "vessel-123"
├─ gear_type_code: "FPO"
├─ gear_name: "My Pots"
├─ all_units_identical: false (N/A)
├─ characteristics: {"number_of_pots": 50}
└─ created_at: 2025-11-14T18:00:00Z

gear_units: [] (empty - no child records)
```

**Rationale**: Pots are tracked as a total count only. No need to track individual pots.

---

### Pattern B: Dual Measurements (No Units)

**Example**: Gillnets Anchored (GNS)

```
gear_sets
├─ id: "550e8400-e29b-41d4-a716-446655440002"
├─ vessel_id: "vessel-123"
├─ gear_type_code: "GNS"
├─ gear_name: "Gillnet Set 1"
├─ all_units_identical: false (N/A)
├─ characteristics: {
│    "overall_length_m": 100.0,
│    "height_m": 2.5
│  }
└─ created_at: 2025-11-14T18:00:00Z

gear_units: [] (empty - measurements are gear-level, not per-unit)
```

**Rationale**: Gillnet registered as one piece with two measurements. Not broken into sub-units.

---

### Pattern C: Multi-Unit with Single Characteristic

**Example**: Beam Trawl (TBB) - 5 beams, all identical 8m

```
gear_sets
├─ id: "550e8400-e29b-41d4-a716-446655440003"
├─ vessel_id: "vessel-123"
├─ gear_type_code: "TBB"
├─ gear_name: "Beam Trawl Set"
├─ all_units_identical: true
├─ characteristics: {"number_of_beams": 5}
└─ created_at: 2025-11-14T18:00:00Z
    │
    └─ gear_units (5 records):
       ├─ unit 1: {"beam_length_m": 8.0}
       ├─ unit 2: {"beam_length_m": 8.0}
       ├─ unit 3: {"beam_length_m": 8.0}
       ├─ unit 4: {"beam_length_m": 8.0}
       └─ unit 5: {"beam_length_m": 8.0}
```

**Rationale**: Each beam tracked separately to support future selective usage reporting ("used beams 1-3").

---

### Pattern D: Multi-Unit with Multiple Characteristics

**Example**: Set Longlines (LLS) - 3 lines, all identical

```
gear_sets
├─ id: "550e8400-e29b-41d4-a716-446655440004"
├─ vessel_id: "vessel-123"
├─ gear_type_code: "LLS"
├─ gear_name: "Longline 1"
├─ all_units_identical: true
├─ characteristics: {"number_of_lines": 3}
└─ created_at: 2025-11-14T18:00:00Z
    │
    └─ gear_units (3 records):
       ├─ unit 1: {
       │    "length_m": 1400.0,
       │    "number_of_hooks": 50,
       │    "hook_size": 4
       │  }
       ├─ unit 2: {
       │    "length_m": 1400.0,
       │    "number_of_hooks": 50,
       │    "hook_size": 4
       │  }
       └─ unit 3: {
            "length_m": 1400.0,
            "number_of_hooks": 50,
            "hook_size": 4
          }
```

**Rationale**: Each line tracked with multiple characteristics. Enables precise reporting and selective usage.

---

### Pattern E: Multi-Unit with Heterogeneous Units

**Example**: Beam Trawl (TBB) - 5 beams, different lengths

```
gear_sets
├─ id: "550e8400-e29b-41d4-a716-446655440005"
├─ vessel_id: "vessel-123"
├─ gear_type_code: "TBB"
├─ gear_name: "Beam Trawl Mixed"
├─ all_units_identical: false
├─ characteristics: {"number_of_beams": 5}
└─ created_at: 2025-11-14T18:00:00Z
    │
    └─ gear_units (5 records):
       ├─ unit 1: {"beam_length_m": 8.0}
       ├─ unit 2: {"beam_length_m": 8.0}
       ├─ unit 3: {"beam_length_m": 8.0}
       ├─ unit 4: {"beam_length_m": 10.0}  ← Different
       └─ unit 5: {"beam_length_m": 10.0}  ← Different
```

**Rationale**: Real-world scenario where fisher has beams of different sizes. Each tracked individually.

---

## Database Schema (SQL DDL)

### Table 1: gear_sets

```sql
CREATE TABLE gear_sets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vessel_id UUID NOT NULL REFERENCES vessels(id) ON DELETE CASCADE,
    gear_type_code VARCHAR(10) NOT NULL,
    gear_name VARCHAR(255),
    all_units_identical BOOLEAN DEFAULT false,
    characteristics JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    CONSTRAINT fk_vessel FOREIGN KEY (vessel_id) REFERENCES vessels(id),
    CONSTRAINT fk_gear_type FOREIGN KEY (gear_type_code) REFERENCES mdr_gear_types(code)
);

CREATE INDEX idx_gear_sets_vessel ON gear_sets(vessel_id);
CREATE INDEX idx_gear_sets_type ON gear_sets(gear_type_code);
CREATE INDEX idx_gear_sets_created ON gear_sets(created_at DESC);
```

### Table 2: gear_units

```sql
CREATE TABLE gear_units (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    gear_set_id UUID NOT NULL REFERENCES gear_sets(id) ON DELETE CASCADE,
    unit_number INTEGER NOT NULL,
    characteristics JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT fk_gear_set FOREIGN KEY (gear_set_id) REFERENCES gear_sets(id),
    CONSTRAINT unique_unit_per_set UNIQUE (gear_set_id, unit_number),
    CONSTRAINT positive_unit_number CHECK (unit_number > 0)
);

CREATE INDEX idx_gear_units_set ON gear_units(gear_set_id);
CREATE INDEX idx_gear_units_number ON gear_units(gear_set_id, unit_number);
```

### Characteristics JSONB Schema

The `characteristics` field uses flexible JSONB to accommodate different gear types:

```javascript
// Examples of characteristics structures

// Simple count (FPO)
{
  "number_of_pots": 50
}

// Dual measurements (GNS)
{
  "overall_length_m": 100.0,
  "height_m": 2.5
}

// Optional + mandatory (OTB)
{
  "model": "Standard Trawl v2",  // optional
  "perimeter_m": 150.0            // mandatory
}

// Multi-unit count (TBB, LLS)
{
  "number_of_beams": 5  // or "number_of_lines": 3
}

// Per-unit single char (TBB units)
{
  "beam_length_m": 8.0
}

// Per-unit multiple chars (LLS units)
{
  "length_m": 1400.0,
  "number_of_hooks": 50,
  "hook_size": 4
}
```

---

## Data Flow Architecture

### Flow 1: Registration (SSF-143A → SSF-147)

```
┌─────────────────┐
│  MOBILE APP     │
│  (SSF-143A)     │
└────────┬────────┘
         │ 1. Fisher completes wizard
         │ 2. Constructs payload
         ↓
    [HTTP POST]
    /api/v1/gears
         │
         ↓
┌─────────────────┐
│  BACKEND API    │
│  (SSF-147)      │
│                 │
│  1. Validate    │──→ Check MDR reference data
│  2. Persist     │──→ BEGIN TRANSACTION
│     ├─ Insert gear_set
│     ├─ Insert gear_units (if needed)
│     └─ COMMIT
│  3. Audit log  │──→ Record registration event
│  4. Response   │
└────────┬────────┘
         │
         ↓ Success response
┌─────────────────┐
│  MOBILE APP     │
│  Show success   │
│  Navigate to    │
│  Gear List      │
└─────────────────┘
```

### Flow 2: Future Haul Reporting (Reference Only)

```
┌─────────────────┐
│  GEAR_SETS      │ ←┐
│  (Registered)   │  │
└─────────────────┘  │
                     │ Fisher selects from registered gear
                     │
┌─────────────────┐  │
│  HAUL REPORTING │  │
│  (Future epic)  │──┘
│                 │
│  Declares:      │
│  - Used gear    │──→ References gear_set_id
│  - Quantity     │    (e.g., "used 30 of my 50 pots")
│  - Which units  │    (e.g., "used beams 1-3")
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  CUMULATION     │
│  (System logic) │
│                 │
│  SUM usage      │
│  across hauls   │──→ Applies (1) aggregation rule
│  GROUP BY       │
│  gear_set_id    │
└─────────────────┘
```

**Key Insight**: Registration records INVENTORY, haul reporting declares USAGE.

---

## Why Two Levels?

### Problem Solved:

**Without two levels** (flat model):
```
❌ Can't track individual units
❌ Can't support "used 3 out of 5 beams"
❌ Can't distinguish identical vs different units
❌ Difficult to extend for complex reporting
```

**With two levels** (hierarchical model):
```
✅ Each unit tracked individually
✅ Selective usage possible
✅ Flexible for identical or heterogeneous sets
✅ Scales to complex reporting requirements
✅ Supports future enhancements (unit-level history)
```

### Real-World Benefit:

**Scenario**: Fisher has 5 beams of different lengths

**Registration**:
- Gear set: "5 beams total"
- Unit 1: 8m
- Unit 2: 8m
- Unit 3: 8m
- Unit 4: 10m
- Unit 5: 10m

**Future Haul Reporting**:
- Haul 1: "Used beams 1-3" (the 8m ones)
- Haul 2: "Used beams 4-5" (the 10m ones)
- System knows exactly which beams were used

**Future Regulations**: If EU requires tracking specific gear usage, we're ready! 🎯

---

## Query Examples

### Query 1: Get All Gear for a Vessel

```sql
SELECT 
    gs.id,
    gs.gear_name,
    gs.gear_type_code,
    gs.characteristics,
    COUNT(gu.id) as unit_count
FROM gear_sets gs
LEFT JOIN gear_units gu ON gs.id = gu.gear_set_id
WHERE gs.vessel_id = 'vessel-123'
GROUP BY gs.id
ORDER BY gs.created_at DESC;
```

**Result**:
```
id       | gear_name    | type | characteristics           | unit_count
---------|--------------|------|---------------------------|------------
uuid-001 | Longline 1   | LLS  | {"number_of_lines": 3}   | 3
uuid-002 | My Pots      | FPO  | {"number_of_pots": 50}   | 0
uuid-003 | Gillnet Set  | GNS  | {"length": 100, "h": 2.5}| 0
```

---

### Query 2: Get Complete Gear Details with All Units

```sql
SELECT 
    gs.*,
    json_agg(
        json_build_object(
            'unit_number', gu.unit_number,
            'characteristics', gu.characteristics
        ) ORDER BY gu.unit_number
    ) as units
FROM gear_sets gs
LEFT JOIN gear_units gu ON gs.id = gu.gear_set_id
WHERE gs.id = 'gear-uuid'
GROUP BY gs.id;
```

**Result**: Complete gear record with nested units array

---

### Query 3: Future Haul Reporting Query (Reference)

```sql
-- This will be implemented in future Hauls epic
SELECT 
    gs.gear_name,
    gs.gear_type_code,
    SUM(hgu.quantity_used) as total_used_across_hauls
FROM gear_sets gs
JOIN haul_gear_usage hgu ON gs.id = hgu.gear_set_id
WHERE hgu.fishing_trip_id = 'trip-123'
GROUP BY gs.id, gs.gear_name, gs.gear_type_code;
```

**This implements the (1) aggregation rule!**

---

## JSON Schema Specifications

### Gear Set Characteristics Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "oneOf": [
    {
      "title": "FPO - Pots",
      "properties": {
        "number_of_pots": {
          "type": "integer",
          "minimum": 1
        }
      },
      "required": ["number_of_pots"]
    },
    {
      "title": "GNS - Gillnets Anchored",
      "properties": {
        "overall_length_m": {
          "type": "number",
          "minimum": 0.01
        },
        "height_m": {
          "type": "number",
          "minimum": 0.01
        }
      },
      "required": ["overall_length_m", "height_m"]
    },
    {
      "title": "LLS - Set Longlines",
      "properties": {
        "number_of_lines": {
          "type": "integer",
          "minimum": 1
        }
      },
      "required": ["number_of_lines"]
    }
  ]
}
```

### Gear Unit Characteristics Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "oneOf": [
    {
      "title": "TBB Unit - Beam",
      "properties": {
        "beam_length_m": {
          "type": "number",
          "minimum": 0.01
        }
      },
      "required": ["beam_length_m"]
    },
    {
      "title": "LLS Unit - Line",
      "properties": {
        "length_m": {
          "type": "number",
          "minimum": 0.01
        },
        "number_of_hooks": {
          "type": "integer",
          "minimum": 1
        },
        "hook_size": {
          "type": "number",
          "minimum": 0.01
        }
      },
      "required": ["length_m", "number_of_hooks", "hook_size"]
    }
  ]
}
```

---

## API Payload Examples

### Example 1: Simple Gear (FPO - Pots)

**Request**:
```json
POST /api/v1/gears

{
  "vessel_id": "vessel-123",
  "gear_type_code": "FPO",
  "gear_name": "My Pots",
  "gear_set_characteristics": {
    "number_of_pots": 50
  },
  "gear_units": []
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "gear_set_id": "uuid-001",
    "gear_name": "My Pots",
    "gear_type_code": "FPO",
    "total_units": 0,
    "created_at": "2025-11-14T18:00:00Z"
  }
}
```

---

### Example 2: Multi-Unit All Identical (LLS - Longlines)

**Request**:
```json
POST /api/v1/gears

{
  "vessel_id": "vessel-123",
  "gear_type_code": "LLS",
  "gear_name": "Longline 1",
  "all_units_identical": true,
  "gear_set_characteristics": {
    "number_of_lines": 3
  },
  "gear_units": [
    {
      "unit_number": 1,
      "characteristics": {
        "length_m": 1400,
        "number_of_hooks": 50,
        "hook_size": 4
      }
    },
    {
      "unit_number": 2,
      "characteristics": {
        "length_m": 1400,
        "number_of_hooks": 50,
        "hook_size": 4
      }
    },
    {
      "unit_number": 3,
      "characteristics": {
        "length_m": 1400,
        "number_of_hooks": 50,
        "hook_size": 4
      }
    }
  ]
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "gear_set_id": "uuid-004",
    "gear_name": "Longline 1",
    "gear_type_code": "LLS",
    "total_units": 3,
    "all_identical": true,
    "created_at": "2025-11-14T18:00:00Z"
  }
}
```

---

### Example 3: Multi-Unit Different (TBB - Beam Trawl)

**Request**:
```json
POST /api/v1/gears

{
  "vessel_id": "vessel-123",
  "gear_type_code": "TBB",
  "gear_name": "Beam Trawl Mixed",
  "all_units_identical": false,
  "gear_set_characteristics": {
    "number_of_beams": 5
  },
  "gear_units": [
    {"unit_number": 1, "characteristics": {"beam_length_m": 8}},
    {"unit_number": 2, "characteristics": {"beam_length_m": 8}},
    {"unit_number": 3, "characteristics": {"beam_length_m": 8}},
    {"unit_number": 4, "characteristics": {"beam_length_m": 10}},
    {"unit_number": 5, "characteristics": {"beam_length_m": 10}}
  ]
}
```

---

## Validation Rules Reference

### Gear Set Level Validation

| Rule | Check | Error Code |
|------|-------|------------|
| Vessel exists | vessel_id in vessels table | 403 |
| Gear type valid | gear_type_code in MDR | 422 |
| Required chars present | Per Business Rules doc | 422 |
| Data types correct | MEASURE=number, QUANTITY=int | 400 |
| Values positive | All numeric > 0 | 422 |

### Gear Units Level Validation

| Rule | Check | Error Code |
|------|-------|------------|
| Count matches | len(gear_units) == number_of_units | 400 |
| Unit numbers sequential | 1, 2, 3... no gaps | 400 |
| All units complete | Each has required chars | 422 |
| Unit data types | Same as gear set level | 400 |
| Foreign key valid | gear_set_id exists | 400 |

---

## Extension Points for Future Stories

### SSF-143B, C, D: Additional Gear Types

**To add new gear type**:
1. Add characteristics schema to config
2. Add validation rules
3. Frontend automatically generates form
4. Backend automatically validates
5. No code changes to core framework!

**Example config entry**:
```json
{
  "SDN": {
    "name": "Danish anchor seine",
    "category": "SEINES",
    "pattern": "dual_measurement_no_units",
    "characteristics": [
      {"code": "GM", "name": "Overall length", "type": "MEASURE", "unit": "m", "required": true},
      {"code": "HE", "name": "Maximum height", "type": "MEASURE", "unit": "m", "required": true}
    ]
  }
}
```

### Future Haul Reporting Integration

**New table** (to be created in Hauls epic):
```sql
CREATE TABLE haul_gear_usage (
    id UUID PRIMARY KEY,
    haul_id UUID REFERENCES hauls(id),
    gear_set_id UUID REFERENCES gear_sets(id),
    quantity_used INTEGER,
    units_used INTEGER[],  -- Array of unit_numbers used
    created_at TIMESTAMP
);
```

**Query for (1) aggregation**:
```sql
-- Sum gear usage across multiple hauls
SELECT 
    gs.gear_name,
    SUM(hgu.quantity_used) as cumulated_usage
FROM haul_gear_usage hgu
JOIN gear_sets gs ON hgu.gear_set_id = gs.id
WHERE haul_id IN (SELECT id FROM hauls WHERE trip_id = 'trip-123')
GROUP BY gs.id, gs.gear_name;
```

---

## Migration Path

### Phase 1: SSF-143A + SSF-147 (Current)
- Implement core framework
- Support 5 pilot gear types
- Validate approach

### Phase 2: SSF-143B (Sprint 4-5)
- Add 15 more common gear types
- Reuse framework
- No structural changes

### Phase 3: SSF-143C (Sprint 6-7)
- Add 40 standard gear types
- Continue pattern reuse
- Refinements based on feedback

### Phase 4: SSF-143D (Sprint 8+)
- Add complex/edge case gear types
- Handle free-text scenarios
- Complete all 72 types

---

## Technical Considerations

### Performance Optimization:
- **Indexes**: On vessel_id, gear_type_code, created_at
- **Caching**: MDR reference data cached in memory
- **Batch insert**: gear_units inserted as batch, not loops
- **Transaction scope**: Minimal to reduce lock time

### Data Integrity:
- **Foreign keys**: Enforce referential integrity
- **Cascading deletes**: Delete gear_set removes all gear_units
- **Constraints**: Unique (gear_set_id, unit_number)
- **Check constraints**: Positive values enforced at database level

### Scalability:
- **JSONB indexing**: Can create GIN indexes if needed
- **Partitioning**: gear_sets could partition by vessel_id if needed
- **Archival**: Old gear can be archived without deleting

---

## Glossary

| Term | Definition |
|------|------------|
| **Gear Set** | Parent record representing a piece of fishing equipment |
| **Gear Unit** | Child record representing an individual component of multi-unit gear |
| **All Identical** | Flag indicating all units in set have same characteristics |
| **MDR** | Master Data Register - EU reference data for fishing codes |
| **Characteristics** | Measurements/attributes required for a gear type (length, count, etc.) |
| **MEASURE** | Numeric value with unit (metres, mm) - allows decimals |
| **QUANTITY** | Integer count - whole numbers only |
| **Aggregation Rule (1)** | EU requirement to sum gear usage across multiple hauls when reporting |

---

## Approval & Review

**Document Status**: Ready for Technical Review

**Required Reviews**:
- [ ] Tech Lead: Database schema validation
- [ ] Backend Developer: API design validation
- [ ] Mobile Developer: Frontend data structure validation
- [ ] Product Manager: Business logic confirmation
- [ ] DG MARE/Client: Registration vs reporting interpretation

**Review Notes**: 
_[To be added after review sessions]_

---

## References

- **SSF-143A**: [MOB] Register New Gear - Dynamic Characteristics (uses this model)
- **SSF-147**: [BACK] Register New Gear Endpoint (implements this model)
- **Business Rules**: GEAR_CHARACTERISTICS_BUSINESS_RULES.md
- **Gear Analysis**: Gear_Registration_Analysis.xlsx
- **MDR Data**: MDR Data for SSF App/ folder

---

*This data model supports the Gear Management epic (PI 02) and provides foundation for future haul reporting.*

**Version**: 1.0  
**Last Updated**: November 14, 2025  
**Status**: Ready for Implementation
