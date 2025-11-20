# SSF-143D: [MOB] Register New Gear - Complex & Edge Case Gear Types

**JIRA Ticket**: SSF-143D (Split from original SSF-143)  
**Summary**: [MOB] Register new gear - Complex & Edge Case Gear Types (12 types)  
**Epic**: Gear Management  
**Sprint**: Sprint 7-8 (or later PI)  
**PI**: PI 03  
**Story Points**: 3  
**Assignee**: [Mobile Developer]  
**Priority**: Low  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Complete the gear type coverage by implementing the final 12 complex and edge case gear types. This story includes gear types that require workshop decisions (Fyke nets), unique multi-measurement patterns (Aerial traps), and free-text handling (Miscellaneous gears). Achieves 100% coverage of all 72 EU-regulated gear types. This story should NOT start until SSF-143A, B, C are complete and Gear Registration Workshop has resolved open questions.
{panel}

{panel:title=Business rules}
*Context*
After SSF-143A/B/C, 60 gear types are supported covering ~95% of actual fishing activity. This story adds the final 12 types that represent edge cases, rare usage, or require special handling. These types were intentionally deferred to validate standard patterns first and to allow time for workshop decisions on ambiguous cases.

*Previous Coverage*
- SSF-143A: 5 pilot types (framework + common patterns)
- SSF-143B: 15 common types (pattern expansion)
- SSF-143C: 40 standard types (bulk configuration)
- **Total before this story**: 60 types

*This Story Adds*: 12 complex/edge case gear types

**12 Gear Types by Complexity**:

**MOST COMPLEX - Requires Workshop Decision** (1 type):
1. **FYK - Fyke nets**
   - Requires: Overall length + Height of wings/leaders + Number of nets
   - **Open Questions**:
     * Is "overall length" a SINGLE measurement or sum of (wings + leaders)?
     * Is "height of wings/leaders" ONE height or separate for each?
     * Register as gear set (like TBB) or individual units?
   - **Must be resolved in Gear Registration Workshop BEFORE implementation**
   - **Estimated Pattern**: Likely multi-unit with 2-3 characteristics per net

**UNIQUE MULTI-MEASUREMENT** (1 type):
2. **FAR - Aerial traps**
   - Requires: 4 SEPARATE measurements
     * Length underwater (m)
     * Height underwater (m)
     * Length aerial (m)
     * Height aerial (m)
   - **Challenge**: How to present 4 fields clearly on mobile
   - **Approach**: Single screen, grouped sections (Underwater | Aerial)

**FREE-TEXT GEAR TYPES** (9 types - Miscellaneous):
3. **HAR** - Harpoons
4. **MHI** - Hand implements (wrenching, clamps, tongs, rakes, spears)
5. **MPM** - Pumps
6. **MPN** - Pushnets
7. **MSP** - Scoopnets
8. **MDR** - Drive-in nets
9. **MDV** - Diving
10. **HMX** - Harvesting machines (not specified)
11. **MIS** - Gear (not specified)

**All require**: Dimensions (free-text) + Description (free-text) + Number of gears

**Challenge**: How to validate free-text "dimensions"?

**ULTIMATE CATCH-ALL** (1 type):
12. **FIX** - Traps (not elsewhere specified)
   - Same as miscellaneous: Dimensions + Description + Number

*New Technical Patterns Required*

**Pattern 1: Quad-Measurement** (FAR only)
- Four separate numeric fields
- Grouped presentation (underwater vs aerial)
- All four mandatory
- Visual layout challenge on mobile

**Pattern 2: Free-Text with Guidance** (10 types)
- "Dimensions" field with examples/templates
- "Description" field with character limit
- "Number of gears" with stepper
- Validation challenge: How to validate free-text dimensions?

*Free-Text Handling Approach*

**Problem**: Regulation says "dimensions and description" but doesn't specify format

**Options Considered**:

**Option A: Fully Free-Text** (Simplest)
```
Dimensions: [text area]
Examples: "Length: 2m, Width: 0.5m" or "Diameter: 30cm"
```
✅ Flexible, fishers use natural language
❌ Difficult to validate, inconsistent data

