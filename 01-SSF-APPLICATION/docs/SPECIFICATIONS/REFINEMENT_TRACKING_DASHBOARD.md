# 📊 REFINEMENT TRACKING DASHBOARD
## Sprint 1-5 | PI 01 | User Story Refinement Progress

> **Purpose**: Track refinement progress towards having all 84 "Open" user stories reach "Ready" status by end of Sprint 5
> **Target**: 6.5 stories per refinement session average
> **Deadline**: End of Sprint 5, PI 01

---

## 📈 CURRENT STATUS SNAPSHOT

### Key Metrics (As of Sprint 1, Session 2 Completed)

```
┌─────────────────────────────────────────────────┐
│  TOTAL USER STORIES               91            │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  📋 To Refine (Open)              84            │
│  ✅ Already Refined (Ready)        7            │
│  🔄 Other Status                   0            │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  REFINEMENT SESSIONS                            │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  ✅ Completed                      2            │
│  📅 Remaining                     13            │
│  🎯 Target Velocity          6.5 stories/session│
│  📊 Current Velocity         0.5 stories/session│
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│  PROGRESS STATUS                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  Progress                  8% (7/91)            │
│  Status                    🔴 CRITICAL RISK     │
│  Required Velocity Now     6.5 stories/session  │
│  Risk Level               HIGH - Action Required│
└─────────────────────────────────────────────────┘
```

---

## 📉 BURNDOWN CHART DATA

### Chart Configuration
- **Y-Axis**: Stories remaining to refine (84 → 0)
- **X-Axis**: Refinement sessions (1-15)
- **Ideal Line**: Linear decrease (84 - (session × 5.6))
- **Actual Line**: Updated after each session

### Data Table for Chart

| Session | Sprint | Stories Remaining (Ideal) | Stories Remaining (Actual) | Variance | Status |
|---------|--------|---------------------------|----------------------------|----------|--------|
| 0       | 1      | 84                        | 84                         | 0        | Start  |
| 1       | 1      | 78                        | 84                         | -6       | 🔴     |
| 2       | 1      | 72                        | 83                         | -11      | 🔴     |
| 3       | 1      | 67                        | [UPDATE]                   | -        | -      |
| 4       | 2      | 61                        | [UPDATE]                   | -        | -      |
| 5       | 2      | 56                        | [UPDATE]                   | -        | -      |
| 6       | 2      | 50                        | [UPDATE]                   | -        | -      |
| 7       | 3      | 45                        | [UPDATE]                   | -        | -      |
| 8       | 3      | 39                        | [UPDATE]                   | -        | -      |
| 9       | 3      | 34                        | [UPDATE]                   | -        | -      |
| 10      | 4      | 28                        | [UPDATE]                   | -        | -      |
| 11      | 4      | 23                        | [UPDATE]                   | -        | -      |
| 12      | 4      | 17                        | [UPDATE]                   | -        | -      |
| 13      | 5      | 12                        | [UPDATE]                   | -        | -      |
| 14      | 5      | 6                         | [UPDATE]                   | -        | -      |
| 15      | 5      | 0                         | [UPDATE]                   | -        | Target |

**Formula for Ideal Line**: `=84-(ROW()-1)*5.6`
**Formula for Variance**: `=Actual-Ideal`
**Status Colors**:
- 🟢 Green: Variance ≥ 0 (ahead or on track)
- 🟡 Yellow: Variance -5 to -1 (slight delay)
- 🔴 Red: Variance < -5 (critical delay)

---

## 📈 BURNUP CHART DATA

### Chart Configuration
- **Y-Axis**: Stories refined (cumulative, 0 → 84)
- **X-Axis**: Refinement sessions (1-15)
- **Total Scope Line**: Horizontal line at 84
- **Target Line**: Linear growth (session × 5.6)
- **Actual Line**: Cumulative stories refined

### Data Table for Chart

