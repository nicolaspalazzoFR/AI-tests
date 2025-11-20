# SSF-143B: [MOB] Register New Gear - Common Gear Types Expansion

**JIRA Ticket**: SSF-143B (Split from original SSF-143)  
**Summary**: [MOB] Register new gear - Common Gear Types Expansion (15 types)  
**Epic**: Gear Management  
**Sprint**: Sprint 4  
**PI**: PI 02  
**Story Points**: 2  
**Assignee**: [Mobile Developer]  
**Priority**: Medium  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Expand the dynamic gear characteristics wizard (SSF-143A) to support 15 additional common gear types. This story reuses the existing framework, patterns, and components established in SSF-143A, adding configuration and validation for the most commonly used gear types after the initial 5 pilots. No new technical patterns are introduced - this is pure expansion using proven approaches.
{panel}

{panel:title=Business rules}
*Context*
SSF-143A established the wizard framework and validated 5 pilot gear types (FPO, GNS, OTB, TBB, LLS). This story expands to 15 additional commonly-used gear types, bringing total coverage from 5 to 20 gear types (~30% of all types, but ~85% of actual fishing activity).

*Reference Documents*
- Business Rules: GEAR_CHARACTERISTICS_BUSINESS_RULES.md
- Gear Analysis: Gear_Registration_Analysis.xlsx (filter by "Simple" and "Medium")
- Data Model: GEAR_REGISTRATION_DATA_MODEL.md  
- Framework: SSF-143A (wizard pattern, smart duplication, validation)

*15 Gear Types to Add*

These types all use patterns already implemented in SSF-143A:

**GILLNET VARIANTS** (6 types - Pattern: Dual measurement, no units):
1. **GND** - Gillnets (drift): Length + Height
2. **GNC** - Gillnets (circling): Length + Height  
3. **GNF** - Gillnets fixed (on stakes): Length + Height
4. **GTN** - Combined gillnets-trammel nets: Length + Height
5. **GTR** - Trammel nets: Length + Height
6. **GEN** - Gillnets (not specified): Length + Height

**TRAWL VARIANTS** (4 types):
7. **TBN** - Nephrops trawl: Model (optional) + Perimeter (Pattern like OTB)
8. **TBS** - Shrimp trawl: Model (optional) + Perimeter (Pattern like OTB)
9. **PTB** - Bottom pair trawl: Model (optional) + Perimeter (Pattern like OTB)
10. **PTM** - Mid-water pair trawl: Model (optional) + Perimeter (Pattern like OTB)

**SEINE VARIANTS** (4 types - Pattern: Dual measurement, no units):
11. **SDN** - Danish anchor seine: Length + Height
12. **SSC** - Scottish seine: Length + Height
13. **SPR** - Pair seine: Length + Height
14. **SV** - Boat/vessel seine: Length + Height

**HOOKS/LINES VARIANT** (1 type):
15. **LHP** - Handlines (hand operated): 3 measurements (Pattern like LLS but simpler)
    - Number of lines + Number of hooks + Hook size

*Pattern Reuse Summary*

| Pattern | Used By | Already Implemented In |
|---------|---------|----------------------|
| Dual measurement (L+H) | 10 types | GNS (SSF-143A) |
| Optional + Mandatory | 4 types | OTB (SSF-143A) |
| Triple measurement | 1 type | LLS (SSF-143A) |

**100% pattern reuse** = Faster implementation, lower risk!

*Implementation Approach*

**NOT Building**: New UI components, new validation patterns, new wizard flows
**Building**: Configuration entries for 15 new gear types

**Configuration-Driven Design**:
```javascript
// Add to gear_type_config.json
{
  "GND": {
    "name": "Gillnets (drift)",
    "category": "GILLNETS",
    "pattern": "dual_measurement",
    "wizard_steps": 1,  // Single screen
    "characteristics": [
      {"code": "GM", "name": "Overall length", "type": "MEASURE", "unit": "m", "required": true},
      {"code": "HE", "name": "Height", "type": "MEASURE", "unit": "m", "required": true}
    ]
  }
}
```

**System automatically**:
- Generates appropriate form fields
- Applies validation rules
- Constructs correct payload
- No custom code per gear type!

*Why These 15 Types*

From Gear_Registration_Analysis.xlsx:
- All rated "Simple" or "Medium" complexity
- All use existing patterns (no R&D needed)
- Together with SSF-143A, cover 85% of actual fishing activity
- High value, low risk delivery

*Testing Strategy*

**Regression Testing**: Ensure SSF-143A pilot types still work
**New Type Testing**: Test each of 15 new types
**Pattern Validation**: Confirm patterns work for all similar types
**Integration Testing**: End-to-end with backend (SSF-147)

*Suggestion 01*: Group gear types by pattern in UI to help fishers understand similarities (e.g., "All seine types have same measurements")

{*}Suggestion 02{*}: Add "Recently used gear types" quick access based on vessel's history

