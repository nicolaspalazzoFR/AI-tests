# SSF-143C: [MOB] Register New Gear - Standard Gear Types Completion

**JIRA Ticket**: SSF-143C (Split from original SSF-143)  
**Summary**: [MOB] Register new gear - Standard Gear Types Completion (40 types)  
**Epic**: Gear Management  
**Sprint**: Sprint 5-6  
**PI**: PI 02 or PI 03  
**Story Points**: 2  
**Assignee**: [Mobile Developer]  
**Priority**: Medium  
**Scope**: [MOB]

---

## 📝 Description Field (Copy-Paste into JIRA Description)

```
{panel:title=Description}
Complete the standard gear type coverage by adding 40 remaining gear types that use established patterns. This brings total coverage to 60 gear types (~83% of all types, ~95% of actual fishing activity). All types in this story use patterns already validated in SSF-143A and SSF-143B, making this primarily a configuration expansion story with bulk testing.
{panel}

{panel:title=Business rules}
*Context*
After SSF-143A (5 types) and SSF-143B (15 types), the framework and all core patterns are proven. This story adds the remaining "standard" gear types - those that don't require workshops, free-text handling, or new pattern development. Focus is on configuration-driven expansion and comprehensive testing.

*Previous Coverage*
- SSF-143A: 5 pilot types (framework)
- SSF-143B: 15 common types (first expansion)
- **Total before this story**: 20 types

*This Story Adds*: 40 standard gear types

**40 Gear Types by Pattern**:

**Dual-Measurement Pattern** (15 types):
- **Remaining Seines**: SX (Seine nets not specified), BS (Beach seine)
- **Surrounding Nets** (5): PS, PS1, PS2, LA, SUX
- **Lift Nets** (4): LNP, LNB, LNS, LN
- **Falling Gear** (3): FCN, FCO, FG
- **Basic Traps** (1): FSN (Stow nets)

**Multi-Unit with Conditional** (8 types):
- **Dredges** (4): DRB, DRH, DRM, DRX (width + optional count)
- **Multiple Trawls** (3): OTT, OTP, TB (perimeter per trawl + count)
- **Mid-water Trawl** (1): OTM (model + perimeter)

**Triple-Measurement Pattern** (6 types):
- **Hooks/Lines**: LHM, LVT, LTL, LX, LLD, LL

**Dual-Measurement with Special** (3 types):
- **Traps**: FWR (Barriers), FPN (Pound nets) - Both L+H pattern

**Unique Simple** (1 type):
- **Beach Seine (BS)**: May have no requirements (check regulation)

*Pattern Reuse Analysis*

| Pattern | Count | Notes |
|---------|-------|-------|
| Dual-Measurement (L+H) | 15 types | 100% reuse from SSF-143A/B |
| Multi-Unit Conditional | 8 types | 100% reuse from SSF-143A (TBB pattern) |
| Triple-Measurement | 6 types | 100% reuse from SSF-143A (LLS pattern) |
| Trawl with Optional | 3 types | 100% reuse from SSF-143A/B |
| Special Cases | 2 types | Minor variations |

**Result**: ~95% code reuse, 5% configuration work!

*Implementation Strategy*

**Bulk Configuration Approach**:
1. Create configuration file with all 40 types
2. Load configurations into system
3. Test systematically by pattern group
4. No per-type custom code

**Configuration Template** (Example):
```json
{
  "LNP": {
    "name": "Portable lift nets",
    "category": "LIFT NETS",
    "pattern": "dual_measurement",
    "characteristics": [
      {"code": "GM", "name": "Maximum perimeter", "type": "MEASURE", "unit": "m", "required": true},
      {"code": "GN", "name": "Number of nets", "type": "QUANTITY", "required": "conditional", "condition": "if > 1"}
    ]
  }
}
```

*Testing Approach*

**Pattern-Based Testing** (not per-type):
- Test one representative from each pattern
- If pattern works, all types using that pattern should work
- Focus on edge cases and boundary conditions

**Sample Testing**: 
- 100% test for pilot types (SSF-143A)
- 50% sample for common types (SSF-143B)
- 25% sample for standard types (this story) + pattern validation
- Reduces testing effort while maintaining quality

*Why These 40 Types*

From Gear_Registration_Analysis.xlsx:
- All "Simple" or "Medium" complexity
- No workshop decisions needed
- No free-text challenges
- Standard EU fishing gear
- After this story: 95% coverage of actual fishing activity

*Suggestion 01*: Implement automated configuration validation to catch errors early (schema validation)

{*}Suggestion 02{*}: Create configuration generator tool to help add new types in future

{color:#ff8b00}*Questions / Ideas*{color}
Should we add configuration versioning to track which gear types were added when?
Should we provide a "preview" mode for new gear types before production deployment?
Should we auto-generate test cases from configuration?
{panel}

{panel:title=Dependencies}
SSF-143A: Framework complete and stable
SSF-143B: First expansion complete and validated
SSF-147: Backend configured for all new types

Technical Dependencies:
- Configuration system scalable to 60 types
- No performance issues with larger config files
- Validation framework handles all patterns
- Backend sync'd with new types

Business Dependencies:
- No critical issues from SSF-143A or SSF-143B
- User feedback on wizard UX positive
- Team confident in pattern approach
{panel}

{panel:title=Mockups}
**No new mockups needed** - All patterns established in SSF-143A

Optional: Annotated screens showing:
- Example lift net registration (conditional pattern)
- Example multiple trawl registration (OTT/OTP)
- Example surrounding net registration (purse seine)
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - Support all surrounding net types (5 types)*{color}
*GIVEN* fisher selects "Purse seine" (PS) or PS1, PS2, LA, SUX
*WHEN* form is displayed
*THEN* show dual-measurement form:
- "Length (m)" *
- "Maximum height (m)" *
*AND* validate both > 0
*AND* use same pattern for all 5 types

{color:#4c9aff}*02 - Support all lift net types with conditional logic (4 types)*{color}
*GIVEN* fisher selects "Portable lift nets" (LNP)
*AND* enters "Number of nets: 3"
*WHEN* form updates
*THEN* make "Number of nets" field required (was conditional)
*AND* wizard proceeds to per-net details (reuse TBB pattern)
*AND* same for: LNB, LNS, LN

{color:#4c9aff}*03 - Support all dredge types (4 types)*{color}
*GIVEN* fisher selects any dredge type (DRB, DRH, DRM, DRX)
*WHEN* form is displayed
*THEN* show:
- "Width of dredge (m)" *
- "Number of dredges" (conditional if > 1)
*AND* follow conditional multi-unit pattern from SSF-143A

{color:#4c9aff}*04 - Support remaining hooks/lines types (6 types)*{color}
*GIVEN* fisher selects LHM, LVT, LTL, LX, LLD, or LL
*WHEN* form is displayed
*THEN* show triple-field pattern (like LHP from SSF-143B):
- Number of lines / Overall length of lines
- Number of hooks
- Hook size
*AND* validate all > 0
*AND* use appropriate labels per gear type

{color:#4c9aff}*05 - Support multiple trawl types (3 types)*{color}
*GIVEN* fisher selects "Twin bottom otter trawl" (OTT)
*AND* enters "Number of trawls: 2"
*WHEN* wizard proceeds
*THEN* show smart duplication option
*AND* collect perimeter per trawl (reuse TBB multi-unit pattern)
*AND* same for OTP, TB

{color:#4c9aff}*06 - Support falling gear types (3 types)*{color}
*GIVEN* fisher selects FCN, FCO, or FG
*WHEN* form is displayed
*THEN* show dual-field with conditional:
- "Maximum perimeter (m)" *
- "Number of devices" (if > 1)
*AND* apply conditional logic like lift nets

{color:#4c9aff}*07 - Configuration-driven implementation verified*{color}
*GIVEN* all 40 new types added to configuration
*WHEN* system loads configurations
*THEN* no custom code per type exists
*AND* all types use framework patterns
*AND* configuration file remains < 50KB
*AND* loading time < 100ms

{color:#4c9aff}*08 - Pattern-based testing validates all types*{color}
*GIVEN* dual-measurement pattern tested with PS (purse seine)
*WHEN* pattern validation passes
*THEN* assume PS1, PS2, LA, SUX also work (same pattern)
*AND* spot-check 2-3 types per pattern to confirm
*AND* document any deviations found

{color:#4c9aff}*09 - Regression testing passes for all previous types*{color}
*GIVEN* SSF-143A and SSF-143B types were working
*WHEN* SSF-143C is deployed
*THEN* all 20 previous types must still function
*AND* no wizard flow regressions
*AND* no validation regressions
*AND* no payload construction regressions

{color:#4c9aff}*10 - Total gear type coverage reaches 60 types*{color}
*GIVEN* SSF-143C is complete
*WHEN* gear type selection dropdown is displayed (SSF-141)
*THEN* show 60 total gear types
*AND* all 60 selectable
*AND* search/filter works across all 60
*AND* performance remains acceptable

h3. Additional Acceptance Criteria

**Configuration Quality**:
* All 40 configurations follow same schema
* No typos in gear type codes
* All MDR codes correct
* All validation rules aligned with Business Rules doc

**Performance**:
* 60 gear types loads in < 200ms
* Form generation for any type < 300ms
* No memory issues with larger configuration
* Search/filter remains responsive

**Testing Coverage**:
* Minimum 10 gear types end-to-end tested (25% sample)
* All 5 patterns validated
* Critical types tested (most commonly used)
* Edge cases tested (conditional logic, optional fields)

**Data Integrity**:
* All payloads valid per Data Model doc
* Backend successfully persists all 40 types
* Retrieval works for all 40 types
```