| Session | Sprint | Stories Refined (Target) | Stories Refined (Actual) | Total Scope | Gap to Target |
|---------|--------|-------------------------|--------------------------|-------------|---------------|
| 0       | 1      | 0                       | 0                        | 84          | 0             |
| 1       | 1      | 6                       | 0                        | 84          | -6            |
| 2       | 1      | 12                      | 1                        | 84          | -11           |
| 3       | 1      | 17                      | [UPDATE]                 | 84          | -             |
| 4       | 2      | 23                      | [UPDATE]                 | 84          | -             |
| 5       | 2      | 28                      | [UPDATE]                 | 84          | -             |
| 6       | 2      | 34                      | [UPDATE]                 | 84          | -             |
| 7       | 3      | 39                      | [UPDATE]                 | 84          | -             |
| 8       | 3      | 45                      | [UPDATE]                 | 84          | -             |
| 9       | 3      | 50                      | [UPDATE]                 | 84          | -             |
| 10      | 4      | 56                      | [UPDATE]                 | 84          | -             |
| 11      | 4      | 61                      | [UPDATE]                 | 84          | -             |
| 12      | 4      | 67                      | [UPDATE]                 | 84          | -             |
| 13      | 5      | 72                      | [UPDATE]                 | 84          | -             |
| 14      | 5      | 78                      | [UPDATE]                 | 84          | -             |
| 15      | 5      | 84                      | [UPDATE]                 | 84          | -             |

**Formula for Target Line**: `=(ROW()-1)*5.6`
**Formula for Gap**: `=Actual-Target`

---

## 📋 REFINEMENT SESSION TRACKER (PDCA)

### Session Log

| # | Sprint | Date | Day | Stories Target | Actual Refined | Cumulative | Remaining | Velocity | Status | Notes / Blockers |
|---|--------|------|-----|----------------|----------------|------------|-----------|----------|--------|------------------|
| 1 | 1 | [Date] | Tue | 7 | 0 | 0 | 84 | 0.0 | 🔴 | Learning session - understanding process |
| 2 | 1 | [Date] | Thu | 7 | 1 | 1 | 83 | 0.5 | 🔴 | Team alignment issues, slow start |
| 3 | 1 | [Next Tue] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 4 | 2 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 5 | 2 | [Date] | Thu | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 6 | 2 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 7 | 3 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 8 | 3 | [Date] | Thu | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 9 | 3 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 10 | 4 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 11 | 4 | [Date] | Thu | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 12 | 4 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 13 | 5 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 14 | 5 | [Date] | Thu | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |
| 15 | 5 | [Date] | Tue | 7 | [UPDATE] | [UPDATE] | [UPDATE] | [UPDATE] | - | - |

**Formulas**:
- Cumulative: `=SUM($F$2:F2)` (sum of actual refined)
- Remaining: `=84-G2` (84 minus cumulative)
- Velocity: `=F2` (actual refined that session)
- Status: 
  - 🟢 if Velocity ≥ 6.5
  - 🟡 if Velocity 4-6.4
  - 🔴 if Velocity < 4

### PDCA Framework Integration

**After Each Session - Complete**:

**PLAN**:
- [ ] Target stories identified (see Planning Guide)
- [ ] Pre-requisites completed
- [ ] Team agenda sent

**DO**:
- [ ] Session conducted
- [ ] Stories discussed and estimated
- [ ] Blockers documented

**CHECK**:
- Actual velocity vs target: [X.X stories]
- Effectiveness: [High/Medium/Low]
- Blockers resolved: [X/Y]

**ACT**:
- [ ] Update next session plan based on learnings
- [ ] Address blockers before next session
- [ ] Adjust approach if needed (session length, preparation, etc.)

---

## 📊 EPIC-LEVEL BREAKDOWN

### Progress by Epic

