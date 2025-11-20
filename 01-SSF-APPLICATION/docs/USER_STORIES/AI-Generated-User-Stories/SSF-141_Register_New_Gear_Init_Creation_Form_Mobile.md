# SSF-141: [MOB] Register New Gear - Init Creation Form

**JIRA Ticket**: SSF-141  
**Summary**: [MOB] Register new gear - Init Creation Form  
**Epic**: Gear Management  
**Sprint**: Sprint 2  
**PI**: PI 02  
**Story Points**: 2  
**Assignee**: [Mobile Developer]  
**Priority**: High  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Initialize and display the gear registration form in the mobile application. This includes loading gear type reference data from the backend, presenting the initial form with gear type selection, and preparing the form for user input. This story focuses on the form initialization and setup, NOT the dynamic characteristics (which is SSF-143) or submission (which is SSF-142).
{panel}
{panel:title=Business rules}
*Context*
When a fisher wants to register a new gear, they tap the "Add New Gear" button from the Vessel's Gear Screen. The app must initialize a new gear registration form, fetch the list of available gear types from the backend (MDR reference data), and present a clean form ready for the fisher to fill in.

This story covers the initial form setup and gear type selection. The dynamic characteristics based on the selected gear type are handled in SSF-143, and form submission is handled in SSF-142.

*Form Initialization Requirements*
- Create new gear registration form screen
- Fetch gear types from backend API (GET /api/v1/reference/gear-types)
- Cache gear type list locally for offline access
- Pre-populate vessel ID from current context
- Initialize all form fields with empty/default values
- Set form in "create" mode (vs "edit" mode)

*Gear Type Selection*
- Display dropdown/picker with all available gear types
- Show gear type name and code from MDR
- Support search/filter within gear type list
- Group gear types by category (optional: Nets, Lines, Traps, etc.)
- Mark required field indicator on gear type selection
- Validate gear type selection before allowing form progression

*Offline Support*
- Cache gear type reference data after first successful fetch
- Use cached data if offline or if fetch fails
- Indicate to user if using cached data (show timestamp)
- Auto-refresh cached data when online and data is stale (>24 hours old)

*User Experience*
- Display loading state while fetching gear types
- Show error message if gear types cannot be loaded
- Provide retry option if fetch fails
- Display helpful hints/tooltips for gear type selection
- Support keyboard navigation and accessibility features

*Suggestion 01*: Show small icons or thumbnails next to each gear type to help fishers quickly identify the type (visual aid).

{*}Suggestion 02{*}: Remember the fisher's last selected gear type and suggest it as a "quick select" option for faster repeated registrations.

