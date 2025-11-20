# SSF-142: [MOB] Register New Gear - Form Submission

**JIRA Ticket**: SSF-142  
**Summary**: [MOB] Register new gear - Form submission  
**Epic**: Gear Management  
**Sprint**: Sprint 2  
**PI**: PI 02  
**Story Points**: 3  
**Assignee**: [Mobile Developer]  
**Priority**: High  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Implement the form submission functionality for registering new fishing gear in the mobile application. This includes saving the gear data locally (offline support), submitting to the backend API, and handling synchronization between the mobile database and backend database.
{panel}
{panel:title=Business rules}
*Context*
Fishers need to register their fishing gear while at sea where internet connectivity may be unreliable or unavailable. The mobile app must support offline data entry, allowing fishers to register gear without an active connection, then automatically sync the data to the backend when connectivity is restored.

*Offline-First Strategy*
- All gear registration data must be saved locally first (mobile database)
- The app should work fully offline - fishers can register gear without internet
- When online, the app should automatically sync pending gear registrations to the backend
- If sync fails, the data remains in local database with "pending sync" status
- The app should retry failed syncs automatically when connection is restored

*Data Validation*
- Validate all required fields before allowing submission
- Gear type must be selected from the MDR reference list
- Required characteristics must be filled based on the selected gear type
- Gear marking details must follow proper format
- All numeric fields (mesh size, length, etc.) must be within valid ranges

*Synchronization Rules*
- Local database is the source of truth until successfully synced
- After successful backend sync, mark local record as "synced"
- Keep track of sync timestamp for each gear registration
- Handle conflicts if gear was modified locally after failed sync
- Display sync status to user (pending, syncing, synced, failed)

*Suggestion 01*: Implement a visual indicator (icon/badge) showing the sync status of each registered gear item in the gear list.

{*}Suggestion 02{*}: Add a manual "Sync Now" button to allow fishers to force synchronization when they know they have good connectivity.