---

## ✅ Tasks Checklist

### Configuration Creation (40 types)
- [ ] Create configurations for 15 dual-measurement types
- [ ] Create configurations for 8 multi-unit conditional types
- [ ] Create configurations for 6 triple-measurement types
- [ ] Create configurations for 3 special trawl types
- [ ] Create configurations for 2 trap types
- [ ] Create configuration for Beach seine (BS) - verify requirements
- [ ] Validate all configuration syntax
- [ ] Load and test configuration parsing

### Pattern Group 1: Dual-Measurement (15 types)
- [ ] Test PS: Purse seine
- [ ] Test LNP: Portable lift nets
- [ ] Test FCN: Cast nets
- [ ] Spot-check 5 more from this group
- [ ] Verify pattern consistency

### Pattern Group 2: Multi-Unit Conditional (8 types)
- [ ] Test DRB: Towed dredge
- [ ] Test OTT: Twin bottom otter trawl
- [ ] Spot-check 3 more from this group
- [ ] Verify conditional logic works

### Pattern Group 3: Triple-Measurement (6 types)
- [ ] Test LLD: Drifting longlines
- [ ] Test LL: Longlines not specified
- [ ] Spot-check 2 more from this group
- [ ] Verify three-field pattern

### Integration Testing
- [ ] Test backend integration for 10 sample types
- [ ] Verify data persists correctly
- [ ] Test retrieval of all new gear types
- [ ] Test gear list display with 60 types

