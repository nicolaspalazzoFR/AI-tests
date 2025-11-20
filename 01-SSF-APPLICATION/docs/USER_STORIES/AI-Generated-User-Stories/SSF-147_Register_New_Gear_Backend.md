# SSF-147: [BACK] Register New Gear - Backend Endpoint

**JIRA Ticket**: SSF-147  
**Summary**: [BACK] Register new gear - Backend API endpoint with two-level data model  
**Epic**: Gear Management  
**Sprint**: Sprint 2  
**PI**: PI 02  
**Story Points**: 3  
**Assignee**: [Backend Developer]  
**Priority**: High  
**Scope**: [BACK]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Create backend API endpoint to receive and persist fishing gear registration data from the mobile app. This endpoint supports the wizard UX flow (SSF-143A) by accepting complete gear registrations with a two-level data structure (gear set + individual units). The endpoint must validate gear characteristics against MDR standards and handle 5 pilot gear types initially, with framework extensible to all 72 types.
{panel}

{panel:title=Business rules}
*Context*
The mobile app collects gear registration data through a multi-step wizard (SSF-143A) and submits a complete payload atomically. The backend must persist this data in a two-level structure that supports future haul reporting where fishers will declare usage of registered gear.

*API Design Pattern: Atomic Submission*

Frontend submits complete gear registration after collecting all wizard steps.  
Backend validates and persists everything in ONE transaction.  
No progressive/partial submissions.

**Why**: 
- Aligns with offline-first architecture
- Prevents partial/orphaned records
- Simpler rollback on errors
- Cleaner state management

*Two-Level Data Model*

**Level 1: Gear Set** (parent record)
- Gear metadata: type, name, vessel association
- Overall characteristics: quantity, all_identical flag
- Timestamps: created_at, updated_at

**Level 2: Gear Units** (child records, optional)
- Per-unit characteristics
- Linked to parent gear set via foreign key
- Only created for multi-unit gear types

**Database Tables**:
```sql
gear_sets (
  id UUID PRIMARY KEY,
  vessel_id UUID REFERENCES vessels(id),
  gear_type_code VARCHAR(10),
  gear_name VARCHAR(255),
  all_units_identical BOOLEAN DEFAULT false,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

gear_units (
  id UUID PRIMARY KEY,
  gear_set_id UUID REFERENCES gear_sets(id) ON DELETE CASCADE,
  unit_number INTEGER,
  characteristics JSONB,
  created_at TIMESTAMP
)
```

*5 Pilot Gear Types for Initial Implementation*

**1. FPO - Pots**: Simple count only
- gear_set_characteristics: {"number_of_pots": integer}
- No gear_units records

**2. GNS - Gillnets Anchored**: Dual measurements, no units
- gear_set_characteristics: {"overall_length_m": decimal, "height_m": decimal}
- No gear_units records

**3. OTB - Bottom Otter Trawl**: Optional + mandatory, no units
- gear_set_characteristics: {"model": string (optional), "perimeter_m": decimal}
- No gear_units records

**4. TBB - Beam Trawl**: Multi-unit with single characteristic
- gear_set_characteristics: {"number_of_beams": integer}
- gear_units records: Each with {"beam_length_m": decimal}

**5. LLS - Set Longlines**: Multi-unit with multiple characteristics
- gear_set_characteristics: {"number_of_lines": integer}
- gear_units records: Each with {"length_m": decimal, "number_of_hooks": integer, "hook_size": decimal}

*Validation Requirements*

**Gear Type Validation**:
- Gear type code must exist in MDR_Gear_Type reference data
- Gear type must be currently valid (not expired)
- Check StartDate and EndDate in MDR

**Characteristic Validation**:
- Required characteristics must be present (per Business Rules doc)
- Data types must match (MEASURE=decimal, QUANTITY=integer, TEXT=string)
- Numeric values must be positive and > 0
- Text fields max 500 characters
- Optional fields can be null/empty

