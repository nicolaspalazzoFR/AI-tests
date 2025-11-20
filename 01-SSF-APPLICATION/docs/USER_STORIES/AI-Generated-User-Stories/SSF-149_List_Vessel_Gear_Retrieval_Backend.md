# SSF-149: [BACK] List of Vessel's Gear - Retrieval

**JIRA Ticket**: SSF-149  
**Summary**: [BACK] List of vessel's gear - Retrieval  
**Epic**: Gear Management  
**Sprint**: Sprint 2  
**PI**: PI 02  
**Story Points**: 2  
**Assignee**: [Backend Developer]  
**Priority**: High  
**Scope**: [BACK]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Create API endpoint to retrieve the list of all fishing gears registered to a specific vessel. This endpoint provides the mobile application with gear data for display in the vessel's gear list screen, supporting both full list retrieval and optional filtering/sorting.
{panel}
{panel:title=Business rules}
*Context*
Fishers need to view all fishing gears currently registered to their vessel. The mobile app calls this endpoint to fetch the gear list when displaying the Vessel's Gear Screen, and also during synchronization to ensure local data is up-to-date with the backend.

The endpoint must return complete gear information including type, characteristics, marking details, and status, while ensuring proper access control (fishers can only retrieve gears for vessels they have permission to access).

*Data Requirements*
- Return all gears associated with the specified vessel ID
- Include complete gear details: type, code, characteristics, marking, dimensions, status
- Include timestamps (created_at, updated_at)
- Support filtering by gear status (active, retired, lost)
- Support sorting (by date, by type, by status)
- Return empty array if vessel has no gears (not an error)

*Performance Requirements*
- Endpoint should respond within 500ms for typical vessel (20-50 gears)
- Support pagination for vessels with many gears (>100)
- Implement efficient database queries with proper indexing
- Cache gear reference data (types, characteristics) to reduce lookups

*Access Control*
- Verify fisher has permission to view gears for the specified vessel
- Return 403 Forbidden if fisher doesn't own or have access to the vessel
- Support different permission levels (owner, crew member, inspector)

*Suggestion 01*: Include a "last_modified" timestamp in response to support efficient delta sync (mobile app can request only gears modified since last sync).

{*}Suggestion 02{*}: Return gear count summary in response header (e.g., "X-Total-Gears: 12") to help mobile app manage pagination.