### Regression Testing
- [ ] Test all 5 SSF-143A pilot types still work
- [ ] Test all 15 SSF-143B types still work
- [ ] Verify no wizard regressions
- [ ] Verify no validation regressions

### Performance Testing
- [ ] Load time with 60 gear types
- [ ] Search performance with 60 types
- [ ] Form generation time
- [ ] Memory usage validation

### Documentation
- [ ] Document any pattern variations discovered
- [ ] Update configuration schema if needed
- [ ] Create configuration guide for future additions
- [ ] Update test documentation

---

## 📊 Complete Gear Types List

### All 40 Types Added in This Story:

**SEINES** (2):
- SX: Seine nets (not specified)
- BS: Beach seine

**SURROUNDING NETS** (5):
- PS: Purse seine
- PS1: One boat operated purse seine
- PS2: Two boat operated purse seine
- LA: Without purse lines (lampara)
- SUX: Surrounding nets (not specified)

**LIFT NETS** (4):
- LNP: Portable lift nets
- LNB: Boat-operated lift nets
- LNS: Shore-operated stationary lift nets
- LN: Lift nets (not specified)

**FALLING GEAR** (3):
- FCN: Cast nets
- FCO: Cover pots/Lantern nets
- FG: Falling gear (not specified)

**DREDGES** (4):
- DRB: Towed dredge
- DRH: Hand dredge
- DRM: Mechanized dredge
- DRX: Dredge (not specified)

**TRAWLS** (4):
- OTT: Twin bottom otter trawl
- OTP: Multiple bottom otter trawl
- TB: Bottom trawls (not specified)
- OTM: Mid-water otter trawl

**HOOKS AND LINES** (6):
- LHM: Lines and pole lines (mechanised)
- LVT: Vertical lines
- LTL: Trolling lines
- LX: Hooks and lines (not specified)
- LLD: Drifting longlines
- LL: Longlines (not specified)

**TRAPS** (3):
- FSN: Stow nets
- FWR: Barriers, fences, weirs
- FPN: Stationary uncovered pound nets

**Total Coverage After SSF-143C**: 60 types / 72 total = 83%  
**Estimated Activity Coverage**: ~95%