**Option B: Semi-Structured** (Recommended)
```
Dimension type: [Length | Width | Diameter | Other] (dropdown)
Value: [number] [unit dropdown: m/cm/mm]
+ Add another dimension (repeatable)

Description: [text area]
```
✅ Some structure for validation
✅ Flexible enough for variety
❌ More complex UI

**Option C: Common Templates** (User-Friendly)
```
For Harpoons, show template:
- Length: [__] m
- Weight: [__] kg (optional)
- Type: [Traditional | Modern]

Description: [text area for additional notes]
```
✅ Guided, consistent data
✅ Faster for users
❌ Need templates for each type

**Recommendation**: Use Option B (Semi-Structured) for MVP, consider templates in future enhancement

*Workshop Prerequisites*

**CRITICAL**: Fyke Nets (FYK) CANNOT be implemented until workshop resolves:

1. **Structure Interpretation**: 
   - Q: Is "overall length" one measurement or calculated?
   - Q: Is "height of wings/leaders" singular or multiple?
   
2. **Registration Model**:
   - Q: Register as set (one entry, N nets) or individually?
   - Q: Mixed-size nets allowed in same set?

3. **Data Entry**:
   - Q: How to guide fishers on "wings" vs "leaders" distinction?
   - Q: Need visual diagram in app?

**Workshop Must Produce**: Clear specification document for FYK structure

*Suggestion 01*: For miscellaneous types, provide photo upload option so fishers can visually document their gear

{*}Suggestion 02{*}: Create gear type suggestion flow: If fisher selects MIS (catch-all), ask clarifying questions to guide to more specific type