| Epic ID | Epic Name | Total Stories | Open (To Refine) | Ready | Other | % Complete | Priority | Sprint Target |
|---------|-----------|---------------|------------------|-------|-------|------------|----------|---------------|
| SSF-123 | [Fishing Operations] | 14 | 13 | 1 | 0 | 7% | HIGH | 1-2 |
| SSF-96  | [Login & Session] | 12 | 6 | 6 | 0 | 50% | CRITICAL | 1 |
| SSF-122 | [Departure & Catches] | 10 | 10 | 0 | 0 | 0% | HIGH | 2-3 |
| SSF-93  | [Gear Management] | 10 | 9 | 1 | 0 | 10% | MEDIUM | 2-3 |
| SSF-95  | [Map & Location] | 8 | 6 | 2 | 0 | 25% | MEDIUM | 3-4 |
| SSF-84  | [Technical Setup] | 8 | 3 | 5 | 0 | 63% | HIGH | 1 |
| SSF-165 | [Backend Infrastructure] | 3 | 3 | 0 | 0 | 0% | MEDIUM | 4-5 |
| SSF-166 | [Internationalization] | 4 | 3 | 1 | 0 | 25% | LOW | 5 |
| SSF-162 | [Menu & Navigation] | 3 | 2 | 1 | 0 | 33% | MEDIUM | 3 |
| SSF-94  | [Home & Widgets] | 5 | 4 | 1 | 0 | 20% | MEDIUM | 2 |
| SSF-86  | [Tracking] | 6 | 1 | 5 | 0 | 83% | HIGH | 1 |
| SSF-97  | [CI/CD & Deployment] | 5 | 5 | 0 | 0 | 0% | MEDIUM | 4-5 |
| SSF-132 | [FMC Integration] | 1 | 1 | 0 | 0 | 0% | MEDIUM | 4 |

**Visual Progress Bars** (for Google Sheets):
Use conditional formatting with data bars based on % Complete column.

**Prioritization Logic**:
1. CRITICAL: Must complete first (dependencies)
2. HIGH: Core functionality
3. MEDIUM: Important but can be scheduled flexibly
4. LOW: Nice-to-have, can be last

---

## 🎯 VELOCITY ANALYSIS

### Current Velocity Trend

| Metric | Value | Status |
|--------|-------|--------|
| **Average Velocity (Sessions 1-2)** | 0.5 stories/session | 🔴 Critical |
| **Target Velocity** | 6.5 stories/session | Target |
| **Gap** | -6.0 stories/session | 🔴 -92% |
| **Required Velocity (Remaining)** | 6.5 stories/session | Unchanged |
| **Projected Completion** | Sprint 15+ | 🔴 Beyond deadline |

### Velocity Recommendations

**Status: 🔴 CRITICAL - IMMEDIATE ACTION REQUIRED**

**Analysis**:
- Sessions 1-2 were learning/alignment sessions
- Only 1 story moved to "Ready" in 2 sessions
- Current pace: 84 stories ÷ 0.5 velocity = 168 sessions needed ❌
- Target pace: 84 stories ÷ 6.5 velocity = 13 sessions ✅

**Immediate Actions Required**:

1. **📋 Improve Pre-Session Preparation**
   - Send materials 48h in advance
   - Pre-draft acceptance criteria
   - Clarify business rules beforehand

2. **⏱️ Optimize Session Format**
   - Time-box each story to 7-8 minutes
   - Use silent reading time (first 5 min)
   - Park detailed discussions for async follow-up

3. **👥 Improve Team Alignment**
   - Review learnings from Sessions 1-2
   - Align on refinement criteria
   - Practice estimation techniques

4. **🎯 Target Quick Wins**
   - Start with simpler stories (2-3 SP)
   - Focus on Epics with existing context (SSF-86, SSF-84)
   - Build momentum before tackling complex stories

**Expected Impact**:
- Session 3 target: 5-7 stories (realistic improvement)
- Session 4+ target: 7-8 stories (full velocity)
- This would put project back on track by Sprint 2

---

