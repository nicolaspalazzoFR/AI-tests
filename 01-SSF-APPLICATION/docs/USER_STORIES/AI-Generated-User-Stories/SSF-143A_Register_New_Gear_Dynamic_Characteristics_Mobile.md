# SSF-143A: [MOB] Register New Gear - Dynamic Characteristics (Framework + Pilot Gears)

**JIRA Ticket**: SSF-143A (Split from original SSF-143)  
**Summary**: [MOB] Register new gear - Dynamic Characteristics Form (Framework + 5 Pilot Gear Types)  
**Epic**: Gear Management  
**Sprint**: Sprint 3  
**PI**: PI 02  
**Story Points**: 3  
**Assignee**: [Mobile Developer]  
**Priority**: High  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Implement the dynamic gear characteristics form using a multi-step wizard pattern that adapts based on selected gear type. This story establishes the framework for dynamic characteristic collection and implements 5 pilot gear types covering all core technical patterns. These 5 types represent the most commonly used fishing gears and will validate the approach before expanding to all 72 gear types in subsequent stories (SSF-143B, C, D).

*IMPORTANT*: This story uses a mobile-first wizard UX pattern (NOT collapsible accordions) following Luke Wroblewski's principles and eUI Mobile component standards.
{panel}

{panel:title=Business rules}
*Context*
After the fisher selects a gear type in SSF-141, the system must dynamically present the appropriate characteristic fields based on the selected gear type. Different gear types require different characteristics - some need just a count, others need multiple measurements per unit. This story implements the framework and 5 pilot gear types that cover all major patterns.

*Reference Documents*
- Business Rules: SSF DOCS/GEAR_CHARACTERISTICS_BUSINESS_RULES.md
- Gear Analysis: SSF DOCS/Gear_Registration_Analysis.xlsx
- Data Model: SSF DOCS/GEAR_REGISTRATION_DATA_MODEL.md

*Two-Level Data Model*
Gear registration consists of two levels:

**Level 1 - Gear Set** (overall)
- Gear type, gear name (optional)
- Overall quantity (e.g., "Number of lines: 3")
- All-identical flag (for smart duplication)

**Level 2 - Gear Units** (repeatable, conditional)
- Per-unit characteristics (e.g., length of each line)
- Only needed for multi-unit gear types
- Can be identical or vary

*Wizard UX Pattern* (Mobile-First per Luke Wroblewski)

**NOT Using**: Collapsible accordions (hide/show pattern)  
**Using Instead**: Multi-step wizard with linear flow

**Why**: 
- Accordions hide content (extra taps to reveal)
- Accordions create cognitive overload on small screens
- Wizard provides clear progress, one task per screen
- Better for accessibility and thumb-friendly navigation

**Wizard Flow**:
1. Screen 1: Gear type & quantity (from SSF-141)
2. Screen 2: Smart duplication decision (if multi-unit)
3. Screen 3+: Unit details (one per screen if needed)
4. Final Screen: Review & confirm

*Smart Duplication Pattern*

For multi-unit gears (e.g., 3 longlines, 5 beams):

**Common Case** (80% of usage): All units identical
- Checkbox: "All [units] have same characteristics" (DEFAULT CHECKED)
- Fisher fills ONE form
- System duplicates to all units
- Saves massive time!

**Edge Case** (20% of usage): Units differ
- Uncheck "All identical"
- Wizard shows one screen per unit
- Progress indicator: "●●○ Unit 2 of 3"

*5 Pilot Gear Types*

These 5 types cover all technical patterns and represent most common fishing gears:

**1. FPO - Pots** (Simplest)
Pattern: Single count field
- Number of pots: [stepper input]
- No sub-units needed
- One-screen registration

**2. GNS - Gillnets Anchored** (Standard Dual-Field)
Pattern: Two measurements
- Overall length: [number] metres
- Height: [number] metres
- No sub-units needed
- One-screen registration