**Unit Count Validation**:
- IF gear_set has "number_of_[units]" declared
- THEN gear_units array length must EQUAL that number
- Example: "number_of_lines: 3" requires exactly 3 gear_unit records
- Reject with 400 if mismatch

**Unit Completeness Validation**:
- Each gear_unit must have ALL required characteristics for that gear type
- No partial/incomplete units allowed
- All units must pass same validation as gear_set

*MDR Reference Data Integration*

Endpoint depends on MDR (Master Data Register) reference data:
- MDR_Gear_Type.xls: Valid gear type codes
- MDR_FA_Gear_Characteristic.xls: Characteristic definitions

**Integration approach**:
- Reference data loaded into database on app server startup
- Cached in memory for fast validation
- Periodic refresh from MDR source (daily/weekly)
- Endpoint: GET /api/v1/reference/gear-types (SSF-141 dependency)

*Forward Compatibility with Haul Reporting*

This data model is designed to support future haul reporting:

**Registration** (this story): Fisher records gear INVENTORY (what they own)
**Future Haul Reporting**: Fisher declares gear USAGE (what they used)
**Future Aggregation**: System sums usage across hauls (applies (1) rule)

**Database design supports**:
- Registered gear can be referenced in haul_gear_usage table (future)
- Selective usage: Can declare "used 2 out of 5 beams" (future)
- Cumulation: SUM(usage) GROUP BY gear_set_id (future)

*Security & Access Control*

- Endpoint requires valid authentication token
- Fisher can only register gear for vessels they have permission to access
- Validate vessel_id in request matches fisher's authorized vessels
- Log all gear registrations for audit trail (SSF-187 dependency)

*Error Response Standards*

Return appropriate HTTP status codes:
- 200: Success
- 400: Bad Request (validation failed)
- 401: Unauthorized (invalid token)
- 403: Forbidden (vessel access denied)
- 422: Unprocessable Entity (business rule validation failed)
- 500: Server Error

*Suggestion 01*: Implement idempotency using client_generated_id to handle duplicate submissions from offline sync

{*}Suggestion 02{*}: Return detailed validation errors in structured format so frontend can map to specific fields