## 🚨 RISK ASSESSMENT

### Risk Matrix

| Risk Level | Velocity Range | Sessions Behind | Status | Action |
|------------|----------------|-----------------|--------|--------|
| 🟢 On Track | ≥ 6.5 | 0 to -1 | Excellent | Maintain |
| 🟡 At Risk | 4.0-6.4 | -2 to -3 | Concern | Monitor & Adjust |
| 🔴 Critical | < 4.0 | -4 or more | Danger | Emergency Action |

**Current Status**: 🔴 CRITICAL (-11 sessions behind ideal pace)

### Risk Mitigation Strategies

#### Short-term (Sprint 1-2)
- ✅ PDCA approach implemented (learning from Sessions 1-2)
- ⚠️ Need immediate velocity improvement in Session 3
- 🎯 Focus on process optimization

#### Medium-term (Sprint 3-4)
- Consider adding extra 30min sessions if still behind
- Review and adjust story complexity estimates
- Identify stories that can be refined asynchronously

#### Long-term (Sprint 5+)
- If still critically behind by Sprint 4: Escalate to stakeholders
- Options: Extend timeline, reduce scope, or add resources
- Document lessons learned for next PI

### Contingency Plans

**Plan A** (Preferred): Improve velocity through process optimization
- Timeline: Sprint 1-2
- Success metric: Reach 6.5+ velocity by Session 6

**Plan B**: Add extra refinement sessions
- Timeline: Sprint 3 if velocity < 5.0
- Format: 2-3 extra 30min sessions per sprint

**Plan C**: Scope adjustment
- Timeline: Sprint 4 if still behind
- Action: Descope lowest priority Epic with stakeholder approval

**Plan D**: Timeline extension
- Timeline: Last resort, end of Sprint 4
- Action: Negotiate extending refinement into Sprint 6

---

## 📧 STAKEHOLDER WEEKLY REPORT TEMPLATE

### Copy-Paste Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 REFINEMENT PROGRESS - Week of [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ STORIES REFINED THIS WEEK
   • Sessions conducted: [X]
   • Stories moved to "Ready": [X]
   • Cumulative progress: [X/84] ([Y]%)

📈 VELOCITY METRICS
   • Current velocity: [X] stories/session
   • Target velocity: 6.5 stories/session
   • Variance: [+/- X] stories/session
   • Status: [🟢 On Track / 🟡 At Risk / 🔴 Critical]

🎯 EPIC FOCUS
   • Primary Epic this week: [Epic Name]
   • Stories refined: [X/Y]
   • Next Epic: [Epic Name]

📅 TIMELINE
   • Sessions remaining: [X]
   • Projected completion: [Sprint X]
   • On track for Sprint 5 deadline: [YES/NO]

💡 KEY INSIGHTS
   • [Insight 1: e.g., "Team velocity improving after process adjustment"]
   • [Insight 2: e.g., "Backend stories refining faster than mobile"]
   • [Insight 3: e.g., "Pre-session prep reducing refinement time"]

⚠️ BLOCKERS & RISKS
   • [Blocker 1 if any]
   • [Blocker 2 if any]
   • Mitigation: [Actions taken]

🔜 NEXT WEEK
   • Sessions planned: [X]
   • Target stories: [X]
   • Focus Epics: [Epic 1, Epic 2]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📖 HOW TO USE THIS DASHBOARD

### Weekly Update Routine (10 minutes)

**After Each Refinement Session**:
1. Update "Refinement Session Tracker" with actual results
2. Update "Burndown Chart Data" - Actual column
3. Update "Burnup Chart Data" - Actual column
4. Update "Velocity Analysis" - recalculate averages
5. Note any blockers in the Notes column

**Every Monday Morning** (5 minutes):
1. Review upcoming sessions (next 2)
2. Check risk status
3. Plan focus for the week