**3. OTB - Bottom Otter Trawl** (Optional + Mandatory Mix)
Pattern: Optional text + mandatory measurement
- Model of trawl: [text] (optional)
- Perimeter of opening: [number] metres (mandatory)
- No sub-units needed
- One-screen registration

**4. TBB - Beam Trawl** (Multi-Unit, Simple Characteristics)
Pattern: Repeatable sub-units with single characteristic each
- Number of beams: [stepper]
- Per beam: Length in metres
- Tests repeatable sub-form pattern
- Tests smart duplication

**5. LLS - Set Longlines** (Multi-Unit, Multiple Characteristics)
Pattern: Repeatable sub-units with 3 characteristics each
- Number of lines: [stepper]
- Per line: Length (m), Number of hooks, Hook size
- Tests most complex pattern
- Tests smart duplication with multiple fields

*Why These 5*
- Each introduces a NEW pattern (no redundancy)
- Cover 80% of actual fishing activity
- All are "Simple" or "Medium" complexity (from analysis)
- No workshop-dependent items (deferred FYK, FAR to SSF-143D)
- Can be delivered and tested quickly

*Component Usage* (eUI Mobile 18.x)

**Navigation**:
- `euim-toolbar` with back button
- Progress indicator for wizard steps

**Input Controls** (per Luke W principles):
- `ion-input` for text and numeric fields
- `ion-button` with +/- for stepper controls (NOT dropdown for quantities)
- `ion-checkbox` for "All identical" toggle
- `ion-select` ONLY for gear type (if needed, but preferably autocomplete)

**Layout**:
- `ion-card` for visual grouping
- `ion-item` for form fields
- `ion-label` with clear required indicators (*)

**Feedback**:
- `ion-progress-bar` for wizard progress
- `euim-alert-message` for validation errors
- Success confirmation after save

*Validation Rules*

**Field-Level Validation**:
- Required fields: Cannot be empty
- Numeric fields: Must be positive numbers > 0
- Text fields: Max 500 characters
- Gear type specific: Reference Business Rules document

**Cross-Field Validation**:
- If "Number of units" = 3, must have exactly 3 units in payload
- All units must have complete characteristics
- Validate against gear type requirements

**Smart Duplication Logic**:
- IF "All identical" checked AND unit 1 complete
- THEN auto-populate units 2-N with unit 1 data
- Allow review/edit before final save

*Offline Support*

- Form state persists if app suspended
- Can save draft locally
- Submit to backend when online
- Clear "unsaved changes" if navigate away (with warning)

*Forward Compatibility with Haul Reporting*

This registration captures gear INVENTORY (what fisher owns).  
Future haul reporting will reference registered gear to declare USAGE.  
The (1) aggregation rule applies during haul reporting, NOT registration.

**Data Flow**:
Registration (now) → Haul Usage Declaration (future) → Automatic Cumulation (future)