{color:#ff8b00}*Questions / Ideas*{color}
Should we enforce vessel size limits for certain gear types (e.g., purse seines too large for small vessels)?
Should we validate against vessel's fishing license/permits for allowed gear types?
Should we implement soft delete vs hard delete for gear records?
{panel}

{panel:title=Dependencies}
Technical Dependencies:
- App Server codebase initialized (SSF-108)
- Database schema for gear_sets and gear_units
- MDR reference data loaded (gear types, characteristics)
- Authentication/authorization middleware
- Validation framework
- API documentation (Swagger)

Frontend Dependencies:
- SSF-141: Gear type selection provides gear_type_code
- SSF-143A: Characteristics collection constructs payload

MDR Data Files:
- MDR_Gear_Type.xls
- MDR_FA_Gear_Characteristic.xls
{panel}

{panel:title=Mockups}
N/A - Backend API, no UI

**API Documentation**:
Swagger spec to be created showing:
- POST /api/v1/gears endpoint
- Request payload schema
- Response schemas (success/error)
- Validation rules
- Authentication requirements
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Accept POST request with complete gear registration*{color}
*GIVEN* authenticated fisher with valid token
*WHEN* POST request sent to /api/v1/gears with complete payload
*THEN* endpoint should accept request
*AND* return 200 OK on success
*AND* return created gear_set_id and timestamp

{color:#4c9aff}*02 - Validate authentication and vessel authorization*{color}
*GIVEN* POST request to /api/v1/gears
*AND* request includes vessel_id: "vessel-123"
*WHEN* endpoint validates authorization
*THEN* verify authentication token is valid
*AND* verify fisher has permission to access vessel-123
*AND* return 401 if token invalid
*AND* return 403 if fisher not authorized for vessel

{color:#4c9aff}*03 - Validate gear type exists in MDR*{color}
*GIVEN* POST request with gear_type_code: "LLS"
*WHEN* validation runs
*THEN* check "LLS" exists in MDR_Gear_Type reference data
*AND* verify gear type is currently valid (within StartDate/EndDate)
*AND* accept if valid
*AND* return 422 with error "Invalid gear type code" if not found

{color:#4c9aff}*04 - Persist gear set and units atomically*{color}
*GIVEN* valid POST request for gear with 3 units
*WHEN* persistence logic executes
*THEN* create gear_set record in database
*AND* create 3 gear_unit records linked to gear_set
*AND* commit as single transaction
*AND* rollback ALL if any insert fails
*AND* return gear_set_id on success

{color:#4c9aff}*05 - Validate unit count matches declaration*{color}
*GIVEN* gear_set declares "number_of_lines: 3"
*AND* gear_units array contains 2 items
*WHEN* validation runs
*THEN* detect count mismatch (3 declared, 2 provided)
*AND* return 400 Bad Request
*AND* error message: "Unit count mismatch: declared 3 but received 2 gear_units"

{color:#4c9aff}*06 - Validate required characteristics present*{color}
*GIVEN* gear type "LLS" requires: length, number_of_hooks, hook_size
*AND* gear_unit missing "hook_size"
*WHEN* validation runs
*THEN* return 422 Unprocessable Entity
*AND* error: "Missing required characteristic: hook_size for gear type LLS"
*AND* indicate which unit failed (unit_number)

{color:#4c9aff}*07 - Validate data types for characteristics*{color}
*GIVEN* characteristic "length_m" should be MEASURE (decimal)
*AND* request provides length_m: "abc" (string)
*WHEN* validation runs
*THEN* return 400 Bad Request
*AND* error: "Invalid data type for length_m: expected number, received string"

{color:#4c9aff}*08 - Validate positive values for measurements*{color}
*GIVEN* request provides length_m: -10
*WHEN* validation runs
*THEN* return 422 Unprocessable Entity
*AND* error: "length_m must be a positive number greater than 0"

{color:#4c9aff}*09 - Handle simple gear type (Pots - no units)*{color}
*GIVEN* POST request for gear type "FPO" (Pots)
*AND* payload includes number_of_pots: 50
*AND* gear_units array is empty
*WHEN* endpoint processes request
*THEN* create gear_set record with characteristics
*AND* do NOT create any gear_unit records
*AND* return success with gear_set_id

{color:#4c9aff}*10 - Handle multi-unit gear with all identical flag*{color}
*GIVEN* POST request for "LLS" with number_of_lines: 3
*AND* all_units_identical: true
*AND* gear_units array has 3 identical items
*WHEN* endpoint processes request
*THEN* accept the submission
*AND* store all_units_identical flag in gear_set
*AND* create 3 gear_unit records
*AND* return success

{color:#4c9aff}*11 - Return structured success response*{color}
*GIVEN* gear registration successful
*WHEN* response is constructed
*THEN* return JSON with:
- success: true
- gear_set_id: UUID
- gear_name: string
- gear_type: code
- total_units: count
- created_at: timestamp
*AND* HTTP status 200 OK

{color:#4c9aff}*12 - Return detailed error response on validation failure*{color}
*GIVEN* validation fails for multiple reasons
*WHEN* error response is constructed
*THEN* return JSON with:
- success: false
- error_code: string
- error_message: string
- validation_errors: array of {field, message, unit_number}
*AND* appropriate HTTP status code (400/422)

{color:#4c9aff}*13 - Implement idempotency for offline sync*{color}
*GIVEN* POST request includes client_generated_id
*AND* gear with same client_generated_id already exists
*WHEN* endpoint receives request
*THEN* return existing gear_set_id (don't create duplicate)
*AND* return 200 OK with existing record
*AND* update updated_at timestamp

{color:#4c9aff}*14 - Generate audit log for gear registration*{color}
*GIVEN* gear successfully registered
*WHEN* persistence completes
*THEN* create audit log entry with:
- fisher_id, vessel_id, gear_set_id
- action: "GEAR_REGISTERED"
- timestamp, IP address
*AND* store in audit_logs table (SSF-187)

{color:#4c9aff}*15 - Handle database connection errors gracefully*{color}
*GIVEN* database connection fails during request
*WHEN* error occurs
*THEN* return 500 Internal Server Error
*AND* log error details for debugging
*AND* do NOT expose internal error details to client
*AND* return generic message: "Service temporarily unavailable"

h3. Additional Acceptance Criteria

**Data Integrity**:
* Foreign key constraints must be enforced (vessel_id, gear_set_id)
* Unit numbers must be sequential (1, 2, 3...) within gear_set
* Timestamps must be in UTC
* UUIDs must be generated server-side
* Characteristics stored in JSONB for flexibility

**Performance**:
* Endpoint must respond within 500ms under normal load
* Support concurrent requests from multiple fishers
* Database indexes on vessel_id and gear_type_code
* Efficient query performance for gear retrieval

**Security**:
* All requests require authentication
* Validate vessel ownership/permission
* Sanitize all input to prevent SQL injection
* Rate limiting to prevent abuse
* Audit logging for compliance

**Extensibility**:
* Framework must support adding new gear types without code changes
* Validation rules driven by configuration (not hard-coded)
* Characteristics schema flexible for future MDR updates
* API versioned (/api/v1/) for backward compatibility
```

---

## ✅ Tasks Checklist

### API Endpoint Setup
- [ ] Create POST /api/v1/gears route
- [ ] Set up authentication middleware
- [ ] Set up authorization middleware (vessel permission)
- [ ] Define request/response schemas
- [ ] Set up error handling middleware

### Database Schema
- [ ] Create gear_sets table migration
- [ ] Create gear_units table migration
- [ ] Define indexes (vessel_id, gear_type_code)
- [ ] Set up foreign key constraints
- [ ] Test database migrations

### MDR Reference Data Integration
- [ ] Load MDR_Gear_Type.xls into database
- [ ] Load MDR_FA_Gear_Characteristic.xls into database
- [ ] Create reference data refresh mechanism
- [ ] Cache reference data in memory
- [ ] Create helper functions to query MDR data

### Validation Logic
- [ ] Implement authentication validation
- [ ] Implement vessel authorization check
- [ ] Implement gear type code validation (exists in MDR)
- [ ] Implement characteristic presence validation (required fields)
- [ ] Implement data type validation (MEASURE, QUANTITY, TEXT)
- [ ] Implement positive value validation (> 0)
- [ ] Implement unit count validation (declared vs provided)
- [ ] Implement unit completeness validation
- [ ] Create validation error message formatter

### Pilot Gear Type 1: FPO (Pots)
- [ ] Implement validation for FPO
- [ ] Required: number_of_pots (integer, > 0)
- [ ] No gear_units expected
- [ ] Test FPO registration
- [ ] Test error scenarios (missing pots, negative value, etc.)

### Pilot Gear Type 2: GNS (Gillnets Anchored)
- [ ] Implement validation for GNS
- [ ] Required: overall_length_m (decimal, > 0), height_m (decimal, > 0)
- [ ] No gear_units expected
- [ ] Test GNS registration
- [ ] Test error scenarios

### Pilot Gear Type 3: OTB (Bottom Otter Trawl)
- [ ] Implement validation for OTB
- [ ] Optional: model (string, max 500 chars)
- [ ] Required: perimeter_m (decimal, > 0)
- [ ] No gear_units expected
- [ ] Test with and without model
- [ ] Test error scenarios

### Pilot Gear Type 4: TBB (Beam Trawl)
- [ ] Implement validation for TBB
- [ ] Required: number_of_beams (integer, > 0)
- [ ] gear_units required: One per beam with beam_length_m
- [ ] Validate unit count matches number_of_beams
- [ ] Test with 1 beam, 3 beams, 5 beams
- [ ] Test all_units_identical flag handling

### Pilot Gear Type 5: LLS (Set Longlines)
- [ ] Implement validation for LLS
- [ ] Required: number_of_lines (integer, > 0)
- [ ] gear_units required: One per line with length_m, number_of_hooks, hook_size
- [ ] Validate all 3 characteristics present per unit
- [ ] Test with varying line counts
- [ ] Test error scenarios (missing characteristics, type mismatches)

### Data Persistence
- [ ] Implement gear_set INSERT logic
- [ ] Implement gear_units batch INSERT logic
- [ ] Wrap in database transaction
- [ ] Generate UUIDs server-side
- [ ] Set created_at/updated_at timestamps
- [ ] Handle database errors gracefully

### Idempotency
- [ ] Accept client_generated_id in request
- [ ] Check if gear with client_generated_id exists
- [ ] Return existing record if found (no duplicate)
- [ ] Create new record if not found
- [ ] Test idempotency scenarios

### Response Construction
- [ ] Build success response JSON
- [ ] Build error response JSON
- [ ] Include validation errors array
- [ ] Set appropriate HTTP status codes
- [ ] Include response timestamps

### Audit Logging
- [ ] Create audit log entry on successful registration
- [ ] Include fisher_id, vessel_id, gear_set_id
- [ ] Record action type: "GEAR_REGISTERED"
- [ ] Store timestamp and IP address
- [ ] Link to SSF-187 audit logging epic

### Error Handling
- [ ] Handle authentication failures
- [ ] Handle authorization failures
- [ ] Handle validation failures
- [ ] Handle database errors
- [ ] Handle MDR reference data unavailable
- [ ] Log all errors for debugging
- [ ] Return user-friendly error messages

### API Documentation
- [ ] Create Swagger/OpenAPI specification
- [ ] Document request payload schema
- [ ] Document response schemas (success/error)
- [ ] Document validation rules
- [ ] Document error codes
- [ ] Provide example requests/responses
- [ ] Document authentication requirements

### Testing
- [ ] Unit tests for validation logic (each gear type)
- [ ] Unit tests for data persistence
- [ ] Integration tests for complete flow (request → database)
- [ ] Test all 5 pilot gear types (happy path)
- [ ] Test all error scenarios per gear type
- [ ] Test authentication/authorization
- [ ] Test idempotency
- [ ] Test transaction rollback on errors
- [ ] Load testing (concurrent requests)
- [ ] Integration test with SSF-143A (mobile submission)

---

## 🔗 API Specification

### Endpoint: POST /api/v1/gears

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body Schema**:
```json
{
  "client_generated_id": "optional-uuid-for-idempotency",
  "vessel_id": "uuid",
  "gear_type_code": "LLS|FPO|GNS|OTB|TBB|...",
  "gear_name": "optional-string-max-255",
  "all_units_identical": "boolean-default-false",
  "gear_set_characteristics": {
    "key": "value (type depends on characteristic)"
  },
  "gear_units": [
    {
      "unit_number": 1,
      "characteristics": {
        "key": "value"
      }
    }
  ]
}
```

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "gear_set_id": "uuid",
    "gear_name": "string",
    "gear_type_code": "string",
    "total_units": 3,
    "created_at": "2025-11-14T18:00:00Z"
  }
}
```

**Error Response (400/422)**:
```json
{
  "success": false,
  "error_code": "VALIDATION_ERROR",
  "error_message": "Gear registration validation failed",
  "validation_errors": [
    {
      "field": "gear_units[0].length_m",
      "message": "Length must be greater than 0",
      "unit_number": 1
    }
  ]
}
```

---

## 🔗 Related Stories

- **SSF-141**: [MOB] Register new gear - Init Creation Form (provides gear_type_code)
- **SSF-143A**: [MOB] Register new gear - Dynamic Characteristics (submits to this endpoint)
- **SSF-148**: [BACK] List of vessel's gear - New Gear (related create operation)
- **SSF-149**: [BACK] List of vessel's gear - Retrieval (will query this data)
- **SSF-187**: [BACK] Audit logs generation (consumes registration events)

---

**Last Updated**: November 14, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
