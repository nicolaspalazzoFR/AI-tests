# Figma AI Prompt: Gear Registration Wizard (eUI Mobile 18.x)

**Purpose**: Generate mockups for SSF-143A gear registration wizard using Figma AI "Make Designs" feature  
**Design System**: eUI Mobile 18.x (European Commission)  
**Target Platform**: iOS and Android mobile apps  
**Created**: November 14, 2025  
**For**: Business Analyst / UX Designer

---

## Prerequisites

### Figma Resources Needed:
1. **eUI Mobile Components Library**: https://www.figma.com/community/file/1052862901059626182
2. **eUI Design Tokens**: https://www.figma.com/community/file/1052857333027422402
3. **eUI Mobile Patterns**: https://www.figma.com/community/file/1052862901059626182

### Before Using Figma AI:
- Open Figma and ensure eUI Mobile library is enabled in your file
- Have reference to eUI Mobile showcase: https://euidev.ecdevops.eu/eui-showcase-mobile-18.x/
- Review existing gear management mockups for consistency

---

## Design System Specifications

### Component Library: eUI Mobile 18.x (Ionic-based)

**Navigation Components**:
- `euim-toolbar`: App bar with back button, title, actions
- `ion-header`: Screen header container
- `ion-footer`: Bottom action bar

**Input Components**:
- `ion-input`: Text and numeric input fields
- `ion-button`: Primary, secondary, and icon buttons
- `ion-checkbox`: Checkbox with label
- `ion-label`: Form field labels with required indicators

**Layout Components**:
- `ion-card`: Card container for content grouping
- `ion-item`: List item for form fields
- `ion-content`: Scrollable content container
- `ion-grid`: Grid layout system

**Feedback Components**:
- `ion-progress-bar`: Linear progress indicator
- `euim-alert-message`: Alert/error messages
- `ion-toast`: Temporary notification messages
- `euim-spinner`: Loading indicator

### Typography (eUI Tokens):
- **Headings**: EC Square Sans Pro, Bold
- **Body**: EC Square Sans Pro, Regular
- **Labels**: EC Square Sans Pro, Medium

### Colors (eUI Tokens):
- **Primary**: #004494 (EC Blue)
- **Secondary**: #FFC107 (EC Yellow)
- **Success**: #00823B (Green)
- **Error**: #DA1E28 (Red)
- **Text**: #1D252C (Dark gray)
- **Background**: #FFFFFF (White)
- **Border**: #DFE3E8 (Light gray)

### Spacing (eUI Tokens):
- **XS**: 4px
- **SM**: 8px
- **MD**: 16px
- **LG**: 24px
- **XL**: 32px

### Touch Targets:
- **Minimum**: 44x44 pixels (Apple HIG / Material Design)
- **Preferred**: 48x48 pixels for primary actions

---

## Screen Set to Generate

### 5 Mockup Screens Needed:

1. **Screen 1**: Gear Type & Quantity (Simple Gear - Pots)
2. **Screen 2**: Gear Type & Quantity (Multi-Unit with Duplication Decision)
3. **Screen 3**: Unit Details (Individual Entry in Wizard)
4. **Screen 4**: Single Form for All Identical Units
5. **Screen 5**: Review & Confirm

---

## Prompt 1: Simple Gear Registration (Pots)

### Copy-Paste into Figma AI:

```
Create a mobile app screen for fishing gear registration using eUI Mobile 18.x design system.

DESIGN SYSTEM:
- Use European Commission eUI Mobile components (Ionic-based)
- Primary color: #004494 (EC Blue)
- Typography: EC Square Sans Pro
- 375x812 pixels (iPhone X dimensions)
- White background
- EC visual identity guidelines

SCREEN: Register New Gear - Pots (Simple)

LAYOUT:
- euim-toolbar at top with back arrow (left), title "Register new gear" (center)
- Main content area with form in ion-card

FORM CONTENT:
1. Gear name field (optional)
   - Label: "Gear name (Optional)"
   - ion-input with placeholder "e.g., My pots"

2. Gear type display (read-only, from previous screen)
   - Label: "Type of gear"
   - Display value: "Pots - FPO" in ion-item (not editable)

3. Number of pots field
   - Label: "Number of pots *" (asterisk for required)
   - Stepper control: [-] [50] [+] buttons
   - Buttons are 44x44 pixels minimum
   - Number displayed between buttons (tap to edit)
   - Helper text below: "Total pots on board"

4. Primary action button at bottom
   - Full-width ion-button
   - Text: "Save gear"
   - EC Blue background (#004494)
   - White text

STYLE:
- Clean, minimal, spacious
- 16px padding around content
- Form fields with clear visual separation
- Required fields marked with red *
- Professional, European Commission branding
```

