# Gear Management Requirements Workshop - Session 1
## FORMATTED WORKSHOP NOTES

**Date:** November 18, 2025  
**Time:** 14:00-15:00  
**Facilitator:** Nicolas Palazzo (Product Owner)  
**Attendees:** DG MARE PM, BO, BA  
**Workshop Rating:** 4/5 (ROTI feedback from participants)

---

## 🎯 WORKSHOP OBJECTIVE

Define and validate business rules for gear characteristics in SSF application to complete Gear Management Epic.

---

## 📋 KEY DECISIONS MADE

### 1. Gear Registration vs. Gear Declaration - Clarification

**DECISION:** Gear registration in the app is OPTIONAL. What's MANDATORY is declaring gears in fishing operation reports.

**Details:**
- Fisher CAN pre-register gears to their vessel (convenience feature)
- Fisher MUST declare gears used in departure reports (regulatory requirement)
- Gear declaration in catch reports is declarative (not validated against pre-registered gears)

**Rationale (Benoit):**
- Most gear reporting is declarative
- Should not be more complex than necessary
- Pre-registration is useful but not blocking

**Impact:**
- Gear registration becomes a convenience feature, not a hard requirement
- Priority may shift: Departure declaration + Hauls become higher priority than gear registration wizard
- Validation logic is simpler (no forced gear pre-registration)

---

### 2. Multi-Unit Gear Registration Approach

**DECISION:** Use separate gear registrations for each line/unit when they have DIFFERENT characteristics.

**Details from Benoit:**
- Fisher doesn't need to register 10 identical lines separately
- Fisher DOES need to register lines with different characteristics separately
- Example: Longline with 3 different hook types = 3 separate gear registrations
  - Line 1: Hook type A, 500m, 100 hooks
  - Line 2: Hook type B, 500m, 150 hooks  
  - Line 3: Hook type C, 500m, 100 hooks

**Rationale:**
- Regulations require declaration by characteristic combinations
- Different characteristics = different gear from regulatory perspective
- Same characteristics = can be grouped

**Implementation Rule:**
- Unique combination of (Gear Type + Characteristics) = One gear registration
- Same gear type with same characteristics can use quantity field

---

### 3. Data Validation Approach

**DECISION:** Display all characteristics (mandatory + optional) with appropriate validation.

**Rules:**
- Mandatory fields: Must be filled for form validation
- Optional fields: Available but not blocking submission
- Source of truth: "Gear-Gear" file from MDR team (expected this week)
- Units and mandatory status defined in Gear-Gear file

**Approved by attendees.**

---

### 4. Gear Composition for Fishing Operations

**KEY INSIGHT (from Norma):**
- Fisher registers individual gear units at departure (regulatory requirement)
- Fisher can COMPOSE gear units together for actual fishing operation
- Example: Take 10 nets on departure, assemble 5 of them together for fishing
- Reporting needs: Declare COMPOSED gear in haul (summed characteristics)

**Implications:**
- Departure report: List of individual gears taken
- Haul report: Composed gear with combined characteristics
- Two different contexts, two different needs

**This affects:** Haul reporting UI/UX (PI 02 scope)

---

## 🔓 OPEN QUESTIONS / PARKING LOT

### 1. Fixed vs. Mobile Gear
**Question:** Some gear is permanently set (fixed location), some is mobile. Does this affect reporting?
**Source:** Norma
**Action:** Document for further discussion
**Priority:** Medium (affects haul reporting design)

### 2. Multi-Vessel Trawling
**Question:** How to handle gear used by two vessels together?
**Source:** Norma
**Action:** Understand use case and regulatory requirements
**Priority:** Low (edge case, defer to later PI)

### 3. Mockup Generation Capacity
**Question:** Do we need a mockup for each gear type, or can we use generic templates?
**Source:** Discussion
**Action:** Align with UX designer (Shylesh) on approach
**Owner:** Nicolas
**By:** Before next workshop

---

## 📊 REQUIREMENTS INSIGHTS

### Fisher Workflow (from Norma):

**Step 1: Gear Registration (Optional convenience)**
- Fisher can pre-register gears to vessel
- Each gear = one physical unit with its characteristics
- Can register multiple units if they have different characteristics

**Step 2: Departure Report (Mandatory)**
- Declare which pre-registered gears are onboard
- OR declare new gears if not pre-registered
- List of individual gear units

**Step 3: Fishing Operation (Haul)**
- May combine multiple gear units for actual fishing
- Reports COMPOSED gear with summed characteristics
- Example: 5 nets of 100m each = 1 composed net of 500m

**Step 4: Catch Report**
- Declare which composed gear was used
- Gear characteristics are declarative (not validated)

---

## 🎯 PRIORITY CLARIFICATION

**Original Assumption:** Gear registration is high priority

**New Understanding (from Benoit):**
- Departure declaration is the regulatory priority
- Haul/Catch reporting is where gear is actually declared
- Gear pre-registration is a convenience feature

**Recommendation for Discussion:**
May need to re-evaluate PI 01 priorities:
- Current focus: Gear registration wizard
- Consider shifting: Departure declaration + Haul basics

**Decision needed:** Confirm with Mission Manager and team

---

## 📅 ACTION ITEMS

| Action | Owner | By When | Status |
|--------|-------|---------|--------|
| Send updated "Gear-Gear" mapping file | Norma (MDR Team) | This week | Pending |
| Align with Shylesh on mockup strategy | Nicolas | Before Wed workshop | Pending |
| Update Confluence with formatted notes | Nicolas | Today EOD | In Progress |
| Review priority implications with team | Nicolas | This week | Pending |
| Complete remaining Gear Mgmt requirements | All | Tomorrow 10am workshop | Scheduled |

---

## 🔄 NEXT STEPS

**Tomorrow's Workshop (Wednesday 10:00-11:00):**
- Complete remaining Gear Management topics
- Finalize business rules
- Prepare for development team handoff

**This Week:**
- Receive Gear-Gear file from MDR team
- Re-assess PI 01 priorities based on new understanding
- Update user stories to reflect validated requirements

---

## 💡 KEY INSIGHTS FOR PRODUCT STRATEGY

### 1. Gear Registration is Less Critical Than Assumed
- It's a convenience feature, not regulatory requirement
- Real priority: Declaration in departure/catch reports
- May need scope discussion with Mission Manager

### 2. Complexity is in Composition Logic
- Fisher workflow: Individual gears → Composed for fishing → Report composed
- Need to design for both contexts
- This is the real challenge, not simple registration

### 3. Keep It Simple (Benoit's Emphasis)
- Most reporting is declarative
- Don't over-engineer
- Start with basic functionality

---

## 📝 WORKSHOP EFFECTIVENESS

**ROTI Score:** 4/5 (Good/OK per participants)

**Feedback Requested:** "Do you have suggestions for improvement?"  
**Response:** "Not really" (interpreted as: workshop met expectations)

**Self-Assessment:**
- ✓ Recommendations were clear and accepted
- ✓ Good energy and collaboration
- ⚠️ Time management needs improvement
- ⚠️ Need faster comprehension of complex explanations

---

## 🎓 LESSONS LEARNED

**What Worked:**
- Coming prepared with recommendations
- Having rationale ready
- Asking for ROTI feedback (professional)
- Creating collaborative atmosphere

**For Improvement:**
- Stricter time management when discussions diverge
- Techniques for quickly understanding complex explanations
- Balance between exploration and agenda adherence

---

*Workshop notes captured by: Nicolas Palazzo*  
*Formatted version created: November 18, 2025*  
*Next workshop: November 19, 2025 at 10:00 AM*