{color:#ff8b00}*Questions / Ideas*{color}
Should we allow fishers to edit a gear registration that is "pending sync", or lock it until sync is complete?
How long should we keep successfully synced gear data in the local database? (for offline viewing)
Should we implement a retry limit for failed syncs, or keep retrying indefinitely?
{panel}
{panel:title=Dependencies}
SSF-147: [BACK] Register new gear API endpoint must be completed
https://citnet.tech.ec.europa.eu/CITnet/jira/browse/SSF-147

SSF-141: [MOB] Register new gear - gear characteristics form must be completed
Local database schema for gear registration must be defined
Network connectivity monitoring service must be available
Authentication token management for API calls must be implemented
{panel}
{panel:title=Mockups}
See: SSF DOCS/Mockups SSF FIGMA/Gear Management/
The mockups show:
- Gear registration form with submit button
- Success/error messages after submission
- Sync status indicators
- Offline mode behavior
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Successfully submit gear registration when online*{color}
*GIVEN* the fisher has completed the gear registration form with all required fields
*AND* the mobile device has an active internet connection
*AND* the user is authenticated
*WHEN* the fisher taps the "Save" or "Submit" button
*THEN* the gear data should be saved to the local database first
*AND* the gear data should be sent to the backend API (POST /api/v1/gears)
*AND* upon successful API response (201 Created), mark the local record as "synced"
*AND* display a success message "Gear registered successfully"
*AND* return the fisher to the gear list screen showing the new gear

{color:#4c9aff}*02 - Save gear registration locally when offline*{color}
*GIVEN* the fisher has completed the gear registration form with all required fields
*AND* the mobile device has NO internet connection
*WHEN* the fisher taps the "Save" button
*THEN* the gear data should be saved to the local database
*AND* mark the local record with status "pending_sync"
*AND* display a message "Gear saved locally. Will sync when online."
*AND* return the fisher to the gear list screen
*AND* the new gear should appear in the list with a "pending sync" indicator

{color:#4c9aff}*03 - Automatically sync pending gear registrations when connection restored*{color}
*GIVEN* there are gear registrations in local database with status "pending_sync"
*AND* the mobile device regains internet connection
*WHEN* the app detects the connection is restored
*THEN* the app should automatically attempt to sync all pending gear registrations
*AND* for each successful sync, update the local record status to "synced"
*AND* display a notification "X gear(s) synced successfully"

{color:#4c9aff}*04 - Validate required fields before submission*{color}
*GIVEN* the fisher is on the gear registration form
*WHEN* the fisher attempts to submit without filling all required fields
*THEN* the submission should be prevented
*AND* highlight the missing/invalid fields in red
*AND* display an error message "Please fill all required fields"
*AND* keep the fisher on the form to complete the missing information

{color:#4c9aff}*05 - Handle API error during submission (online)*{color}
*GIVEN* the fisher has completed the gear registration form
*AND* the mobile device has internet connection
*WHEN* the fisher submits the form
*AND* the backend API returns an error (e.g., 400 Bad Request, 500 Server Error)
*THEN* the gear data should remain in local database with status "sync_failed"
*AND* display an error message explaining the issue
*AND* allow the fisher to retry submission or edit the gear data
*AND* the gear should appear in the list with a "sync failed" indicator

{color:#4c9aff}*06 - Prevent duplicate submissions*{color}
*GIVEN* the fisher has submitted a gear registration
*AND* the submission is in progress (saving to backend)
*WHEN* the submit button is still visible
*THEN* the submit button should be disabled during the submission process
*AND* display a loading indicator "Submitting..."
*AND* prevent the fisher from tapping submit multiple times
*AND* re-enable the button only after success or failure response

{color:#4c9aff}*07 - Display sync status for each gear in the list*{color}
*GIVEN* the fisher is viewing the gear list
*WHEN* the list contains gears with different sync statuses
*THEN* each gear should display its sync status:
  - Synced: Green checkmark icon
  - Pending sync: Orange clock/sync icon
  - Sync failed: Red warning icon
*AND* tapping on a "sync failed" gear should allow retry

{color:#4c9aff}*08 - Validate gear characteristics based on gear type*{color}
*GIVEN* the fisher has selected a gear type "Gillnet" (requires mesh size)
*WHEN* the fisher attempts to submit without entering mesh size
*THEN* the submission should be prevented
*AND* display error message "Mesh size is required for Gillnet"
*AND* highlight the mesh size field

{color:#4c9aff}*09 - Handle token expiration during submission*{color}
*GIVEN* the fisher has completed the gear registration form
*AND* the authentication token has expired
*WHEN* the fisher attempts to submit the form
*THEN* the app should detect the expired token
*AND* prompt the fisher to re-authenticate
*AND* after successful re-authentication, resume the gear registration submission
*AND* complete the sync without losing the entered data

{color:#4c9aff}*10 - Manual sync retry for failed submissions*{color}
*GIVEN* a gear registration has status "sync_failed" in the local database
*AND* the mobile device has internet connection
*WHEN* the fisher taps the "Retry Sync" button or icon
*THEN* the app should attempt to sync that specific gear to the backend
*AND* update the status based on the result (synced or sync_failed)
*AND* display appropriate feedback message

h3. Additional Acceptance Criteria
* Form submission should complete within 3 seconds (with good connectivity)
* Local database operations (save) should complete within 500ms
* All gear data must be validated before saving to local database
* Implement proper error handling for all network failures
* Log all submission attempts and sync operations for debugging
* Implement automatic retry with exponential backoff for failed syncs
* Display clear user feedback for all submission states (loading, success, error)
* Preserve form data if app is closed/crashed before submission
* Implement conflict resolution if gear was modified during sync
* Support batch sync for multiple pending gear registrations
```

---

## ✅ Tasks Checklist

### Form Submission Logic
- [ ] Implement form validation (required fields, data types, value ranges)
- [ ] Create local database save function for gear data
- [ ] Implement API call to backend POST /api/v1/gears endpoint
- [ ] Handle successful submission (update local DB status, show success message)
- [ ] Handle failed submission (update status, show error message)
- [ ] Implement submit button disable/enable logic during submission
- [ ] Add loading indicator during submission process

### Offline Support
- [ ] Implement local database schema for gear registrations
- [ ] Create offline save functionality (save to local DB only)
- [ ] Implement sync status tracking (pending_sync, synced, sync_failed)
- [ ] Add network connectivity detection service
- [ ] Display appropriate messages for offline/online modes

### Synchronization Logic
- [ ] Implement automatic sync when connection is restored
- [ ] Create background sync service for pending gear registrations
- [ ] Implement manual sync retry functionality
- [ ] Add sync status indicators (icons) in gear list
- [ ] Handle API errors during sync (retry logic with exponential backoff)
- [ ] Implement batch sync for multiple pending items
- [ ] Track sync timestamps for each gear

### Data Validation
- [ ] Validate gear type selection (must be from MDR list)
- [ ] Validate gear characteristics based on selected type
- [ ] Validate numeric fields (min/max values, proper format)
- [ ] Validate gear marking details format
- [ ] Display validation errors clearly to user

### Authentication & Security
- [ ] Implement authentication token validation before submission
- [ ] Handle token expiration during submission
- [ ] Implement token refresh mechanism
- [ ] Secure storage of gear data in local database
- [ ] Encrypt sensitive data if needed

### User Experience
- [ ] Display success message after submission
- [ ] Display error messages with actionable guidance
- [ ] Show sync status for each gear in the list
- [ ] Implement navigation back to gear list after submission
- [ ] Add manual "Sync Now" button (optional)
- [ ] Display sync progress/status notifications

### Testing
- [ ] Unit tests for form validation logic
- [ ] Unit tests for local database operations
- [ ] Integration tests for API submission
- [ ] Test offline mode functionality
- [ ] Test sync functionality when connection restored
- [ ] Test error handling scenarios
- [ ] Test token expiration handling
- [ ] Test duplicate submission prevention
- [ ] Performance testing (submission speed)

### Error Handling & Logging
- [ ] Implement comprehensive error handling for all scenarios
- [ ] Log all submission attempts (success/failure)
- [ ] Log all sync operations
- [ ] Track failed syncs for debugging
- [ ] Implement error reporting/analytics

---

## 📱 User Flow Reference

**Happy Path (Online):**
1. Fisher completes gear registration form
2. Fisher taps "Save" button
3. App validates form data
4. App saves to local database (status: pending_sync)
5. App calls backend API
6. Backend returns 201 Created
7. App updates local record (status: synced)
8. App displays success message
9. Fisher returns to gear list

**Offline Path:**
1. Fisher completes gear registration form
2. Fisher taps "Save" button
3. App detects no internet connection
4. App validates form data
5. App saves to local database (status: pending_sync)
6. App displays "Saved locally, will sync when online"
7. Fisher returns to gear list (gear shows "pending sync" icon)
8. Later: Connection restored → Auto-sync triggered → Status updated to "synced"

**Error Path:**
1. Fisher completes form and submits
2. App saves locally
3. API call fails (400/500 error)
4. App updates local record (status: sync_failed)
5. App displays error message
6. Fisher can retry or edit gear data

---

## 🔗 Related Stories

- **SSF-147**: [BACK] Register new gear - API endpoint (dependency)
- **SSF-141**: [MOB] Register new gear - gear characteristics form (dependency)
- **SSF-xxx**: [MOB] Offline data synchronization service
- **SSF-xxx**: [MOB] Network connectivity monitoring

---

**Last Updated**: November 11, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