**Every Wednesday** (15 minutes):
1. Generate weekly report for stakeholders
2. Update Epic-level progress
3. Adjust next sprint's session targets if needed
4. Review velocity trend and take corrective action if needed

### Google Sheets Setup Instructions

1. **Create new Google Sheet**: "SSF Refinement Tracking Dashboard"

2. **Import Data**:
   - Sheet 1 "Master Data": Import EXPORT_JIRA_10_11_2025_backlog_status.csv
   - Sheet 2 "Burndown": Copy burndown table from this file
   - Sheet 3 "Burnup": Copy burnup table from this file
   - Sheet 4 "Session Tracker": Copy session tracker table
   - Sheet 5 "Epic Breakdown": Copy epic breakdown table
   - Sheet 6 "Dashboard": Create visual summary with charts

3. **Create Charts**:
   - **Burndown Chart**: Line chart with Sessions (X) vs Stories Remaining (Y)
     - Series 1: Ideal Line (blue)
     - Series 2: Actual Line (red)
   - **Burnup Chart**: Line chart with Sessions (X) vs Stories Refined (Y)
     - Series 1: Target Line (blue)
     - Series 2: Actual Line (green)
     - Series 3: Total Scope (horizontal line at 84)
   - **Velocity Trend**: Column chart showing velocity per session
   - **Epic Progress**: Stacked bar chart showing Open vs Ready by Epic

4. **Conditional Formatting**:
   - Session Tracker Status column: Color based on velocity
   - Burndown Variance: Red if negative, green if positive
   - Epic % Complete: Data bars with gradient

5. **Formulas to Add**:
   - All formulas indicated in tables above
   - Auto-calculate remaining sessions: `=15-COUNT(completed_sessions)`
   - Auto-calculate required velocity: `=stories_remaining/sessions_remaining`

### Sharing Settings

- **Edit Access**: PM, Tech Lead
- **Comment Access**: BA, Developer
- **View Access**: Stakeholders, Business Owner

---

## 🔄 CONTINUOUS IMPROVEMENT TRACKING

### Lessons Learned Log

| Date | Session | What Worked | What Didn't Work | Action for Next Time |
|------|---------|-------------|------------------|----------------------|
| [Date] | 1 | Team presence | No pre-work, unclear process | Send materials 48h before |
| [Date] | 2 | Better clarity | Still too slow, lengthy discussions | Time-box stories to 7min |
| [Next] | 3 | [UPDATE] | [UPDATE] | [UPDATE] |

### Process Metrics

| Metric | Session 1 | Session 2 | Session 3 | Target | Trend |
|--------|-----------|-----------|-----------|--------|-------|
| Avg time per story | N/A | ~60min | [UPDATE] | 8min | - |
| Stories with clear acceptance criteria | 0% | 50% | [UPDATE] | 100% | ↗️ |
| Pre-session materials sent | No | No | [UPDATE] | Yes | - |
| Team attendance rate | 100% | 100% | [UPDATE] | 100% | ✅ |

---

## ✅ SUCCESS CRITERIA

**Sprint 5 End Goal - Definition of Done**:
- [ ] All 84 "Open" stories moved to "Ready" status
- [ ] All stories have clear acceptance criteria
- [ ] All stories have story point estimates
- [ ] All dependencies identified and documented
- [ ] All business rules documented
- [ ] Mockups finalized for mobile stories
- [ ] Technical feasibility confirmed for all stories
- [ ] Client has reviewed and approved all "Ready" stories

**Weekly Success Indicators**:
- ✅ Average velocity ≥ 6.5 stories/session over last 3 sessions
- ✅ No more than 2 sessions below 5.0 stories/session
- ✅ Burndown chart trending toward zero by Session 15
- ✅ No critical blockers lasting > 1 sprint
- ✅ Team confidence in refinement process improving

---

**Last Updated**: [Current Date]
**Next Review**: [Next Wednesday]
**Owner**: Product Manager
**Contributors**: Tech Lead, BA, Development Team
