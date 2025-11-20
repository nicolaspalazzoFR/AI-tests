# SSF-148: [BACK] List of Vessel's Gear - New Gear

**JIRA Ticket**: SSF-148  
**Summary**: [BACK] List of vessel's gear - New Gear  
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
Create API endpoint to register/create a new fishing gear for a vessel. This endpoint receives gear registration data from the mobile application, validates it, stores it in the database, and returns the created gear with a unique identifier.
{panel}
{panel:title=Business rules}
*Context*
When a fisher registers a new gear through the mobile app, the data needs to be stored in the backend database. This endpoint handles the creation of new gear records, ensuring data integrity and proper association with the vessel.

The endpoint must validate all incoming gear data according to MDR reference rules and gear-type-specific requirements before storing in the database.

*Validation Requirements*
- Gear type must exist in the MDR reference data
- Gear type code must be valid according to MDR standards
- Required characteristics must be present based on gear type (e.g., mesh size for nets)
- Numeric fields must be within valid ranges (min/max values)
- Gear marking details must follow proper format and requirements
- All dates must be valid and in correct format
- Vessel ID must exist and fisher must have permission to add gears to that vessel

*Data Storage*
- Generate unique gear ID (UUID) for each new gear
- Store complete gear information including type, characteristics, dimensions, marking
- Associate gear with the vessel ID
- Record creation timestamp and creator user ID
- Store gear status (active, retired, lost, etc.)
- Maintain audit trail of gear creation

*Business Validations*
- Check for duplicate gears (same type + marking on same vessel) - may warn but allow
- Verify fisher has permission to register gears for the specified vessel
- Validate MDR gear type exists and is currently valid
- Ensure gear characteristics match the gear type requirements
- Check data completeness before persistence

*Suggestion 01*: Implement idempotency - if the same gear data is submitted multiple times (e.g., due to network retry), return the existing gear instead of creating duplicates.

{*}Suggestion 02{*}: Return detailed validation errors with field-level error messages to help the mobile app provide better user feedback.