{color:#ff8b00}*Questions / Ideas*{color}
Should we include soft-deleted gears in the response (with a "deleted" status)?
Should we support filtering by multiple criteria simultaneously (e.g., status AND type)?
Should we include related data like gear photos/attachments in the response, or require separate API calls?
{panel}
{panel:title=Dependencies}
Database schema for gear storage must be completed
Authentication and authorization middleware must be implemented
Vessel ownership/permission validation service must be available
MDR reference data must be available for gear type lookups
{panel}
{panel:title=Mockups}
See: SSF DOCS/Mockups SSF FIGMA/Gear Management/
The mockups show the gear list screen that displays data from this endpoint.
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Successfully retrieve list of gears for a vessel*{color}
*GIVEN* a fisher is authenticated and has permission to access vessel "VESSEL-123"
*AND* vessel "VESSEL-123" has 3 gears registered
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 200 OK
*AND* the response should include a JSON array with 3 gear objects
*AND* each gear object should contain: id, vessel_id, gear_type, characteristics, marking, status, created_at, updated_at
*AND* gears should be ordered by creation date (newest first)

{color:#4c9aff}*02 - Return empty array when vessel has no gears*{color}
*GIVEN* a fisher is authenticated and has permission to access vessel "VESSEL-456"
*AND* vessel "VESSEL-456" has NO gears registered
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-456/gears
*THEN* the response should return status 200 OK
*AND* the response should include an empty JSON array []
*AND* no error should be returned

{color:#4c9aff}*03 - Validate fisher has permission to access vessel*{color}
*GIVEN* a fisher with user ID "USER-123" is authenticated
*AND* the fisher does NOT have permission to access vessel "VESSEL-789"
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-789/gears
*THEN* the response should return status 403 Forbidden
*AND* the error message should be "You do not have permission to view gears for this vessel"

{color:#4c9aff}*04 - Handle non-existent vessel ID*{color}
*GIVEN* a fisher is authenticated
*AND* vessel ID "VESSEL-999" does not exist in the database
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-999/gears
*THEN* the response should return status 404 Not Found
*AND* the error message should be "Vessel not found: VESSEL-999"

{color:#4c9aff}*05 - Filter gears by status*{color}
*GIVEN* vessel "VESSEL-123" has 5 gears: 3 active, 1 retired, 1 lost
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-123/gears?status=active
*THEN* the response should return status 200 OK
*AND* the response should include only the 3 active gears
*AND* retired and lost gears should NOT be included

{color:#4c9aff}*06 - Sort gears by specified field*{color}
*GIVEN* vessel "VESSEL-123" has gears created on different dates
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-123/gears?sort=created_at&order=asc
*THEN* the response should return status 200 OK
*AND* gears should be ordered by creation date in ascending order (oldest first)
*WHEN* order=desc is specified
*THEN* gears should be ordered in descending order (newest first)

{color:#4c9aff}*07 - Support pagination for large gear lists*{color}
*GIVEN* vessel "VESSEL-123" has 50 gears registered
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-123/gears?page=1&limit=20
*THEN* the response should return status 200 OK
*AND* the response should include 20 gear objects (first page)
*AND* response headers should include pagination info (total count, current page, total pages)
*WHEN* page=2 is requested
*THEN* the next 20 gears should be returned

{color:#4c9aff}*08 - Include gear type details from MDR*{color}
*GIVEN* a gear has gear_type_code "GN" (Gillnet)
*WHEN* the gear list is retrieved
*THEN* each gear should include expanded gear type information:
  - gear_type_code: "GN"
  - gear_type_name: "Gillnet"
  - gear_type_category: "NET"
*AND* this should be populated from MDR reference data

{color:#4c9aff}*09 - Handle database errors during retrieval*{color}
*GIVEN* a fisher makes a valid request
*AND* the database is unavailable or encounters an error
*WHEN* a GET request is made to /api/v1/vessels/VESSEL-123/gears
*THEN* the response should return status 500 Internal Server Error
*AND* the error message should be "Unable to retrieve gears. Please try again."
*AND* the error should be logged for debugging

{color:#4c9aff}*10 - Return gear characteristics in correct format*{color}
*GIVEN* a gear has characteristics: mesh_size: 120, net_length: 1000, mesh_unit: "mm"
*WHEN* the gear is retrieved in the list
*THEN* characteristics should be returned as a structured object
*AND* include all characteristic values with proper data types
*AND* include units where applicable
*AND* maintain data integrity (no loss or corruption)

h3. Additional Acceptance Criteria
* API endpoint must be documented in Swagger/OpenAPI specification
* Response must include proper Content-Type: application/json header
* API must implement proper authentication (JWT token validation)
* API must implement proper authorization (vessel permission check)
* Support CORS for mobile app access
* Implement rate limiting (e.g., max 100 requests per minute per user)
* Response time should be under 500ms for typical vessel
* Database queries must use proper indexes for performance
* Handle large result sets efficiently (use pagination)
* Log all retrieval requests for monitoring
* Cache gear type reference data to improve performance
* Support conditional GET with ETag/If-Modified-Since headers (optional)
```

---

## ✅ Tasks Checklist

### API Endpoint Setup
- [ ] Create GET /api/v1/vessels/{vesselId}/gears endpoint
- [ ] Define response body JSON schema
- [ ] Set up route handler
- [ ] Implement query parameter parsing (status, sort, order, page, limit)

### Authentication & Authorization
- [ ] Implement JWT token validation
- [ ] Verify user is authenticated
- [ ] Check user has permission to view gears for specified vessel
- [ ] Handle unauthorized access (return 403)
- [ ] Handle unauthenticated requests (return 401)

### Data Retrieval Logic
- [ ] Query gears from database by vessel ID
- [ ] Join with gear type reference data from MDR
- [ ] Include all required gear fields
- [ ] Handle empty result set (return empty array)
- [ ] Optimize database query with proper indexes

### Filtering & Sorting
- [ ] Implement status filter (active, retired, lost)
- [ ] Implement sorting by field (created_at, gear_type, status)
- [ ] Implement sort order (asc, desc)
- [ ] Handle invalid filter/sort parameters
- [ ] Apply default sorting (newest first) if not specified

### Pagination
- [ ] Implement page and limit query parameters
- [ ] Calculate total count of gears
- [ ] Calculate total pages
- [ ] Return pagination metadata in response headers
- [ ] Handle invalid page numbers
- [ ] Set reasonable default and maximum limits

### Response Formatting
- [ ] Format gear data for response
- [ ] Include gear type details from MDR
- [ ] Format characteristics as structured object
- [ ] Include all timestamps in ISO 8601 format
- [ ] Return 200 OK with gear array
- [ ] Return 404 for non-existent vessel
- [ ] Return 403 for permission errors
- [ ] Return 500 for server errors

### Error Handling
- [ ] Handle vessel not found (404)
- [ ] Handle permission errors (403)
- [ ] Handle database errors (500)
- [ ] Handle invalid query parameters (400)
- [ ] Log all errors for debugging
- [ ] Return user-friendly error messages

### Performance Optimization
- [ ] Add database indexes on vessel_id, created_at, status
- [ ] Implement query result caching (optional)
- [ ] Cache MDR gear type reference data
- [ ] Optimize JOIN queries
- [ ] Use connection pooling
- [ ] Monitor query performance

### Logging & Monitoring
- [ ] Log all gear retrieval requests
- [ ] Log query execution time
- [ ] Log errors and exceptions
- [ ] Track API usage metrics
- [ ] Monitor response times

### Documentation
- [ ] Document endpoint in Swagger/OpenAPI
- [ ] Document query parameters (status, sort, order, page, limit)
- [ ] Document response schema
- [ ] Document pagination headers
- [ ] Document error responses
- [ ] Add example requests and responses

### Testing
- [ ] Unit tests for retrieval logic
- [ ] Test with empty vessel (no gears)
- [ ] Test with multiple gears
- [ ] Test filtering by status
- [ ] Test sorting (asc/desc)
- [ ] Test pagination
- [ ] Test permission errors
- [ ] Test database errors
- [ ] Integration tests
- [ ] Performance testing with large datasets

---

## 🔗 Related Stories

- **SSF-144**: [MOB] Vessel's Gear Screen - Gear List (consumer)
- **SSF-148**: [BACK] List of vessel's gear - New Gear (related)
- **SSF-142**: [MOB] Register new gear - Form submission (related)
- **SSF-147**: [BACK] Register new gear - Reference data (related)

---

**Last Updated**: November 11, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
