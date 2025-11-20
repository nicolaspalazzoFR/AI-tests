# SSF-144: [MOB] Vessel's Gear Screen - Gear List

**JIRA Ticket**: SSF-144  
**Summary**: [MOB] Vessel's Gear Screen - Gear list  
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
Display the list of fishing gears registered to the vessel in the mobile application. This screen shows all gears associated with the current vessel, including their key information (type, characteristics, sync status) and provides access to gear management actions (view details, edit, delete).
{panel}
{panel:title=Business rules}
*Context*
Fishers need to view all fishing gears currently registered to their vessel. This gear list serves as the main hub for gear management, allowing fishers to see what gears are on board, their characteristics, and their synchronization status with the backend.

The gear list must support both online and offline modes, displaying locally stored gear data when no internet connection is available.

*Display Requirements*
- Show all gears registered to the current vessel
- Display key gear information: gear type, gear code/ID, main characteristics (e.g., mesh size for nets)
- Show sync status for each gear (synced, pending sync, sync failed)
- Display gears in reverse chronological order (newest first)
- Support empty state when no gears are registered
- Include visual indicators for gear status and type

*Offline Support*
- The gear list must work fully offline using locally stored data
- Display all gears saved in the local database
- Clearly indicate which gears are pending synchronization with backend
- Show last sync timestamp for each gear
- Allow viewing gear details even when offline

*User Interactions*
- Tap on a gear item to view full details
- Long press or swipe gesture to reveal actions menu (Edit, Delete)
- Pull-to-refresh to sync with backend (when online)
- Search/filter gears by type or characteristics
- Sort gears by date added, type, or sync status

*Suggestion 01*: Implement grouping by gear type (e.g., "Nets", "Lines", "Traps") with expandable/collapsible sections for better organization.

{*}Suggestion 02{*}: Add a "Quick Actions" button on each gear item for common operations (View, Edit, Sync) without needing to navigate away.

{panel}
{panel:title=Dependencies}
SSF-149: [BACK] List of vessel's gear - Retrieval endpoint must be completed
https://citnet.tech.ec.europa.eu/CITnet/jira/browse/SSF-149

SSF-148: [BACK] List of vessel's gear - New Gear endpoint (for creating gears)
Local database schema for storing gear data must be defined
Authentication and vessel selection must be completed
Gear detail view screen must be implemented
{panel}
{panel:title=Mockups}
See: SSF DOCS/Mockups SSF FIGMA/Gear Management/
The mockups show:
- Gear list screen with multiple gear items
- Empty state when no gears registered
- Sync status indicators on each gear item
- "Add new gear" button
- Search/filter functionality
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Display list of registered gears when gears exist*{color}
*GIVEN* the fisher has selected a vessel
*AND* the vessel has 3 gears registered in the local database
*WHEN* the fisher navigates to the Vessel's Gear Screen
*THEN* the screen should display all 3 gears in a list
*AND* each gear item should show: gear type name, gear ID/code, main characteristic (e.g., mesh size)
*AND* each gear item should display its sync status icon
*AND* gears should be ordered by creation date (newest first)