{color:#ff8b00}*Questions / Ideas*{color}
Should free-text dimensions be OCR-scanned if fisher uploads photo of gear specs?
Should we crowd-source common dimension patterns from fisher submissions?
Should MDV (Diving) even be a "gear" or reclassified as fishing method?
{panel}

{panel:title=Dependencies}
SSF-143A, B, C: All complete and stable
Gear Registration Workshop: Completed with FYK specification
SSF-147: Backend supports free-text characteristics

Technical Dependencies:
- Framework proven with 60 types
- No critical bugs outstanding
- Team familiar with configuration approach
- Free-text validation strategy approved

Business Dependencies:
- Workshop decisions documented
- Client approval on free-text approach
- FYK specification clear and agreed
- User feedback on 60 types reviewed

Workshop Outputs Required:
- Fyke nets structure specification
- Free-text validation guidelines
- Aerial trap UI layout approval
- Miscellaneous gear handling policy
{panel}

{panel:title=Mockups}
**New mockups required** for:
1. Aerial trap form (4-measurement layout)
2. Fyke nets form (post-workshop)
3. Free-text gear form (semi-structured)

Should be created AFTER workshop using FIGMA_AI_PROMPT document pattern
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Implement aerial trap four-measurement pattern*{color}
*GIVEN* fisher selects "Aerial traps" (FAR)
*WHEN* characteristics form is displayed
*THEN* show single screen with two grouped sections:
- **Underwater measurements**
  * Length (m) *
  * Height (m) *
- **Aerial measurements**
  * Length (m) *
  * Height (m) *
*AND* all four fields required
*AND* validate all > 0
*AND* group headings use visual separation (card/divider)

{color:#4c9aff}*02 - Implement fyke nets per workshop specification*{color}
*GIVEN* Gear Registration Workshop has specified FYK structure
*AND* fisher selects "Fyke nets" (FYK)
*WHEN* form is displayed
*THEN* implement per workshop decision
*AND* follow agreed registration model (set vs individual)
*AND* collect characteristics as specified
*AND* validate per workshop rules

**NOTE**: This AC will be updated after workshop

{color:#4c9aff}*03 - Implement semi-structured free-text for miscellaneous gears*{color}
*GIVEN* fisher selects any miscellaneous type (HAR, MHI, MPM, etc.)
*WHEN* form is displayed
*THEN* show semi-structured dimensions input:
- Dimension type dropdown: [Length | Width | Diameter | Height | Other]
- Value: numeric input
- Unit: [m | cm | mm] dropdown
- [+ Add another dimension] button (repeatable)
*AND* "Description" text area (max 500 chars)
*AND* "Number of gears" stepper

{color:#4c9aff}*04 - Provide examples/templates for free-text inputs*{color}
*GIVEN* fisher enters dimensions for "Harpoons" (HAR)
*WHEN* dimensions section is displayed
*THEN* show placeholder/example: "e.g., Length: 2.5m"
*AND* show helper text: "Add all relevant dimensions"
*WHEN* description field focused
*THEN* show example: "e.g., Traditional hand-thrown harpoon, wooden shaft"

{color:#4c9aff}*05 - Validate free-text has minimum content*{color}
*GIVEN* fisher enters dimensions for miscellaneous gear
*WHEN* validation runs
*THEN* require at least 1 dimension entry
*AND* require description field not empty (min 10 characters)
*AND* require number of gears > 0
*AND* show clear error if any missing

{color:#4c9aff}*06 - Handle "catch-all" categories with guidance*{color}
*GIVEN* fisher selects "Gear (not elsewhere specified)" (MIS)
*WHEN* form is displayed
*THEN* show warning message: "Please use a more specific gear type if possible"
*AND* show link to gear type selection to change
*AND* allow proceeding if fisher confirms MIS is correct

{color:#4c9aff}*07 - Support repeatable dimension entries*{color}
*GIVEN* fisher adding dimensions for gear
*WHEN* fisher taps "+ Add another dimension"
*THEN* add new dimension entry row
*AND* allow up to 5 dimension entries
*AND* each dimension can be removed (X button)
*AND* at least 1 dimension must remain

{color:#4c9aff}*08 - Construct payload with free-text data*{color}
*GIVEN* fisher completes miscellaneous gear registration
*WHEN* payload is constructed
*THEN* include:
{
  "gear_set_characteristics": {
    "dimensions": [
      {"type": "length", "value": 2.5, "unit": "m"},
      {"type": "width", "value": 0.5, "unit": "m"}
    ],
    "description": "Traditional harpoon...",
    "number_of_gears": 2
  }
}

{color:#4c9aff}*09 - Complete coverage reaches 100% (72 types)*{color}
*GIVEN* SSF-143D is complete
*WHEN* all gear types counted
*THEN* system supports all 72 EU-regulated gear types
*AND* dropdown shows all 72 types
*AND* all types functional end-to-end

{color:#4c9aff}*10 - Workshop decisions implemented correctly*{color}
*GIVEN* workshop specified approach for FYK
*WHEN* FYK implementation reviewed
*THEN* implementation must match workshop specification exactly
*AND* all workshop questions answered in code
*AND* edge cases from workshop handled

h3. Additional Acceptance Criteria

**Workshop Dependency**:
* FYK implementation blocked until workshop complete
* Workshop specification document created and approved
* Team aligned on approach before coding begins
* Client validated the approach

**Free-Text Quality**:
* Examples/templates helpful and clear
* Validation prevents completely empty data
* Character limits prevent abuse
* Data stored structured (not just blob)

**Edge Cases**:
* Diving (MDV) - Is this even a gear? Discuss with client
* All "not specified" categories guide to specific types when possible
* Rare types still fully functional despite low usage

**Complete Coverage**:
* All 72 types in system
* No gaps in regulation compliance
* Future-proof for regulation updates
* System ready for production
```

---

## ✅ Tasks Checklist

### Workshop Coordination
- [ ] Schedule Gear Registration Workshop
- [ ] Prepare workshop materials (QA file, mockups, questions)
- [ ] Conduct workshop with BA, Tech Lead, Product Manager
- [ ] Document workshop decisions
- [ ] Get client approval on FYK specification
- [ ] Create FYK implementation specification

### Fyke Nets Implementation (FYK) - AFTER WORKSHOP
- [ ] Review workshop specification for FYK
- [ ] Implement FYK structure per workshop decision
- [ ] Create FYK-specific form/wizard
- [ ] Implement FYK validation rules
- [ ] Test FYK registration end-to-end
- [ ] Test edge cases identified in workshop
- [ ] Document FYK implementation for future reference

### Aerial Traps Implementation (FAR)
- [ ] Design 4-measurement layout (mobile-friendly)
- [ ] Implement grouped sections (Underwater | Aerial)
- [ ] Create labels: "Length underwater", "Height underwater", etc.
- [ ] Implement validation for all 4 fields
- [ ] Test on various screen sizes
- [ ] Get BA/designer review on layout
- [ ] Test end-to-end

### Free-Text Framework (for 9 miscellaneous types)
- [ ] Design semi-structured dimensions input
- [ ] Implement dimension type dropdown
- [ ] Implement value + unit inputs
- [ ] Implement repeatable dimension rows
- [ ] Implement "Add dimension" button
- [ ] Implement "Remove dimension" button (X)
- [ ] Create description text area with counter
- [ ] Add examples/templates per gear type

### Miscellaneous Gear Type 1: HAR (Harpoons)
- [ ] Add HAR configuration
- [ ] Create HAR-specific examples ("Length: X m")
- [ ] Test free-text input
- [ ] Test validation
- [ ] Test submission and persistence

### Miscellaneous Gear Types 2-9 (MHI, MPM, MPN, MSP, MDR, MDV, HMX, MIS)
- [ ] Add configurations for all 8 types
- [ ] Create type-specific examples for each
- [ ] Test 3 types end-to-end (sample)
- [ ] Validate pattern works for all
- [ ] Special handling for MDV (Diving) - discuss classification
- [ ] Test MIS (ultimate catch-all) with guidance flow

### Traps Not Specified (FIX)
- [ ] Add FIX configuration
- [ ] Implement free-text pattern (same as miscellaneous)
- [ ] Test end-to-end
- [ ] Validate with backend

### Validation for Free-Text
- [ ] Require at least 1 dimension entry
- [ ] Require description min 10 characters
- [ ] Validate numeric values in dimensions
- [ ] Prevent submission with empty free-text
- [ ] Test edge cases (very long descriptions, many dimensions)

### Payload Construction for Complex Types
- [ ] Implement FAR payload (4 separate fields)
- [ ] Implement FYK payload (per workshop decision)
- [ ] Implement miscellaneous payload (structured dimensions array)
- [ ] Test backend accepts all new payload structures
- [ ] Validate data persists correctly

### UI/UX Refinements
- [ ] Create clear grouping for FAR measurements
- [ ] Add visual separators (cards, dividers)
- [ ] Implement guidance for "not specified" types
- [ ] Add examples throughout free-text forms
- [ ] Test usability on real devices

### Integration Testing
- [ ] Test all 12 new types with backend
- [ ] Verify data persistence for complex types
- [ ] Test retrieval of complex gear registrations
- [ ] End-to-end for FYK, FAR, 3 miscellaneous types

### Regression Testing
- [ ] Spot-check 10 types from SSF-143A/B/C
- [ ] Verify no regressions with 72 types loaded
- [ ] Test search/filter with complete set
- [ ] Validate performance acceptable

### Final System Validation
- [ ] Verify all 72 types functional
- [ ] Test gear type dropdown with complete set
- [ ] Performance testing with 72 types
- [ ] Memory usage validation
- [ ] Complete coverage validation

### Documentation
- [ ] Document workshop decisions (FYK)
- [ ] Document free-text handling approach
- [ ] Document FAR layout decisions
- [ ] Create guide for rare/unusual gear types
- [ ] Update Business Rules doc if needed
- [ ] Final configuration documentation

---

## 📊 Complex Gear Types Detail

### Aerial Traps (FAR) - 4 Measurements

**Layout Concept**:
```
┌─────────────────────────────────┐
│ Aerial Trap Characteristics     │
├─────────────────────────────────┤
│ 🌊 UNDERWATER SECTION           │
│ Length underwater * [___] M     │
│ Height underwater * [___] M     │
│                                  │
│ ☁️ AERIAL SECTION                │
│ Length aerial * [___] M          │
│ Height aerial * [___] M          │
│                                  │
│ [Save Gear]                      │
└─────────────────────────────────┘
```

**Payload**:
```json
{
  "gear_type_code": "FAR",
  "gear_set_characteristics": {
    "length_underwater_m": 5.0,
    "height_underwater_m": 2.0,
    "length_aerial_m": 3.0,
    "height_aerial_m": 1.5
  }
}
```

---

### Fyke Nets (FYK) - Workshop Dependent

**Current Understanding** (to be validated):
- Overall length = wings + leaders combined
- Height = one measurement for entire net
- Number = count of nets in set

**Possible Implementation** (after workshop):
```
Step 1: Number of fyke nets [stepper]
Step 2: All identical? [checkbox]
Step 3: Per net characteristics
  - Overall length of wings/leaders (m) *
  - Height (m) *
Step 4: Review & Save
```

**TO BE DETERMINED IN WORKSHOP**

---

### Miscellaneous Types (9 types) - Semi-Structured

**Example: Harpoons (HAR)**

**Form Layout**:
```
┌─────────────────────────────────┐
│ Harpoon Characteristics          │
├─────────────────────────────────┤
│ Dimensions                       │
│                                  │
│ Dimension 1                      │
│ Type: [Length ▼]                 │
│ Value: [2.5] Unit: [m ▼]        │
│ [×]                              │
│                                  │
│ [+ Add dimension]                │
│                                  │
│ Description *                    │
│ [text area]                      │
│ Example: "Traditional hand-      │
│ thrown harpoon, wooden shaft"    │
│                                  │
│ Number of harpoons * [2] +/-     │
│                                  │
│ [Save Gear]                      │
└─────────────────────────────────┘
```

**Payload**:
```json
{
  "gear_type_code": "HAR",
  "gear_set_characteristics": {
    "dimensions": [
      {"type": "length", "value": 2.5, "unit": "m"}
    ],
    "description": "Traditional hand-thrown harpoon...",
    "number_of_gears": 2
  }
}
```

---

### FIX - Traps Not Specified

**Same pattern as miscellaneous**, but in TRAPS category

**Guidance to Add**:
```
⚠️ "Traps (not elsewhere specified)" should only be used if your trap 
doesn't fit any other trap category. Consider:
- Pots (FPO) if using pot/creel traps
- Fyke nets (FYK) if using wing/leader nets
- Stow nets (FSN) if using framed nets
- Barriers (FWR) if using fixed structures
```

---

## 🔗 Related Stories

- **SSF-143A**: Framework + 5 pilots (dependency)
- **SSF-143B**: 15 common types (dependency)
- **SSF-143C**: 40 standard types (dependency)
- **SSF-147**: Backend gear registration (must support free-text)
- **Gear Registration Workshop**: Required before implementation

---

## 📋 Workshop Agenda (To Be Scheduled)

### Topics to Resolve:

1. **Fyke Nets Structure** (30 min)
   - Review regulation wording
   - Clarify "overall length" calculation
   - Decide on wings/leaders measurement approach
   - Agree on registration model (set vs individual)

2. **Free-Text Validation** (20 min)
   - How much structure to enforce?
   - Validation rules for dimensions
   - Accept Option A, B, or C approach?

3. **Diving Classification** (10 min)
   - Is MDV a "gear" or should it be reclassified?
   - If gear, what dimensions make sense?

4. **Edge Case Handling** (10 min)
   - Guidance for "not specified" categories
   - When to allow MIS/FIX vs guide to specific

**Total**: 70 minutes  
**Attendees**: BA, Tech Lead, Product Manager, Mobile Dev (optional)  
**Output**: Specification document for SSF-143D implementation

---

**Last Updated**: November 14, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Blocked - Awaiting Gear Registration Workshop

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