---

## Prompt 2: Multi-Unit Gear with Smart Duplication

### Copy-Paste into Figma AI:

```
Create a mobile app screen for fishing gear registration using eUI Mobile 18.x design system.

DESIGN SYSTEM:
- European Commission eUI Mobile components
- Primary color: #004494
- Typography: EC Square Sans Pro
- 375x812 pixels
- White background

SCREEN: Gear Configuration - Step 2 of 4

LAYOUT:
- euim-toolbar with back arrow, title "Gear configuration"
- Progress indicator below toolbar: ●●○○ with text "Step 2 of 4"
- Main content in ion-card

FORM CONTENT:
1. Summary display (non-editable)
   - "Gear type: Set longlines (LLS)"
   - "Number of lines: 3"
   - In light gray ion-card

2. Smart duplication checkbox
   - Large checkbox (24x24)
   - Label: "All lines have same characteristics"
   - DEFAULT CHECKED state (blue checkmark)
   - Helper text below in smaller font:
     "Check this to save time - we'll duplicate your entries to all 3 lines"
   - Use green info icon next to helper text

3. Navigation buttons at bottom
   - [Back] button (outline style, left side)
   - [Continue] button (solid EC Blue, right side)
   - Both buttons 44px height minimum

VISUAL STYLE:
- Checkbox is prominently displayed
- Helper text is friendly and encouraging
- Clear visual hierarchy
- Spacious layout (24px between sections)
- EC professional appearance
```

---

## Prompt 3: Individual Unit Entry (Wizard Step)

### Copy-Paste into Figma AI:

```
Create a mobile app screen for fishing gear registration wizard using eUI Mobile 18.x design system.

DESIGN SYSTEM:
- European Commission eUI Mobile
- Primary: #004494
- Typography: EC Square Sans Pro
- 375x812 pixels

SCREEN: Line 2 of 3 - Unit Details

LAYOUT:
- euim-toolbar with back arrow, title "Line details"
- Progress indicator: ●●○ with text "Line 2 of 3" below toolbar
- ion-content with form

FORM CONTENT:
1. Screen title
   - Large heading: "Line 2"
   - Subheading: "Enter characteristics for this line"

2. Length field
   - Label: "Length of line *"
   - ion-input with numeric keyboard
   - Placeholder: "0"
   - Unit indicator: "M" (metres) on the right side
   - Helper text: "In metres"

3. Number of hooks field
   - Label: "Number of hooks *"
   - Stepper control: [-] [50] [+]
   - 44x44 pixel buttons
   - Helper text: "Total hooks on this line"

4. Hook size field
   - Label: "Hook size *"
   - ion-select dropdown
   - Placeholder: "Select size"
   - Dropdown arrow indicator

5. Navigation buttons (sticky bottom)
   - [Back: Line 1] (outline, left)
   - [Next: Line 3] (solid EC Blue, right)
   - Both 48px height, full-width combined

STYLE:
- Spacious layout (16px padding)
- Clear visual hierarchy
- Required fields marked with red *
- Progress dots at top for orientation
- Mobile-optimized (thumb-friendly)
```

---

## Prompt 4: Single Form for All Identical Units

### Copy-Paste into Figma AI:

```
Create a mobile app screen for fishing gear registration using eUI Mobile 18.x.

DESIGN SYSTEM:
- eUI Mobile 18.x (European Commission)
- Primary: #004494
- Typography: EC Square Sans Pro  
- 375x812 pixels

SCREEN: Line Characteristics (Applies to All)

LAYOUT:
- euim-toolbar with back, title "Line characteristics"
- Progress: ●●●○ "Step 3 of 4"
- ion-content with form

CONTEXT BAR (at top, light blue background):
- Icon: ℹ️ info icon
- Text: "These characteristics will be applied to all 3 lines"
- Dismissible close X on right

FORM CONTENT:
1. Length of line *
   - ion-input, numeric
   - Unit: "M" on right
   - Placeholder: "0"

2. Number of hooks *
   - Stepper: [-] [50] [+]
   - 44x44 buttons

3. Hook size *
   - ion-select dropdown
   - Placeholder: "Select size"

BOTTOM SECTION (fixed):
- Summary text in gray: "This will create 3 identical lines"
- [Continue to review] button
  - Full width
  - EC Blue solid
  - 48px height

STYLE:
- Friendly informational tone
- Clear that this applies to multiple units
- Spacious, clean layout
- EC professional branding
```

---

## Prompt 5: Review & Confirm Screen

### Copy-Paste into Figma AI:

```
Create a mobile app review screen for fishing gear registration using eUI Mobile 18.x.

DESIGN SYSTEM:
- eUI Mobile 18.x
- Primary: #004494
- Typography: EC Square Sans Pro
- 375x812 pixels

SCREEN: Review & Confirm

LAYOUT:
- euim-toolbar with back, title "Review gear"
- Progress: ●●●● "Step 4 of 4"
- Scrollable content area

CONTENT SECTIONS:

1. Gear Information Card (ion-card)
   - Heading: "Gear Information"
   - Gear name: "Longline 1"
   - Gear type: "Set longlines (LLS)"
   - Number of lines: "3"
   - [Edit] link in top-right (EC Blue text)

2. Units List (3 ion-cards)
   Card 1:
   - Heading: "Line 1" with ✓ icon
   - Length: 1400 M
   - Number of hooks: 50
   - Hook size: 4
   
   Card 2:
   - Heading: "Line 2" with ✓ icon
   - Length: 1400 M
   - Number of hooks: 50
   - Hook size: 4
   
   Card 3:
   - Heading: "Line 3" with ✓ icon
   - Length: 1400 M
   - Number of hooks: 50
   - Hook size: 4

3. Success indicator
   - Green checkmark icon
   - Text: "All information complete"

BOTTOM ACTIONS (fixed footer):
- [Edit gear] button (outline)
- [Save gear] button (solid EC Blue)
- Stack vertically, full width each
- 48px height

STYLE:
- Summary/review aesthetic
- Cards with subtle shadows
- Green checkmarks for completed items
- Clear, scannable layout
- Confident, ready-to-submit feeling
```

---

## Alternative: Manual Design Brief (If Figma AI Doesn't Work)

If Figma AI isn't producing expected results, use this structured brief for your BA:

### Screen-by-Screen Specifications

#### Screen 1: Simple Gear (Pots)
**Components**:
- euim-toolbar: "Register new gear" with back button
- ion-card containing:
  - ion-item: Gear name input (optional)
  - ion-item: Gear type display (read-only) "Pots - FPO"
  - ion-item: Number of pots with +/- stepper (44x44px buttons)
  - Helper text: "Total pots on board"
- ion-button: "Save gear" (full-width, EC Blue)

**Layout**:
- 16px padding throughout
- 8px spacing between form items
- Stepper centered in item

---

#### Screen 2: Duplication Decision
**Components**:
- euim-toolbar: "Gear configuration"
- Progress bar component: ●●○○ "Step 2 of 4"
- ion-card (summary):
  - Read-only display: "Set longlines (LLS)"
  - Read-only display: "Number of lines: 3"
- ion-card (decision):
  - Large ion-checkbox (24x24, checked state)
  - Label: "All lines have same characteristics"
  - Helper text with info icon
- Bottom buttons: [Back] [Continue]

**Interactions**:
- Checkbox toggles between checked/unchecked
- Continue button proceeds to next appropriate screen based on checkbox state

---