{color:#ff8b00}*Questions / Ideas*{color}
Should we display a brief description of each gear type to help fishers choose correctly?
Should we show which gear types are most commonly used by this vessel (based on history)?
Should we validate against vessel's allowed gear types based on fishing license/permits?
{panel}
{panel:title=Dependencies}
SSF-147: [BACK] Register new gear - Reference data endpoint must be completed
https://citnet.tech.ec.europa.eu/CITnet/jira/browse/SSF-147

SSF-144: [MOB] Vessel's Gear Screen must be completed (navigation source)
Local database schema for caching gear types must be defined
Navigation framework and screen routing must be set up
Form validation library/framework must be available
{panel}
{panel:title=Mockups}
See: SSF DOCS/Mockups SSF FIGMA/Gear Management/
The mockups show:
- Gear registration form screen initial state
- Gear type dropdown/picker
- Form fields layout
- Loading and error states
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Successfully initialize gear registration form*{color}
*GIVEN* the fisher is on the Vessel's Gear Screen
*AND* the fisher has internet connection
*WHEN* the fisher taps the "Add New Gear" button
*THEN* the app should navigate to the gear registration form screen
*AND* display a loading indicator while fetching gear types
*AND* fetch gear types from backend API (GET /api/v1/reference/gear-types)
*AND* display the form with gear type dropdown populated
*AND* all other form fields should be empty/default state
*AND* the vessel ID should be pre-populated from context

{color:#4c9aff}*02 - Display gear type dropdown with all available types*{color}
*GIVEN* the backend returns 15 gear types
*WHEN* the gear registration form is loaded
*THEN* the gear type dropdown should contain all 15 gear types
*AND* each type should display: name, code, and optional category
*AND* the dropdown should be searchable/filterable
*AND* the gear type field should be marked as required (with * indicator)

{color:#4c9aff}*03 - Cache gear types locally for offline use*{color}
*GIVEN* the app successfully fetched gear types from the backend
*WHEN* the data is received
*THEN* the gear types should be stored in local database
*AND* include a timestamp of when cached
*WHEN* the form is opened again offline
*THEN* the cached gear types should be used
*AND* display a message "Using cached data from [date]"

{color:#4c9aff}*04 - Handle network error when fetching gear types*{color}
*GIVEN* the fisher is online but the backend API is unavailable
*WHEN* the gear registration form attempts to fetch gear types
*THEN* the API call should fail with error
*AND* the app should check for cached gear types in local database
*AND* if cache exists, use cached data and show "Using cached data" message
*AND* if no cache exists, display error "Unable to load gear types. Please try again."
*AND* provide a "Retry" button

{color:#4c9aff}*05 - Load form entirely offline using cached data*{color}
*GIVEN* the fisher has NO internet connection
*AND* gear types were previously cached
*WHEN* the fisher opens the gear registration form
*THEN* the form should load using cached gear types
*AND* display indicator "Offline - Using cached data"
*AND* all form fields should be functional
*AND* NOT display any network error messages

{color:#4c9aff}*06 - Validate gear type is selected before proceeding*{color}
*GIVEN* the fisher is on the gear registration form
*AND* the gear type field is empty
*WHEN* the fisher attempts to proceed to characteristics section
*THEN* the form should prevent progression
*AND* highlight the gear type field in red
*AND* display error message "Please select a gear type"

{color:#4c9aff}*07 - Filter gear types by search term*{color}
*GIVEN* the gear type dropdown contains "Gillnet", "Trammel Net", "Long line"
*WHEN* the fisher types "net" in the gear type search field
*THEN* the dropdown should filter to show only "Gillnet" and "Trammel Net"
*AND* "Long line" should be hidden
*WHEN* the search is cleared
*THEN* all gear types should be displayed again

{color:#4c9aff}*08 - Display loading state during initial fetch*{color}
*GIVEN* the fisher opens the gear registration form
*WHEN* the gear types are being fetched from backend
*THEN* display a loading indicator (spinner/skeleton)
*AND* disable the gear type dropdown (not interactive)
*AND* optionally display message "Loading gear types..."
*WHEN* the fetch completes
*THEN* hide loading indicator and enable dropdown

{color:#4c9aff}*09 - Pre-populate vessel ID from current context*{color}
*GIVEN* the fisher has selected vessel "VESSEL-123"
*WHEN* the gear registration form is initialized
*THEN* the vessel ID should be automatically set to "VESSEL-123"
*AND* the vessel ID field should be hidden or read-only (not editable)
*AND* the vessel name should be displayed for context

{color:#4c9aff}*10 - Handle empty gear types response*{color}
*GIVEN* the backend API returns an empty array of gear types
*WHEN* the gear registration form is loaded
*THEN* display error message "No gear types available. Please contact support."
*AND* disable form progression
*AND* provide option to go back to gear list

h3. Additional Acceptance Criteria
* Form screen must have proper navigation (back button to return to gear list)
* Form must be responsive and work on different screen sizes
* All form fields must follow app's design system and styling
* Form must support accessibility features (screen readers, keyboard navigation)
* Loading state must be clear and not confusing to user
* Error messages must be user-friendly and actionable
* Form initialization must complete within 3 seconds (with good connectivity)
* Cached data must be refreshed if older than 24 hours (when online)
* Form must handle app suspension/restoration without losing state
* All user interactions must have appropriate visual feedback
```

---

## ✅ Tasks Checklist

### Screen Setup
- [ ] Create gear registration form screen/component
- [ ] Set up navigation route from Gear List to Registration Form
- [ ] Design form layout and UI components
- [ ] Implement back button navigation
- [ ] Set up form state management

### Gear Type Data Fetching
- [ ] Implement API call to GET /api/v1/reference/gear-types
- [ ] Handle authentication token in API request
- [ ] Parse API response (gear types array)
- [ ] Handle successful response
- [ ] Handle error responses (network, server errors)

### Local Caching
- [ ] Create local database table for gear types cache
- [ ] Implement function to save gear types to cache
- [ ] Store cache timestamp
- [ ] Implement function to read gear types from cache
- [ ] Check cache age and validity
- [ ] Clear stale cache (>24 hours old)

### Gear Type Dropdown/Picker
- [ ] Create gear type dropdown component
- [ ] Populate dropdown with fetched gear types
- [ ] Display gear type name and code
- [ ] Implement search/filter functionality
- [ ] Handle gear type selection
- [ ] Mark field as required (visual indicator)
- [ ] Support keyboard navigation

### Form Initialization
- [ ] Initialize all form fields with empty/default values
- [ ] Pre-populate vessel ID from context
- [ ] Display vessel name for context
- [ ] Set form mode to "create"
- [ ] Prepare form validation rules
- [ ] Set up form submission handler (link to SSF-142)

### Loading States
- [ ] Display loading indicator during API fetch
- [ ] Disable form controls during loading
- [ ] Show "Loading gear types..." message
- [ ] Hide loading state when fetch completes

### Error Handling
- [ ] Display error message if fetch fails
- [ ] Check for cached data as fallback
- [ ] Display "Retry" button on error
- [ ] Handle empty gear types response
- [ ] Handle network timeout errors
- [ ] Log errors for debugging

### Offline Support
- [ ] Detect offline mode
- [ ] Use cached gear types when offline
- [ ] Display "Offline - Using cached data" indicator
- [ ] Show cache timestamp
- [ ] Handle case when no cache exists offline

### Validation
- [ ] Validate gear type is selected
- [ ] Display validation error messages
- [ ] Highlight invalid fields
- [ ] Prevent form progression with invalid data

### User Experience
- [ ] Display helpful hints/tooltips
- [ ] Show required field indicators
- [ ] Implement smooth transitions/animations
- [ ] Provide clear error messages
- [ ] Handle form state during app suspension
- [ ] Implement accessibility features

### Testing
- [ ] Unit tests for form initialization logic
- [ ] Test API fetch success scenario
- [ ] Test API fetch failure scenario
- [ ] Test offline mode with cached data
- [ ] Test offline mode without cache
- [ ] Test gear type selection
- [ ] Test search/filter functionality
- [ ] Test form validation
- [ ] Test navigation (to/from form)
- [ ] UI/Visual testing

---

## 📱 Form Flow Reference

**Initialization Flow (Online):**
1. Fisher taps "Add New Gear" from Gear List
2. App navigates to Gear Registration Form
3. Display loading indicator
4. Fetch gear types from backend API
5. Store gear types in local cache
6. Populate gear type dropdown
7. Hide loading indicator
8. Form ready for user input

**Initialization Flow (Offline with Cache):**
1. Fisher taps "Add New Gear" from Gear List
2. App navigates to Gear Registration Form
3. Detect no internet connection
4. Load gear types from local cache
5. Populate gear type dropdown
6. Display "Offline - Using cached data" indicator
7. Form ready for user input

**Initialization Flow (Offline without Cache):**
1. Fisher taps "Add New Gear" from Gear List
2. App navigates to Gear Registration Form
3. Detect no internet connection
4. Attempt to load from cache - no data found
5. Display error "Unable to load gear types offline"
6. Provide "Go Back" option

**Initialization Flow (API Error with Cache Fallback):**
1. Fisher taps "Add New Gear" from Gear List
2. App navigates to Gear Registration Form
3. Attempt to fetch from API - fails
4. Check local cache - data found
5. Load gear types from cache
6. Display "Using cached data (backup)" indicator
7. Form ready for user input

---

## 🔗 Related Stories

- **SSF-147**: [BACK] Register new gear - Reference data endpoint (dependency)
- **SSF-144**: [MOB] Vessel's Gear Screen - Gear List (navigation source)
- **SSF-143**: [MOB] Register new gear - Gear characteristics (next step after this)
- **SSF-142**: [MOB] Register new gear - Form submission (final step)

---

**Last Updated**: November 11, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