**Remaining for SSF-143D**: 12 complex/edge case types (FYK, FAR, miscellaneous)

*Reference Documents*
- Business Rules: GEAR_CHARACTERISTICS_BUSINESS_RULES.md (Sections 4.2-4.8)
- Gear Analysis: Gear_Registration_Analysis.xlsx
- Data Model: GEAR_REGISTRATION_DATA_MODEL.md
- Framework: SSF-143A wizard implementation

*Testing Efficiency*

**Sample-Based Testing**:
- Full test: 10 types (25% sample)
- Pattern validation: All 5 patterns
- Regression: All 20 previous types (spot-check)
- Total tests: ~30-35 instead of 60+

*Suggestion 01*: Generate automated tests from configuration to ensure all types tested

{*}Suggestion 02{*}: Create configuration validation tool that checks against Business Rules document

{color:#ff8b00}*Questions / Ideas*{color}
Should we implement A/B testing to compare original collapsible mockup vs wizard for user preference?
Should we add telemetry to track which gear types are most/least used?
Should we provide batch registration for identical gears?
{panel}

{panel:title=Dependencies}
SSF-143A: Complete and stable
SSF-143B: Complete and validated
SSF-147: Backend supports all patterns

Technical Dependencies:
- Configuration system proven scalable
- All patterns working from previous stories
- Backend configuration updated
- No outstanding bugs from SSF-143A/B

Business Dependencies:
- User acceptance of wizard UX
- No scope changes from client
- Team velocity maintains 2 SP/sprint capacity
{panel}

{panel:title=Mockups}
**No new mockups needed** - All patterns covered by SSF-143A mockups

Reference: FIGMA_AI_PROMPT_Gear_Registration_Wizard.md shows all required patterns
{panel}
```

---

## ✅ Acceptance Criteria Field (Copy-Paste into JIRA Acceptance Criteria)

```
{color:#4c9aff}*01 - All 40 gear types accessible in system*{color}
*GIVEN* fisher opens gear type selection (SSF-141)
*WHEN* dropdown is displayed
*THEN* all 60 gear types should be available (20 previous + 40 new)
*AND* search/filter works across all
*AND* performance remains acceptable (< 200ms load)

{color:#4c9aff}*02 - Pattern validation for dual-measurement types (15 types)*{color}
*GIVEN* fisher registers "Purse seine" (PS) successfully
*WHEN* same pattern tested on PS1, PS2, LA, SUX
*THEN* all should behave identically
*AND* validate pattern works for all 15 dual-measurement types in this story

{color:#4c9aff}*03 - Pattern validation for multi-unit conditional (8 types)*{color}
*GIVEN* "Towed dredge" (DRB) registration works with conditional logic
*WHEN* tested on DRH, DRM, DRX, OTT, OTP, TB, OTM
*THEN* all should follow same conditional pattern
*AND* "if > 1" logic functions correctly for all

{color:#4c9aff}*04 - Configuration drives all behavior (no hard-coding)*{color}
*GIVEN* configuration entry for any of the 40 types
*WHEN* system processes the gear type
*THEN* form fields generated from configuration
*AND* validation applied from configuration
*AND* NO gear-type-specific code branches exist

{color:#4c9aff}*05 - Batch testing validates pattern groups*{color}
*GIVEN* 10 representative types selected (one per pattern + extras)
*WHEN* end-to-end tested
*THEN* all 10 must pass successfully
*AND* extrapolate success to other types in same pattern group

{color:#4c9aff}*06 - Payload construction correct for all 40 types*{color}
*GIVEN* any of the 40 new types registered
*WHEN* payload is constructed
*THEN* structure must match Data Model doc
*AND* characteristics must match Business Rules doc
*AND* backend must accept and persist successfully

{color:#4c9aff}*07 - No regression in previous 20 types*{color}
*GIVEN* SSF-143A and SSF-143B types were working
*WHEN* SSF-143C is deployed
*THEN* spot-check 5 types from SSF-143A
*AND* spot-check 5 types from SSF-143B
*AND* all 10 must still function correctly

{color:#4c9aff}*08 - Configuration validation prevents errors*{color}
*GIVEN* configuration file with 60 entries
*WHEN* system loads configuration at startup
*THEN* validate all entries against schema
*AND* reject invalid configurations
*AND* log validation errors
*AND* prevent app start if configuration invalid

{color:#4c9aff}*09 - Performance acceptable with 60 types*{color}
*GIVEN* 60 gear types loaded
*WHEN* measuring performance
*THEN* gear type list loads in < 200ms
*AND* search/filter responds in < 100ms
*AND* form generation for any type < 300ms
*AND* no memory warnings or crashes

{color:#4c9aff}*10 - Documentation updated for all 40 types*{color}
*GIVEN* SSF-143C implementation complete
*WHEN* configuration documentation reviewed
*THEN* all 40 types should be documented
*AND* patterns clearly indicated
*AND* any special cases noted
*AND* test coverage documented

h3. Additional Acceptance Criteria

**Configuration Management**:
* Configuration file versioned in git
* Changes reviewed before deployment
* Schema validation automated
* Rollback plan if configuration issues found

**Quality Assurance**:
* Pattern-based testing approach documented
* Sample types justified (why these 10 tested end-to-end)
* Regression test suite maintained
* Any bugs found documented and tracked

**Coverage Metrics**:
* 60/72 types supported (83%)
* Estimated 95% of actual fishing activity covered
* All "Simple" and "Medium" types complete
* Only "Complex" types remain (SSF-143D)
```

---

## ✅ Tasks Checklist

### Configuration File Management
- [ ] Create or expand gear_type_config.json
- [ ] Add all 40 configurations
- [ ] Validate JSON syntax
- [ ] Create configuration schema
- [ ] Implement schema validation
- [ ] Test configuration loading

### Surrounding Nets (5 types)
- [ ] Add PS, PS1, PS2, LA, SUX configurations
- [ ] Test PS end-to-end
- [ ] Spot-check 2 others
- [ ] Verify pattern consistency

### Lift Nets (4 types)
- [ ] Add LNP, LNB, LNS, LN configurations
- [ ] Test LNP with conditional logic
- [ ] Verify "if > 1" pattern works
- [ ] Test multi-unit wizard for lift nets

### Falling Gear (3 types)
- [ ] Add FCN, FCO, FG configurations
- [ ] Test FCN end-to-end
- [ ] Verify conditional pattern

### Dredges (4 types)
- [ ] Add DRB, DRH, DRM, DRX configurations
- [ ] Test DRB with multiple dredges
- [ ] Test DRH with single dredge
- [ ] Verify conditional logic

### Seines (2 types)
- [ ] Add SX, BS configurations
- [ ] Test SX end-to-end
- [ ] Verify BS requirements (may be none)

### Multiple Trawls (4 types)
- [ ] Add OTT, OTP, TB, OTM configurations
- [ ] Test OTT with 2 trawls
- [ ] Test OTP with 3+ trawls
- [ ] Verify per-trawl characteristics

### Remaining Hooks/Lines (6 types)
- [ ] Add LHM, LVT, LTL, LX, LLD, LL configurations
- [ ] Test LLD end-to-end
- [ ] Test LL end-to-end
- [ ] Verify triple-field pattern

### Basic Traps (3 types)
- [ ] Add FSN, FWR, FPN configurations
- [ ] Test FSN (stow nets)
- [ ] Test FWR (barriers/fences)
- [ ] Verify length + height pattern

### Integration Testing
- [ ] Backend integration for 10 sample types
- [ ] Database persistence verification
- [ ] Gear list retrieval with new types
- [ ] End-to-end flows for representative types

### Regression Testing
- [ ] Test 5 types from SSF-143A
- [ ] Test 5 types from SSF-143B
- [ ] Verify wizard navigation unchanged
- [ ] Verify validation logic unchanged

### Performance Testing
- [ ] Load 60 gear types and measure time
- [ ] Test search with 60 types
- [ ] Test filter functionality
- [ ] Monitor memory usage
- [ ] Test on slow devices

### Documentation & QA
- [ ] Update configuration documentation
- [ ] Document testing approach (sample-based)
- [ ] Create configuration addition guide
- [ ] Update team onboarding materials

---

## 🔗 Related Stories

- **SSF-143A**: Framework + 5 pilots (dependency)
- **SSF-143B**: 15 common types (dependency)
- **SSF-143D**: 12 complex types (follows this)
- **SSF-147**: Backend gear registration (must be updated)

---

**Last Updated**: November 14, 2025  
**Created By**: AI Assistant (Cline)  
**Status**: Ready for Development (after SSF-143B)

---

*This user story follows the JIRA formatting standards established in PROJECT_CONTEXT.md and JIRA_FORMATTING_GUIDE.md*