{color:#ff8b00}*Questions / Ideas*{color}
Should we implement gear numbering/sequencing per vessel (e.g., "Gear #1", "Gear #2")?
Should we allow backdating gear registration (register a gear with creation date in the past)?
Should we send notifications to authorities when certain gear types are registered (high-risk gears)?
{panel}
{panel:title=Dependencies}
SSF-147: [BACK] Register new gear - Reference data endpoint must be completed
https://citnet.tech.ec.europa.eu/CITnet/jira/browse/SSF-147

Database schema for gear storage must be defined
MDR reference data must be loaded in database
Authentication and authorization middleware must be implemented
Vessel ownership/permission validation service must be available
{panel}
{panel:title=Mockups}
See: SSF DOCS/Mockups SSF FIGMA/Gear Management/
The mockups show the mobile gear registration form that will submit data to this endpoint.
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Successfully create new gear with valid data*{color}
*GIVEN* a fisher is authenticated and authorized
*AND* the fisher has permission to add gears to vessel "VESSEL-123"
*AND* the request contains valid gear data (type: "Gillnet", mesh size: 120mm, marking: "ABC123")
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 201 Created
*AND* the response should include the created gear with unique ID
*AND* the gear should be stored in the database
*AND* the response should include: id, vessel_id, gear_type, characteristics, marking, created_at
*AND* the creation timestamp should be recorded

{color:#4c9aff}*02 - Validate gear type exists in MDR*{color}
*GIVEN* a fisher submits gear registration data
*AND* the gear type code "INVALID_TYPE" does not exist in MDR
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 400 Bad Request
*AND* the error message should be "Invalid gear type: INVALID_TYPE not found in MDR"
*AND* no gear should be created in the database

{color:#4c9aff}*03 - Validate required characteristics based on gear type*{color}
*GIVEN* a fisher submits gear data for gear type "Gillnet"
*AND* "Mesh Size" is a required characteristic for Gillnets
*AND* the request does NOT include mesh size
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 400 Bad Request
*AND* the error message should be "Missing required characteristic: Mesh Size for gear type Gillnet"
*AND* no gear should be created in the database

{color:#4c9aff}*04 - Validate numeric fields are within allowed ranges*{color}
*GIVEN* a fisher submits gear data for gear type "Gillnet"
*AND* the mesh size value is 5mm (below minimum allowed: 10mm)
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 400 Bad Request
*AND* the error message should be "Mesh Size must be between 10mm and 500mm"
*AND* no gear should be created in the database

{color:#4c9aff}*05 - Validate fisher has permission to add gears to vessel*{color}
*GIVEN* a fisher with user ID "USER-456" is authenticated
*AND* the fisher does NOT have permission to add gears to vessel "VESSEL-789"
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-789/gears
*THEN* the response should return status 403 Forbidden
*AND* the error message should be "You do not have permission to add gears to this vessel"
*AND* no gear should be created in the database

{color:#4c9aff}*06 - Handle missing required fields*{color}
*GIVEN* a fisher submits gear data
*AND* the required field "gear_type" is missing from the request
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 400 Bad Request
*AND* the error message should be "Missing required field: gear_type"
*AND* no gear should be created in the database

{color:#4c9aff}*07 - Handle invalid vessel ID*{color}
*GIVEN* a fisher submits valid gear data
*AND* the vessel ID "VESSEL-999" does not exist in the database
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-999/gears
*THEN* the response should return status 404 Not Found
*AND* the error message should be "Vessel not found: VESSEL-999"
*AND* no gear should be created in the database

{color:#4c9aff}*08 - Handle database errors during creation*{color}
*GIVEN* a fisher submits valid gear data
*AND* the database is unavailable or encounters an error
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 500 Internal Server Error
*AND* the error message should be "Unable to create gear. Please try again."
*AND* the error should be logged for debugging
*AND* no partial data should be committed to the database

{color:#4c9aff}*09 - Generate unique ID for created gear*{color}
*GIVEN* two fishers simultaneously create gears for different vessels
*WHEN* both POST requests are processed
*THEN* each gear should receive a unique ID (UUID)
*AND* the IDs should never collide or duplicate
*AND* both gears should be created successfully

{color:#4c9aff}*10 - Store all gear data correctly*{color}
*GIVEN* a fisher submits complete gear data including:
  - gear_type: "Gillnet"
  - characteristics: { mesh_size: 120, net_length: 1000 }
  - marking: "ABC123"
  - dimensions: { width: 5, height: 2 }
*WHEN* a POST request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* all data should be stored in the database
*AND* retrieving the gear should return all submitted data accurately
*AND* no data should be lost or corrupted

h3. Additional Acceptance Criteria
* API endpoint must be documented in Swagger/OpenAPI specification
* Request body must be validated against defined JSON schema
* All timestamps must be in ISO 8601 format (UTC)
* API must implement proper authentication (JWT token validation)
* API must implement proper authorization (vessel permission check)
* Response must include proper Content-Type: application/json header
* API must log all gear creation attempts (success and failure)
* Database transaction must be used (rollback on error)
* Created gear ID must be returned in response for mobile app to store
* API must handle concurrent requests safely (thread-safe)
* Response time should be under 1 second for successful creation
* Implement rate limiting to prevent abuse (e.g., max 20 gear creations per minute per user)
```

---

## ✅ Tasks Checklist

### API Endpoint Setup
- [ ] Create POST /api/v1/vessels/{vesselId}/gears endpoint
- [ ] Define request body JSON schema
- [ ] Define response body JSON schema
- [ ] Implement request body validation middleware
- [ ] Set up route handler

### Authentication & Authorization
- [ ] Implement JWT token validation
- [ ] Verify user is authenticated
- [ ] Check user has permission to add gears to specified vessel
- [ ] Handle unauthorized access (return 403)
- [ ] Handle unauthenticated requests (return 401)

### Request Validation
- [ ] Validate all required fields are present
- [ ] Validate gear_type exists in MDR reference data
- [ ] Validate gear_type code format
- [ ] Validate required characteristics based on gear type
- [ ] Validate numeric fields are within allowed ranges (min/max)
- [ ] Validate marking format and requirements
- [ ] Validate date fields are valid and in correct format
- [ ] Validate vessel ID exists in database

### Business Logic
- [ ] Generate unique gear ID (UUID)
- [ ] Associate gear with vessel ID
- [ ] Store gear type code and reference
- [ ] Store all gear characteristics
- [ ] Store gear marking and dimensions
- [ ] Set gear status (default: active)
- [ ] Record creation timestamp (UTC)
- [ ] Record creator user ID

### Data Persistence
- [ ] Create database transaction
- [ ] Insert gear data into database
- [ ] Commit transaction on success
- [ ] Rollback transaction on error
- [ ] Handle database constraint violations
- [ ] Handle database connection errors

### Response Handling
- [ ] Return 201 Created on success
- [ ] Include created gear data in response body
- [ ] Include Location header with gear resource URL
- [ ] Return 400 Bad Request for validation errors
- [ ] Return 403 Forbidden for permission errors
- [ ] Return 404 Not Found for invalid vessel ID
- [ ] Return 500 Internal Server Error for server errors
- [ ] Format all error responses consistently

### Error Handling
- [ ] Handle validation errors with detailed messages
- [ ] Handle database errors
- [ ] Handle MDR reference lookup errors
- [ ] Handle vessel permission check errors
- [ ] Log all errors for debugging
- [ ] Return user-friendly error messages
- [ ] Include error codes in responses

### Logging & Monitoring
- [ ] Log all gear creation attempts
- [ ] Log successful gear creations
- [ ] Log validation failures
- [ ] Log permission errors
- [ ] Log database errors
- [ ] Implement request/response logging
- [ ] Add performance monitoring

### Documentation
- [ ] Document endpoint in Swagger/OpenAPI
- [ ] Document request body schema
- [ ] Document response schemas (success + errors)
- [ ] Document authentication requirements
- [ ] Document authorization requirements
- [ ] Add example requests and responses
- [ ] Document error codes and messages

### Testing
- [ ] Unit tests for validation logic
- [ ] Unit tests for business logic
- [ ] Integration tests for database operations
- [ ] Test successful gear creation
- [ ] Test validation error scenarios
- [ ] Test permission error scenarios
- [ ] Test database error handling
- [ ] Test concurrent request handling
- [ ] Load/stress testing
- [ ] API contract testing

---

## 🔗 Related Stories

- **SSF-147**: [BACK] Register new gear - Reference data endpoint (dependency)
- **SSF-142**: [MOB] Register new gear - Form submission (consumer)
- **SSF-149**: [BACK] List of vessel's gear - Retrieval (related)
- **SSF-144**: [MOB] Vessel's Gear Screen - Gear List (consumer)

---

**Last Updated**: November 11, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