{color:#ff8b00}*ASSUMPTION REQUIRING CLIENT VALIDATION*{color}
We assume gear registration captures equipment inventory (what fisher OWNS), not typical usage. The (1) aggregation rule for reporting applies during haul declarations (future Hauls epic), not during gear registration.

Client must validate this interpretation in Gear Registration Workshop.

*Suggestion 01*: Use haptic feedback on successful step completion for tactile confirmation (iOS/Android native)

{*}Suggestion 02{*}: Add "Save as Draft" option at any wizard step so fisher can come back later without losing data

{color:#ff8b00}*Questions / Ideas*{color}
Should we allow fishers to duplicate an existing gear registration as a starting point for a new similar gear?
Should we show typical/average values for each gear type to help fishers validate their entries?
Should we support photo upload of gear for visual confirmation in future versions?
{panel}

{panel:title=Dependencies}
SSF-141: [MOB] Register new gear - Init Creation Form (must be completed - gear type selection)
SSF-147: [BACK] Register new gear endpoint (must support two-level data model)

Technical Dependencies:
- Wizard/stepper navigation component library
- Form validation framework
- Local database schema for gear_sets and gear_units tables
- eUI Mobile 18.x components available
- Offline-first data persistence layer

Business Dependencies:
- Business Rules document finalized: GEAR_CHARACTERISTICS_BUSINESS_RULES.md
- Gear Registration Analysis reviewed: Gear_Registration_Analysis.xlsx
- Client validation on registration vs reporting interpretation
{panel}

{panel:title=Mockups}
Current mockups show collapsible accordion pattern - **TO BE UPDATED**

New wizard pattern mockups to be generated using:
- eUI Mobile components (https://euidev.ecdevops.eu/eui-showcase-mobile-18.x/)
- Multi-step wizard pattern
- See: FIGMA_AI_PROMPT_Gear_Registration_Wizard.md for Figma AI generation instructions

Reference screens:
- Wizard step progression with progress bar
- Stepper controls for quantities (+/- buttons)
- "All identical" smart duplication UI
- Review & confirm screen
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Display wizard with progress indicator*{color}
*GIVEN* fisher has selected gear type "Longline (LLS)" in SSF-141
*WHEN* the characteristics form is displayed
*THEN* show wizard with progress indicator "Step 1 of 4"
*AND* display screen title "Gear Information"
*AND* show back button to return to gear type selection
*AND* show "Continue" or "Next" button to proceed

{color:#4c9aff}*02 - Collect gear set quantity with stepper control*{color}
*GIVEN* fisher is registering gear type "Longline (LLS)"
*WHEN* Step 1 is displayed
*THEN* show field "Number of lines" with stepper control (+/- buttons)
*AND* default value should be 1
*AND* allow direct numeric input (tap number to edit)
*AND* minimum value = 1, maximum value = 20
*AND* show validation error if value < 1
*AND* do NOT use dropdown for quantity selection

{color:#4c9aff}*03 - Display smart duplication option for multi-unit gears*{color}
*GIVEN* fisher has entered "Number of lines: 3" (or any value > 1)
*WHEN* fisher taps "Continue"
*THEN* navigate to Step 2
*AND* display checkbox "All lines have same characteristics" (checked by default)
*AND* show helper text "Check this to save time - we'll duplicate your entries"
*AND* show "Continue" button

{color:#4c9aff}*04 - Smart duplication path - collect once, apply to all*{color}
*GIVEN* "All lines identical" is CHECKED
*AND* fisher taps "Continue"
*WHEN* Step 3 is displayed
*THEN* show title "Line Characteristics (applies to all 3 lines)"
*AND* show fields: Length, Number of hooks, Hook size
*AND* do NOT show unit number or progress for individual lines
*WHEN* fisher completes fields and taps "Continue"
*THEN* navigate directly to Review screen (skip individual line screens)
*AND* Review screen shows all 3 lines with identical values

{color:#4c9aff}*05 - Individual unit path - one screen per unit*{color}
*GIVEN* "All lines identical" is UNCHECKED
*AND* fisher taps "Continue"
*WHEN* Step 3 is displayed
*THEN* show title "Line 1 of 3"
*AND* show progress indicator "●○○"
*AND* show fields: Length, Number of hooks, Hook size
*WHEN* fisher completes and taps "Next"
*THEN* navigate to "Line 2 of 3" screen
*AND* show progress "●●○"
*WHEN* all units complete
*THEN* navigate to Review screen

{color:#4c9aff}*06 - Validate required characteristics per gear type*{color}
*GIVEN* fisher is entering characteristics for "Longline (LLS)"
*WHEN* fisher leaves "Length" field empty and taps "Continue"
*THEN* prevent navigation
*AND* highlight "Length" field in red
*AND* show error "Length is required for Set longlines"
*AND* scroll to first error field

{color:#4c9aff}*07 - Handle simple gear type (Pots - no sub-units)*{color}
*GIVEN* fisher selected gear type "Pots (FPO)" in SSF-141
*WHEN* characteristics form is displayed
*THEN* show simple form with "Number of pots" stepper only
*AND* show "Save Gear" button (no multi-step wizard needed)
*AND* no "All identical" option (not applicable)
*WHEN* fisher enters 50 and taps "Save"
*THEN* submit gear registration with just the count

{color:#4c9aff}*08 - Handle dual-field gear type (Gillnets - no sub-units)*{color}
*GIVEN* fisher selected gear type "Gillnets anchored (GNS)"
*WHEN* characteristics form is displayed
*THEN* show form with two fields: "Overall length (m)" and "Height (m)"
*AND* both marked as required with * indicator
*AND* show "Save Gear" button
*AND* no wizard progression (single screen sufficient)
*WHEN* both fields complete and "Save" tapped
*THEN* submit gear registration

{color:#4c9aff}*09 - Display review screen with all entered data*{color}
*GIVEN* fisher has completed all wizard steps for "3 longlines, all identical"
*WHEN* final "Review & Confirm" screen is displayed
*THEN* show gear summary:
- Gear name: "Longline 1" (or auto-generated)
- Gear type: "Set longlines (LLS)"
- Number of lines: 3
- Line 1: Length 1400m, 50 hooks, size 4
- Line 2: Length 1400m, 50 hooks, size 4
- Line 3: Length 1400m, 50 hooks, size 4
*AND* show [Edit] button to go back and modify
*AND* show [Save Gear] button to submit

{color:#4c9aff}*10 - Use stepper controls for all quantity inputs*{color}
*GIVEN* form displays any quantity field (Number of beams, Number of lines, Number of hooks, etc.)
*WHEN* the field is rendered
*THEN* display +/- button stepper controls
*AND* allow direct numeric input (tap to edit)
*AND* increment/decrement by 1 on button tap
*AND* prevent value from going below minimum
*AND* do NOT use dropdown menus for quantities (Luke W principle)

{color:#4c9aff}*11 - Implement wizard navigation with back/next*{color}
*GIVEN* fisher is in middle of wizard (e.g., "Line 2 of 3")
*WHEN* screen is displayed
*THEN* show [Back] button in top-left
*AND* show [Next] or [Continue] button at bottom
*AND* enable [Back] navigation to previous step
*AND* validate current step before allowing [Next]
*AND* maintain entered data when navigating back

{color:#4c9aff}*12 - Show wizard progress indicator*{color}
*GIVEN* fisher is in multi-step wizard
*WHEN* any wizard screen is displayed
*THEN* show progress indicator (e.g., "●●○ Step 2 of 3")
*AND* clearly indicate current step and total steps
*AND* optionally show step names (Gear Info → Units → Review)

{color:#4c9aff}*13 - Handle beam trawl multi-unit with single characteristic*{color}
*GIVEN* fisher selected "Beam trawl (TBB)"
*AND* entered "Number of beams: 5"
*AND* unchecked "All identical"
*WHEN* wizard progresses to beam details
*THEN* show 5 sequential screens: "Beam 1 of 5", "Beam 2 of 5", etc.
*AND* each screen shows single field: "Beam length (m)"
*AND* progress updates: ●○○○○, ●●○○○, ●●●○○, etc.

{color:#4c9aff}*14 - Save form state for offline and app suspension*{color}
*GIVEN* fisher is mid-way through wizard (entered data in steps 1-2)
*WHEN* app is suspended (backgrounded) or goes offline
*THEN* save current form state to local storage
*WHEN* app resumes or comes back online
*THEN* restore fisher to exact same step with data intact
*AND* show "Draft in progress" indicator

{color:#4c9aff}*15 - Validate data types per characteristic*{color}
*GIVEN* characteristic is MEASURE type (e.g., length, height)
*WHEN* fisher enters value
*THEN* validate it's a positive decimal number
*AND* show error if negative or zero
*AND* allow up to 2 decimal places
*GIVEN* characteristic is QUANTITY type (e.g., number of hooks)
*THEN* validate it's a positive integer (whole number)
*AND* show error if decimal or negative

{color:#4c9aff}*16 - Display appropriate keyboard for input type*{color}
*GIVEN* field requires numeric input (length, quantity, etc.)
*WHEN* field is focused
*THEN* display numeric keyboard on mobile device
*AND* include decimal point for MEASURE types
*AND* exclude decimal for QUANTITY types

{color:#4c9aff}*17 - Handle optional vs mandatory fields clearly*{color}
*GIVEN* gear type "Bottom otter trawl (OTB)" has optional "Model" field
*WHEN* form is displayed
*THEN* show "Model of trawl" without * indicator
*AND* show "(Optional)" helper text
*AND* allow field to be empty on submission
*GIVEN* field is mandatory (e.g., "Perimeter")
*THEN* show * indicator after label
*AND* prevent submission if empty

{color:#4c9aff}*18 - Enable edit from review screen*{color}
*GIVEN* fisher is on Review & Confirm screen
*AND* sees data for all entered units
*WHEN* fisher taps [Edit] button
*THEN* navigate back to first wizard step
*AND* maintain all previously entered data
*AND* allow fisher to modify any values
*WHEN* fisher completes wizard again
*THEN* show updated values in Review screen

{color:#4c9aff}*19 - Submit complete gear registration payload*{color}
*GIVEN* fisher has reviewed all data on final screen
*WHEN* fisher taps "Save Gear" button
*THEN* construct complete gear registration payload with:
- Gear set level: type, name, quantity, all_identical flag
- Gear units array: all unit details
*AND* validate payload completeness
*AND* submit to backend POST /api/v1/gears (SSF-147)
*AND* handle response (success/error)

{color:#4c9aff}*20 - Display success confirmation and navigate to gear list*{color}
*GIVEN* gear registration submitted successfully
*WHEN* backend returns success response
*THEN* show success message "Gear registered successfully"
*AND* auto-navigate to Vessel's Gear Screen (SSF-144) after 2 seconds
*AND* new gear should appear in the list
*AND* clear wizard form state

h3. Additional Acceptance Criteria

**UX & Accessibility**:
* All wizard screens must use eUI Mobile 18.x components
* Stepper buttons must be minimum 44x44 pixels (thumb-friendly)
* Form must support screen reader navigation
* Progress indicators must announce current step to screen readers
* All required fields must have aria-required attribute
* Error messages must be clearly associated with fields (aria-describedby)

**Performance**:
* Wizard step transitions must be smooth (< 300ms)
* Form state must persist across app suspension
* No data loss on navigation back/forth
* Validation must be instant (< 100ms feedback)

**Data Integrity**:
* Form data must match Business Rules requirements exactly
* Unit count must match gear_units array length
* All required characteristics per gear type must be collected
* Data must be structured correctly for backend API (SSF-147)

**Error Handling**:
* Network errors during submission: Save locally, retry when online
* Validation errors: Clear, specific messages per field
* System errors: Fallback to save draft, contact support
* Back-end rejection: Display error message, allow correction
```

---

## ✅ Tasks Checklist

### Framework Setup
- [ ] Create wizard navigation framework/component
- [ ] Implement wizard state management (current step, data, progress)
- [ ] Create progress indicator component (●●○ style)
- [ ] Set up form validation framework for wizard
- [ ] Implement stepper control component (+/- buttons per Luke W)
- [ ] Create wizard screen base template

### Gear Type Pattern Framework
- [ ] Create configuration mapping: gear_type_code → required_characteristics
- [ ] Implement dynamic field generation based on gear type
- [ ] Create reusable characteristic input components (length, count, text)
- [ ] Implement optional vs mandatory field logic
- [ ] Set up keyboard type switching (numeric vs text)

### Smart Duplication Feature
- [ ] Create "All identical" checkbox component
- [ ] Implement duplication logic (copy unit 1 to units 2-N)
- [ ] Build conditional wizard flow (single unit form vs multi-unit screens)
- [ ] Create review screen with duplicated data display
- [ ] Allow edit of duplicated values

### Pilot Gear Type 1: FPO (Pots)
- [ ] Implement single-screen form: Number of pots with stepper
- [ ] No wizard needed - direct save
- [ ] Validate positive integer
- [ ] Test submission to backend

### Pilot Gear Type 2: GNS (Gillnets Anchored)
- [ ] Implement single-screen form: Length + Height
- [ ] Both fields mandatory with * indicators
- [ ] Numeric keyboard for both inputs
- [ ] Validate both > 0
- [ ] Test submission to backend

### Pilot Gear Type 3: OTB (Bottom Otter Trawl)
- [ ] Implement single-screen form: Model (optional) + Perimeter (mandatory)
- [ ] Clearly mark Model as "(Optional)"
- [ ] Validate Perimeter is required and > 0
- [ ] Allow submission with Model empty
- [ ] Test submission to backend

### Pilot Gear Type 4: TBB (Beam Trawl)
- [ ] Implement Step 1: Number of beams (stepper)
- [ ] Implement Step 2: "All beams identical?" checkbox
- [ ] Implement Step 3a: Single beam form (if all identical)
- [ ] Implement Step 3b: Multi-screen per beam (if different)
- [ ] Show progress "Beam 1 of 5", "Beam 2 of 5", etc.
- [ ] Implement Review screen showing all beams
- [ ] Test both paths (identical vs different)
- [ ] Test submission with 1 beam, 3 beams, 5 beams

### Pilot Gear Type 5: LLS (Set Longlines)
- [ ] Implement Step 1: Number of lines (stepper)
- [ ] Implement Step 2: "All lines identical?" checkbox
- [ ] Implement Step 3a: Single line form with 3 fields (if all identical)
  - Length of line (m)
  - Number of hooks
  - Hook size
- [ ] Implement Step 3b: Multi-screen per line (if different)
- [ ] Show progress "Line 1 of 3", "Line 2 of 3", "Line 3 of 3"
- [ ] Implement Review screen showing all lines
- [ ] Test both paths
- [ ] Test submission with varying line counts

### Wizard Navigation
- [ ] Implement [Back] button functionality
- [ ] Implement [Next]/[Continue] button functionality
- [ ] Implement step-by-step validation
- [ ] Maintain form data across navigation
- [ ] Implement [Skip to Review] option (optional enhancement)

### Review & Confirmation
- [ ] Create Review screen component
- [ ] Display all gear set information
- [ ] Display all unit information (in list/card format)
- [ ] Implement [Edit] button (navigate back to Step 1)
- [ ] Implement [Save Gear] button
- [ ] Show loading indicator during submission

### Data Submission
- [ ] Construct two-level payload (gear_set + gear_units array)
- [ ] Validate payload structure before submission
- [ ] Call backend API POST /api/v1/gears (SSF-147)
- [ ] Handle success response (show confirmation, navigate to gear list)
- [ ] Handle error response (show error message, allow retry)
- [ ] Implement offline queue (save locally if offline)

### Offline Support
- [ ] Persist wizard state to local storage
- [ ] Restore wizard state on app resume
- [ ] Queue submissions for when online
- [ ] Show "Draft" indicator for incomplete registrations
- [ ] Implement "Unsaved changes" warning on navigation away

### Validation & Error Handling
- [ ] Implement field-level validation (on blur)
- [ ] Implement step-level validation (before Next)
- [ ] Implement form-level validation (before Submit)
- [ ] Display validation errors clearly (per Luke W principles)
- [ ] Associate error messages with fields (accessibility)
- [ ] Test all validation scenarios

### Component Integration (eUI Mobile 18.x)
- [ ] Integrate `euim-toolbar` for navigation
- [ ] Use `ion-input` for all text/numeric fields
- [ ] Use `ion-button` for stepper +/- controls
- [ ] Use `ion-checkbox` for "All identical" toggle
- [ ] Use `ion-card` for visual grouping
- [ ] Use `ion-progress-bar` for wizard progress
- [ ] Use `euim-alert-message` for errors
- [ ] Ensure consistent eUI styling across all components

### Testing
- [ ] Unit tests for wizard navigation logic
- [ ] Unit tests for smart duplication logic
- [ ] Unit tests for each of 5 pilot gear types
- [ ] Test data payload construction
- [ ] Test validation rules for all 5 gear types
- [ ] Test offline form state persistence
- [ ] Test back/next navigation with data integrity
- [ ] UI tests for each wizard screen
- [ ] Accessibility tests (screen reader, keyboard nav)
- [ ] Test on iOS and Android devices
- [ ] Test with slow network conditions
- [ ] Integration test with SSF-141 (gear type selection)
- [ ] Integration test with SSF-147 (backend submission)

---

## 📱 Wizard Flow Reference

### Flow A: Simple Gear (No Units) - FPO, GNS, OTB

```
SSF-141: Select Gear Type
         ↓
   Single Screen Form
   - Show all characteristics
   - No wizard needed
         ↓
   [Save Gear] → Backend
         ↓
   Success → Navigate to Gear List
```

### Flow B: Multi-Unit with Smart Duplication (All Identical) - TBB, LLS

```
SSF-141: Select Gear Type
         ↓
   Step 1: Quantity
   - Number of [units]: [stepper]
   - [Continue]
         ↓
   Step 2: Duplication Decision
   - ☑ All [units] identical (checked)
   - [Continue]
         ↓
   Step 3: Single Unit Form
   - Characteristics (applies to all)
   - [Continue]
         ↓
   Step 4: Review & Confirm
   - Shows all units with duplicated data
   - [Edit] [Save Gear]
         ↓
   Backend Submission
         ↓
   Success → Navigate to Gear List
```

### Flow C: Multi-Unit with Individual Entry (Different Units) - TBB, LLS

```
SSF-141: Select Gear Type
         ↓
   Step 1: Quantity
   - Number of [units]: [stepper]
   - [Continue]
         ↓
   Step 2: Duplication Decision
   - ☐ All [units] identical (unchecked)
   - [Continue]
         ↓
   Step 3: Unit 1 Details
   - Progress: ●○○ (1 of 3)
   - Characteristics
   - [Next: Unit 2]
         ↓
   Step 4: Unit 2 Details
   - Progress: ●●○ (2 of 3)
   - [Back] [Next: Unit 3]
         ↓
   Step 5: Unit 3 Details
   - Progress: ●●● (3 of 3)
   - [Back] [Continue to Review]
         ↓
   Step 6: Review & Confirm
   - Shows all 3 units with individual data
   - [Edit] [Save Gear]
         ↓
   Backend Submission
         ↓
   Success → Navigate to Gear List
```

---

## 📊 Data Structure Reference

### Payload Structure (Sent to Backend)

**Simple Gear (FPO, GNS, OTB)**:
```json
{
  "vessel_id": "vessel-uuid",
  "gear_type_code": "FPO",
  "gear_name": "My Pots",
  "gear_set_characteristics": {
    "number_of_pots": 50
  },
  "gear_units": []
}
```

**Multi-Unit Gear - All Identical (TBB, LLS)**:
```json
{
  "vessel_id": "vessel-uuid",
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

**Multi-Unit Gear - Different Units**:
```json
{
  "vessel_id": "vessel-uuid",
  "gear_type_code": "TBB",
  "gear_name": "Beam Trawl Set",
  "all_units_identical": false,
  "gear_set_characteristics": {
    "number_of_beams": 5
  },
  "gear_units": [
    {"unit_number": 1, "characteristics": {"beam_length_m": 8}},
    {"unit_number": 2, "characteristics": {"beam_length_m": 8}},
    {"unit_number": 3, "characteristics": {"beam_length