{color:#ff8b00}*Questions / Ideas*{color}
Should we display pattern-specific help text? (e.g., "All gillnet types require length and height")
Should we warn fishers if selecting unusual gear type for their vessel size?
Should we provide examples of typical values for each gear type?
{panel}

{panel:title=Dependencies}
SSF-143A: Framework must be complete and tested
SSF-147: Backend must support new gear types (configuration update)

Technical Dependencies:
- SSF-143A wizard framework functional
- Configuration system for gear types
- Validation framework extensible
- Backend gear type validation updated

Business Dependencies:
- SSF-143A tested and validated by users
- No critical issues from pilot implementation
- Pattern confirmation from team
{panel}

{panel:title=Mockups}
**Reuses existing mockups from SSF-143A** - no new screens needed

Mockup variations needed (optional):
- Example of gillnet form (dual measurement pattern)
- Example of trawl form (optional + mandatory pattern)
- Example of seine form (dual measurement pattern)

Can be simple annotations on SSF-143A mockups showing field label changes
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Support all 6 gillnet variants with same pattern*{color}
*GIVEN* fisher selects gear type "Gillnets (drift)" (GND)
*WHEN* characteristics form is displayed
*THEN* show single-screen form with two fields:
- "Overall length (m)" * (required)
- "Height (m)" * (required)
*AND* both use numeric keyboard
*AND* validate both > 0
*AND* no wizard needed (pattern like GNS from SSF-143A)
*AND* same behavior for: GNC, GNF, GTN, GTR, GEN

{color:#4c9aff}*02 - Support all 4 trawl variants with optional model*{color}
*GIVEN* fisher selects "Nephrops trawl" (TBN)
*WHEN* characteristics form is displayed
*THEN* show single-screen form with:
- "Model of trawl (Optional)" text field
- "Perimeter of opening (m)" * (required) numeric field
*AND* allow submission with empty model
*AND* validate perimeter > 0
*AND* same pattern for: TBS, PTB, PTM

{color:#4c9aff}*03 - Support all 4 seine types with same pattern*{color}
*GIVEN* fisher selects "Danish anchor seine" (SDN)
*WHEN* characteristics form is displayed
*THEN* show single-screen form with:
- "Overall length (m)" * (required)
- "Maximum height (m)" * (required)
*AND* validate both > 0
*AND* same pattern for: SSC, SPR, SV

{color:#4c9aff}*04 - Support handlines with triple measurement*{color}
*GIVEN* fisher selects "Handlines and pole lines (hand operated)" (LHP)
*WHEN* characteristics form is displayed
*THEN* show single-screen form with three fields:
- "Total number of lines" * (stepper control)
- "Total number of hooks" * (stepper control)
- "Hook size" * (numeric or select)
*AND* validate all > 0
*AND* no sub-units wizard (pattern like simple triple-field from LLS without units)

{color:#4c9aff}*05 - Configuration-driven field generation*{color}
*GIVEN* gear type configuration entry exists for "GND"
*WHEN* fisher selects that gear type
*THEN* system reads configuration
*AND* dynamically generates form fields per config
*AND* applies validation rules from config
*AND* NO custom code for this specific gear type

{color:#4c9aff}*06 - Validate using configuration rules*{color}
*GIVEN* configuration specifies field "overall_length_m" is required, type MEASURE
*WHEN* fisher leaves field empty or enters invalid value
*THEN* validation error appears
*AND* error message generated from configuration
*AND* field highlighted per SSF-143A validation pattern

{color:#4c9aff}*07 - Maintain wizard framework compatibility*{color}
*GIVEN* any of the 15 new gear types selected
*WHEN* form is generated
*THEN* use same wizard components from SSF-143A
*AND* same navigation patterns (back/next)
*AND* same progress indicators (if multi-step)
*AND* same validation feedback (errors, hints)
*AND* same eUI Mobile 18.x styling

{color:#4c9aff}*08 - Submit correct payload structure per type*{color}
*GIVEN* fisher completes registration for "Gillnet (drift)" (GND)
*WHEN* gear is saved
*THEN* construct payload:
{
  "gear_type_code": "GND",
  "gear_set_characteristics": {
    "overall_length_m": <value>,
    "height_m": <value>
  },
  "gear_units": []
}
*AND* submit to backend (SSF-147)

{color:#4c9aff}*09 - Handle backend validation for new types*{color}
*GIVEN* backend rejects submission with validation error for new gear type
*WHEN* error response received
*THEN* display error message to fisher
*AND* allow correction
*AND* highlight specific field if field-level error

{color:#4c9aff}*10 - Regression test pilot gear types*{color}
*GIVEN* SSF-143A pilot types (FPO, GNS, OTB, TBB, LLS) were working
*WHEN* SSF-143B is deployed
*THEN* all 5 pilot types must still function correctly
*AND* no regressions in wizard flow
*AND* no regressions in validation
*AND* no regressions in payload construction

h3. Additional Acceptance Criteria

**Pattern Consistency**:
* All gillnet variants (GND-GEN) must behave identically except gear type name
* All trawl variants with optional model must behave identically
* All seine types must behave identically
* Field labels may differ but patterns are consistent

**Performance**:
* No performance degradation with 20 gear types vs 5
* Configuration loaded efficiently (cached)
* Form generation remains fast (< 300ms)

**Data Quality**:
* All 15 types must construct valid payloads per Data Model doc
* Backend integration must work for all 15
* Validation rules must match Business Rules document exactly

**Extensibility**:
* Adding more gear types in SSF-143C should be equally easy
* No hard-coded logic preventing future expansion
* Configuration file remains maintainable
```

---

## ✅ Tasks Checklist

### Configuration Expansion
- [ ] Add 6 gillnet configurations (GND, GNC, GNF, GTN, GTR, GEN)
- [ ] Add 4 trawl configurations (TBN, TBS, PTB, PTM)
- [ ] Add 4 seine configurations (SDN, SSC, SPR, SV)
- [ ] Add 1 hooks/lines configuration (LHP)
- [ ] Validate configuration syntax
- [ ] Test configuration loading

### Gillnet Types (6 types)
- [ ] Test GND: Gillnets (drift) registration
- [ ] Test GNC: Gillnets (circling) registration
- [ ] Test GNF: Gillnets fixed registration
- [ ] Test GTN: Combined gillnets-trammel nets registration
- [ ] Test GTR: Trammel nets registration
- [ ] Test GEN: Gillnets not specified registration
- [ ] Verify all use same dual-measurement pattern
- [ ] Test validation for all 6

### Trawl Types (4 types)
- [ ] Test TBN: Nephrops trawl registration
- [ ] Test TBS: Shrimp trawl registration
- [ ] Test PTB: Bottom pair trawl registration
- [ ] Test PTM: Mid-water pair trawl registration
- [ ] Verify all use optional model + perimeter pattern
- [ ] Test with and without model for each
- [ ] Test validation for all 4

### Seine Types (4 types)
- [ ] Test SDN: Danish anchor seine registration
- [ ] Test SSC: Scottish seine registration
- [ ] Test SPR: Pair seine registration
- [ ] Test SV: Boat/vessel seine registration
- [ ] Verify all use length + height pattern
- [ ] Test validation for all 4

### Hooks/Lines Type (1 type)
- [ ] Test LHP: Handlines registration
- [ ] Verify uses triple-field pattern
- [ ] Test stepper controls for lines and hooks
- [ ] Test hook size input
- [ ] Test validation

### Integration & Regression
- [ ] Integration test with backend for all 15 new types
- [ ] Regression test all 5 pilot types from SSF-143A
- [ ] Test gear type dropdown now shows 20 types total
- [ ] Test search/filter with expanded type list
- [ ] Verify no performance degradation

### Validation
- [ ] Verify field-level validation for all 15
- [ ] Test required field enforcement
- [ ] Test data type validation (MEASURE vs QUANTITY)
- [ ] Test positive value validation
- [ ] Test error message display

### Data & Backend
- [ ] Verify payload construction for all 15 types
- [ ] Test backend submission for each type
- [ ] Verify data persists correctly in database
- [ ] Test retrieval of registered gears (SSF-149)

### Documentation
- [ ] Update configuration documentation
- [ ] Document any pattern variations discovered
- [ ] Update test cases for new types
- [ ] Note any issues or edge cases found

---

## 📊 Gear Types Reference

### Added in This Story:

| Code | Name | Pattern | Fields |
|------|------|---------|--------|
| **GND** | Gillnets (drift) | Dual-Measurement | Length*, Height* |
| **GNC** | Gillnets (circling) | Dual-Measurement | Length*, Height* |
| **GNF** | Gillnets fixed | Dual-Measurement | Length*, Height* |
| **GTN** | Combined gillnets-trammel | Dual-Measurement | Length*, Height* |
| **GTR** | Trammel nets | Dual-Measurement | Length*, Height* |
| **GEN** | Gillnets (not specified) | Dual-Measurement | Length*, Height* |
| **TBN** | Nephrops trawl | Optional+Mandatory | Model(opt), Perimeter* |
| **TBS** | Shrimp trawl | Optional+Mandatory | Model(opt), Perimeter* |
| **PTB** | Bottom pair trawl | Optional+Mandatory | Model(opt), Perimeter* |
| **PTM** | Mid-water pair trawl | Optional+Mandatory | Model(opt), Perimeter* |
| **SDN** | Danish anchor seine | Dual-Measurement | Length*, Height* |
| **SSC** | Scottish seine | Dual-Measurement | Length*, Height* |
| **SPR** | Pair seine | Dual-Measurement | Length*, Height* |
| **SV** | Boat or vessel seine | Dual-Measurement | Length*, Height* |
| **LHP** | Handlines (hand operated) | Triple-Measurement | Lines*, Hooks*, Size* |

**Coverage after this story**: 20 gear types / 72 total = 28% (but ~85% of actual usage!)

---

## 🔗 Related Stories

- **SSF-143A**: Framework + 5 pilots (dependency - must be complete)
- **SSF-143C**: Standard gear types (follows this story)
- **SSF-143D**: Complex gear types (follows SSF-143C)
- **SSF-147**: Backend must support new gear types

---

**Last Updated**: November 14, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development (after SSF-143A complete)

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