{color:#4c9aff}*02 - Display empty state when no gears registered*{color}
*GIVEN* the fisher has selected a vessel
*AND* the vessel has NO gears registered
*WHEN* the fisher navigates to the Vessel's Gear Screen
*THEN* the screen should display an empty state message "No gears registered yet"
*AND* display an illustration or icon indicating empty list
*AND* show a prominent "Add New Gear" button
*AND* optionally display helpful text like "Tap + to register your first gear"

{color:#4c9aff}*03 - Display sync status indicators for each gear*{color}
*GIVEN* the fisher is viewing the gear list
*AND* the list contains gears with different sync statuses
*WHEN* the list is displayed
*THEN* each gear should show appropriate sync status:
  - Synced gear: Green checkmark icon + "Synced" label
  - Pending sync: Orange clock icon + "Pending" label
  - Sync failed: Red warning icon + "Failed" label
*AND* the sync status should be clearly visible without tapping the item

{color:#4c9aff}*04 - Navigate to gear detail view on tap*{color}
*GIVEN* the fisher is viewing the gear list
*AND* the list contains at least one gear
*WHEN* the fisher taps on a gear item
*THEN* the app should navigate to the gear detail screen
*AND* display full information about the selected gear
*AND* provide options to edit or delete the gear

{color:#4c9aff}*05 - Display "Add New Gear" button*{color}
*GIVEN* the fisher is viewing the Vessel's Gear Screen
*WHEN* the screen is loaded
*THEN* an "Add New Gear" button should be visible
*AND* the button should be prominently placed (e.g., floating action button or header button)
*WHEN* the fisher taps the "Add New Gear" button
*THEN* the app should navigate to the gear registration form

{color:#4c9aff}*06 - Load and display gears from local database (offline)*{color}
*GIVEN* the fisher has no internet connection
*AND* there are gears stored in the local database
*WHEN* the fisher navigates to the Vessel's Gear Screen
*THEN* the app should load gears from the local database
*AND* display all locally stored gears
*AND* show appropriate sync status for each gear
*AND* NOT display any error about missing internet connection

{color:#4c9aff}*07 - Sync gear list with backend when online*{color}
*GIVEN* the fisher has internet connection
*AND* the fisher is viewing the gear list
*WHEN* the fisher performs pull-to-refresh gesture
*THEN* the app should fetch the latest gear list from the backend API
*AND* update the local database with any new or modified gears
*AND* display a loading indicator during sync
*AND* show success message "Gear list updated" after successful sync
*AND* refresh the displayed list with updated data

{color:#4c9aff}*08 - Handle sync errors gracefully*{color}
*GIVEN* the fisher has internet connection
*AND* the fisher attempts to sync the gear list
*WHEN* the backend API returns an error (e.g., 500 Server Error)
*THEN* the app should display an error message "Unable to sync. Please try again."
*AND* keep displaying the locally stored gear list
*AND* allow the fisher to retry the sync

{color:#4c9aff}*09 - Display gear characteristics based on gear type*{color}
*GIVEN* the gear list contains different gear types
*WHEN* the list is displayed
*THEN* each gear should show relevant characteristics for its type:
  - Gillnet: Show mesh size (e.g., "Mesh: 120mm")
  - Longline: Show length (e.g., "Length: 5000m")
  - Trap: Show quantity (e.g., "Qty: 50")
*AND* use consistent formatting for all characteristics

{color:#4c9aff}*10 - Filter/search gears by type or name*{color}
*GIVEN* the fisher is viewing a gear list with multiple gears
*WHEN* the fisher enters "net" in the search field
*THEN* the list should filter to show only gears with "net" in their type name
*AND* display count of filtered results (e.g., "3 of 12 gears")
*WHEN* the fisher clears the search
*THEN* the full list should be displayed again

h3. Additional Acceptance Criteria
* Gear list must load within 1 second from local database
* Support smooth scrolling for lists with 50+ gears
* Implement pull-to-refresh gesture for manual sync
* Show last sync timestamp at top of list (e.g., "Last synced: 2 minutes ago")
* Display total count of gears (e.g., "12 gears registered")
* Handle empty search results with appropriate message
* Implement proper error handling for all data loading scenarios
* Support swipe gestures for quick actions (optional)
* Preserve scroll position when returning to list from detail view
* Display visual feedback during data loading operations
```

---

## ✅ Tasks Checklist

### UI/Screen Development
- [ ] Design and implement gear list screen layout
- [ ] Create gear list item component/widget
- [ ] Implement empty state view (when no gears)
- [ ] Add "Add New Gear" floating action button or header button
- [ ] Design and implement sync status indicators (icons + labels)
- [ ] Create loading state view (shimmer/skeleton)

### Data Loading & Display
- [ ] Implement function to load gears from local database
- [ ] Query gears by vessel ID from local database
- [ ] Sort gears by creation date (newest first)
- [ ] Map gear data to display format
- [ ] Implement gear list item rendering with all required fields
- [ ] Display gear type name and icon
- [ ] Display main characteristics based on gear type
- [ ] Show sync status for each gear

### Offline Support
- [ ] Ensure gear list works fully offline using local data
- [ ] Handle case when local database is empty
- [ ] Display appropriate messages for offline mode
- [ ] Cache gear list data for faster subsequent loads

### Synchronization
- [ ] Implement pull-to-refresh gesture
- [ ] Call backend API to fetch latest gear list (GET /api/v1/vessels/{id}/gears)
- [ ] Update local database with fetched gears
- [ ] Handle sync success and refresh display
- [ ] Handle sync errors and display error messages
- [ ] Show last sync timestamp
- [ ] Implement automatic sync on screen load (when online)

### User Interactions
- [ ] Implement tap gesture on gear item to navigate to detail view
- [ ] Implement "Add New Gear" button tap to navigate to registration form
- [ ] Implement pull-to-refresh gesture
- [ ] Add search/filter functionality (optional)
- [ ] Implement swipe gestures for quick actions (optional)
- [ ] Preserve scroll position on navigation return

### Search & Filter (Optional)
- [ ] Add search bar to screen
- [ ] Implement search/filter logic by gear type or characteristics
- [ ] Display filtered results count
- [ ] Handle empty search results

### Sync Status Display
- [ ] Display sync status icon for each gear
- [ ] Show "Synced" status with green checkmark
- [ ] Show "Pending Sync" status with orange clock icon
- [ ] Show "Sync Failed" status with red warning icon
- [ ] Display sync timestamp or relative time

### Error Handling
- [ ] Handle database query errors
- [ ] Handle API sync errors
- [ ] Handle network errors during sync
- [ ] Display user-friendly error messages
- [ ] Log errors for debugging

### Performance
- [ ] Optimize local database queries
- [ ] Implement lazy loading for large lists (if needed)
- [ ] Cache gear list data
- [ ] Optimize list rendering performance

### Testing
- [ ] Unit tests for gear list loading logic
- [ ] Unit tests for sync functionality
- [ ] Test empty state display
- [ ] Test with different numbers of gears (0, 1, 10, 50+)
- [ ] Test offline mode functionality
- [ ] Test sync success and failure scenarios
- [ ] Test navigation to detail view
- [ ] Test navigation to registration form
- [ ] Test search/filter functionality
- [ ] UI/Visual testing for all states

---

## 📱 Screen States Reference

**1. Loading State:**
- Display skeleton/shimmer placeholders while loading from database
- Show loading indicator for initial load

**2. Empty State:**
- No gears registered
- Display illustration + "No gears registered yet" message
- Prominent "Add New Gear" button

**3. Populated State (Offline):**
- Display all gears from local database
- Show sync status for each gear
- Display "Offline" indicator or message

**4. Populated State (Online):**
- Display all gears
- Support pull-to-refresh
- Show last sync timestamp

**5. Syncing State:**
- Show loading indicator during sync
- Overlay on existing list (don't clear list during sync)

**6. Error State:**
- Display error message for sync failures
- Keep showing locally stored gears
- Provide retry option

**7. Search/Filter Active:**
- Show filtered results
- Display filter count
- Show "Clear" button

---

## 🔗 Related Stories

- **SSF-149**: [BACK] List of vessel's gear - Retrieval (dependency)
- **SSF-148**: [BACK] List of vessel's gear - New Gear (related)
- **SSF-141**: [MOB] Register new gear - Init Creation Form (navigation target)
- **SSF-xxx**: [MOB] Gear detail view screen
- **SSF-xxx**: [MOB] Edit gear functionality
- **SSF-xxx**: [MOB] Delete gear functionality

---

**Last Updated**: November 11, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