#### Screen 3: Individual Unit Entry
**Components**:
- euim-toolbar: "Line details"
- Progress: ●●○ "Line 2 of 3"
- Screen title: "Line 2" (large heading)
- Form fields in ion-items:
  - Length of line * (numeric input, "M" unit)
  - Number of hooks * (stepper control)
  - Hook size * (select dropdown)
- Bottom navigation:
  - [Back: Line 1] (outline)
  - [Next: Line 3] (solid)

**Visual Details**:
- Progress dots use EC Blue for completed
- Required fields have red asterisk
- Buttons are side-by-side at bottom
- Form fields have proper spacing (8px between)

---

#### Screen 4: Single Form (All Identical)
**Components**:
- euim-toolbar: "Line characteristics"
- Progress: ●●●○ "Step 3 of 4"
- Info banner (light blue background):
  - Icon + "These characteristics will be applied to all 3 lines"
- Form fields (same as Screen 3 but context different)
- Summary text: "This will create 3 identical lines"
- [Continue to review] button

**Visual Details**:
- Info banner uses EC Blue tint (#E6F0F8)
- Friendly, helpful tone
- Clear indication this is applying to multiple units

---

#### Screen 5: Review & Confirm
**Components**:
- euim-toolbar: "Review gear"
- Progress: ●●●● "Step 4 of 4"
- Gear info ion-card:
  - Section heading with [Edit] link
  - Key-value pairs (gear name, type, count)
- Unit cards (3x ion-card):
  - "Line 1" with green ✓
  - Characteristics listed
  - Compact display
- Success indicator:
  - Green checkmark + "All information complete"
- Bottom actions (stacked):
  - [Edit gear] (outline)
  - [Save gear] (solid EC Blue)

**Visual Details**:
- Scannable card layout
- Green checkmarks for completed sections
- Clear data hierarchy
- Confident, ready-to-submit aesthetic

---

## Design Principles to Follow

### 1. Mobile-First (Luke Wroblewski)
- ✅ One primary action per screen
- ✅ Stepper controls instead of dropdowns for quantities
- ✅ Numeric keyboard for number inputs
- ✅ Clear progress indicators
- ✅ Linear flow (no hidden content)

### 2. eUI Compliance
- ✅ Use only eUI Mobile components
- ✅ Follow EC color palette
- ✅ EC Square Sans Pro typography
- ✅ Official EC branding guidelines

### 3. Accessibility
- ✅ 44x44px minimum touch targets
- ✅ High contrast ratios (WCAG AA)
- ✅ Clear labels for all inputs
- ✅ Required field indicators
- ✅ Error message associations

### 4. Consistency
- ✅ Match existing CALYPSO app styling
- ✅ Consistent spacing throughout
- ✅ Standard navigation patterns
- ✅ Familiar eUI patterns

---

## Quick Reference: Component Usage Map

| Need | eUI Mobile Component | Properties |
|------|---------------------|------------|
| App bar | `euim-toolbar` | Back button, title, actions |
| Text input | `ion-input` | Type="text" or "number" |
| Number stepper | `ion-button` (3x) | Icon="+", icon="-", and display value |
| Checkbox | `ion-checkbox` | Checked state, label |
| Dropdown | `ion-select` | With ion-select-option children |
| Primary button | `ion-button` | Expand="block", color="primary" |
| Card | `ion-card` | With ion-card-content |
| Form field | `ion-item` | With ion-label + ion-input |
| Progress bar | `ion-progress-bar` | Value=0.5 for 50% |
| Progress dots | Custom | Use ● (filled) ○ (empty) with EC Blue |
| Alert/Info | `euim-alert-message` | Type="info" |
| Success message | `ion-toast` | Color="success", duration=2000 |

---

## Color Usage Guide

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Primary buttons | EC Blue | #004494 | Save, Continue, Next |
| Secondary buttons | Outline | #004494 border | Back, Cancel, Edit |
| Required indicators | Red | #DA1E28 | Asterisks (*) |
| Success | Green | #00823B | Checkmarks, confirmations |
| Error | Red | #DA1E28 | Error messages, validation |
| Progress (active) | EC Blue | #004494 | Filled progress dots |
| Progress (inactive) | Gray | #DFE3E8 | Empty progress dots |
| Text (primary) | Dark Gray | #1D252C | Headings, labels |
| Text (secondary) | Gray | #73818C | Helper text, hints |
| Background | White | #FFFFFF | Screen background |
| Card background | White | #FFFFFF | With shadow |

---

## Tips for Best Results with Figma AI

### Do's:
✅ Be specific about component names (use eUI/Ionic names)
✅ Specify exact dimensions (375x812 for mobile)
✅ Mention EC branding explicitly
✅ Describe layout in top-to-bottom order
✅ Specify touch target sizes (44x44px)
✅ Include helper text and hints

### Don'ts:
❌ Don't ask for complex interactions (Figma AI does static screens)
❌ Don't expect perfect first try (iterate and refine)
❌ Don't forget to mention European Commission branding
❌ Don't use generic components (specify eUI equivalents)

---

## Iteration & Refinement

If Figma AI results need adjustment:

1. **Wrong components**: Regenerate with more specific eUI component names
2. **Wrong colors**: Specify exact hex codes in prompt
3. **Layout issues**: Be more explicit about spacing and order
4. **Size problems**: Mention 375x812 dimensions and 44px touch targets
5. **Branding off**: Emphasize EC visual identity and eUI design system

---

## Example Follow-Up Prompts

**If progress indicator wrong**:
```
Update the progress indicator to use filled circles (●) for completed 
steps and empty circles (○) for upcoming steps. Use EC Blue (#004494) 
for filled circles and light gray (#DFE3E8) for empty. Display as: 
●●○○ with "Step 2 of 4" text below in gray.
```

**If stepper buttons too small**:
```
Increase the stepper button sizes to 44x44 pixels minimum for 
thumb-friendly tapping. Buttons should be: [-] [50] [+] with the 
number in between being directly editable by tapping it.
```

**If missing EC branding**:
```
Add European Commission visual identity: EC Square Sans Pro font 
throughout, EC Blue (#004494) for primary actions, and maintain 
professional government app aesthetic following EC design guidelines.
```

---

## Validation Checklist

Before finalizing mockups, verify:

- [ ] All components from eUI Mobile library (not generic)
- [ ] EC Blue (#004494) used for primary actions
- [ ] EC Square Sans Pro typography
- [ ] 375x812 pixel dimensions (or state other target)
- [ ] 44x44px minimum touch targets for all interactive elements
- [ ] Required fields marked with red *
- [ ] Helper text provided for complex fields
- [ ] Progress indicators on wizard screens
- [ ] Back/Next navigation on wizard screens
- [ ] Consistent spacing (16px padding, 8px between fields)
- [ ] Matches existing CALYPSO app aesthetic
- [ ] Professional EC government branding
- [ ] Accessible (high contrast, clear labels)

---

## Resources & References

### Online Resources:
- **eUI Mobile Showcase**: https://euidev.ecdevops.eu/eui-showcase-mobile-18.x/
- **eUI Design Tokens**: https://www.figma.com/community/file/1052857333027422402
- **eUI Mobile Components**: https://www.figma.com/community/file/1052862901059626182
- **Ionic Components Docs**: https://ionicframework.com/docs/components

### Project References:
- **User Story**: SSF-143A_Register_New_Gear_Dynamic_Characteristics_Mobile.md
- **Business Rules**: GEAR_CHARACTERISTICS_BUSINESS_RULES.md
- **Data Model**: GEAR_REGISTRATION_DATA_MODEL.md
- **Existing Mockups**: SSF DOCS/Mockups SSF FIGMA/Gear Management/

### Design Principles:
- **Luke Wroblewski**: Mobile form design best practices
- **EC Guidelines**: 2025_Guidelines_for_partners.pdf

---

## Contact for Help

**eUI Support**:
- Helpdesk request: helpdesk support request
- Teams community channels
- Email: helpdesk support request

**Internal Team**:
- Business Analyst: For design questions
- Product Manager: For business rule clarifications
- Tech Lead: For technical feasibility

---

*This prompt guide is part of the Gear Management epic (PI 02) and supports user story SSF-143A.*

**Version**: 1.0  
**Last Updated**: November 14, 2025  
**Status**: Ready to Use
