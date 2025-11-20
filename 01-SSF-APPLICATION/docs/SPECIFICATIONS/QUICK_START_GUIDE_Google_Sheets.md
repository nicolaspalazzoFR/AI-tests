# 🚀 QUICK START GUIDE - Google Sheets Setup
## Automated Refinement Tracking System

> **Time to setup**: 10 minutes
> **Time to use weekly**: 10 minutes total
> **Your role**: Enter 1 number after each session, everything else auto-calculates!

---

## 📦 What You Got

### 1. **REFINEMENT_TRACKER_backlog_status.csv**
Your main tracking tool - where magic happens automatically
- Dashboard with auto-updating metrics
- Session log (you enter data here)
- Burndown/Burnup charts (auto-calculated)
- Epic progress (auto-tracked)
- Weekly reports (auto-generated)

### 2. **SESSION_PLANNER_backlog_status.csv**
Your weekly prep tool - saves you planning time
- All 13 sessions pre-scheduled
- Candidate stories already allocated
- Pre-session checklist templates
- Quick reference agenda
- Velocity optimization strategies

---

## ⚡ 5-MINUTE SETUP

### Step 1: Import to Google Sheets (3 minutes)

**File 1: REFINEMENT_TRACKER**
1. Open Google Sheets: https://sheets.google.com
2. Click **File > Import**
3. Upload `REFINEMENT_TRACKER_backlog_status.csv`
4. **Import location**: Replace spreadsheet
5. **Separator type**: Detect automatically
6. **Convert text to numbers**: Yes
7. Click **Import data**
8. Rename sheet to: **"SSF Refinement Tracker"**

**File 2: SESSION_PLANNER**
1. Repeat steps 1-7 with `SESSION_PLANNER_backlog_status.csv`
2. Rename sheet to: **"SSF Session Planner"**

### Step 2: Create Multiple Sheets (2 minutes)

**IMPORTANT**: The CSV imported as ONE sheet, but you need to split it into multiple sheets:

**In REFINEMENT_TRACKER**:
1. Look for rows that say "Sheet Name, DASHBOARD", "Sheet Name, SESSION LOG", etc.
2. For each "Sheet Name" section:
   - Select all rows for that section (from "Sheet Name" to "---END---")
   - Right-click > **Copy**
   - At bottom, click **+** to add new sheet
   - Name it exactly as shown (e.g., "DASHBOARD", "SESSION LOG", etc.)
   - Paste the data
   - Delete the "Sheet Name" and "---END---" marker rows

**Result**: You should have 6 sheets:
- DASHBOARD
- SESSION LOG
- BURNDOWN CHART DATA
- BURNUP CHART DATA
- EPIC PROGRESS
- (Delete the original import sheet)

**In SESSION_PLANNER**:
1. Same process - split into 9 sheets:
   - SESSION CALENDAR
   - SESSION 3 - CANDIDATE STORIES
   - SESSION 4 - CANDIDATE STORIES
   - SESSION 5 - CANDIDATE STORIES
   - SESSIONS 6-15 - SUMMARY
   - PRE-SESSION CHECKLIST
   - QUICK REFERENCE
   - VELOCITY QUICK WINS
   - EPIC PRIORITY MATRIX

---

## 🎨 OPTIONAL: Add Charts (5 minutes)

### Burndown Chart
1. Go to BURNDOWN CHART DATA sheet
2. Select columns A:D (Session # through Actual)
3. **Insert > Chart**
4. Chart type: **Line chart**
5. Customize:
   - X-axis: Session #
   - Series 1 (Ideal): Blue line
   - Series 2 (Actual): Red line
   - Title: "Refinement Burndown"
6. Move chart to DASHBOARD sheet

### Burnup Chart
1. Go to BURNUP CHART DATA sheet
2. Select columns A:E
3. **Insert > Chart**
4. Chart type: **Line chart**
5. Customize:
   - Series 1 (Target): Blue line
   - Series 2 (Actual): Green line
   - Series 3 (Total Scope): Horizontal line at 84
6. Move chart to DASHBOARD sheet

---

## 🎯 HOW TO USE - Your 10-Minute Weekly Workflow

### Monday Morning (5 minutes)

**Open SESSION_PLANNER:**
1. Check **SESSION CALENDAR** sheet
2. Find next Tuesday's session (should be highlighted 🟡)
3. Go to **SESSION X - CANDIDATE STORIES** sheet
4. Copy the list of 7 stories
5. Send prep email to team:

```
Subject: Refinement Session Tomorrow - Prep Materials

Team,

Tomorrow's refinement session (Tuesday 14:00, 60min):
Target: 7 stories (quick wins)

Stories to review:
[Paste the 7 stories from SESSION_PLANNER]

Please review:
- Business rules in Confluence
- Mockups in Figma (links in planner)
- Come with questions

See you tomorrow!
```

**Done!** Takes 5 minutes.

---

### After Each Refinement Session (2 minutes)

**Open REFINEMENT_TRACKER:**
1. Go to **SESSION LOG** sheet
2. Find today's row (e.g., Session 3)
3. **Enter ONE number** in column F "Stories Refined"
   - Example: Enter `7` if you refined 7 stories
4. **Optional**: Add notes in column K if blockers
5. Check **DASHBOARD** sheet to see:
   - ✅ Cumulative progress auto-updated
   - ✅ Velocity auto-calculated
   - ✅ Status color auto-updated (🟢/🟡/🔴)
   - ✅ Charts auto-updated
   - ✅ Projected completion auto-updated

**That's it!** Everything else calculates automatically.

---

### Wednesday Morning (3 minutes)

**Open REFINEMENT_TRACKER:**
1. Go to **DASHBOARD** sheet
2. Find "WEEKLY REPORT" section (row ~23)
3. Cell B24 contains auto-generated report
4. **Copy the cell contents**
5. **Paste in email** to stakeholders:

```
To: Stakeholders
Subject: Weekly Refinement Progress

[Paste the auto-generated report here]
```

**Done!** Perfect for your 3-day/week schedule.

---

## 🔥 PRO TIPS - Maximum Automation

### 1. Share with Team (View Only)
- **File > Share**
- Add team emails
- Set to **"Viewer"** (except you = Editor)
- They can see progress anytime, you update

### 2. Set Up Conditional Formatting (One-Time, 5 min)

**For SESSION LOG Status column:**
1. Select column J (Status)
2. **Format > Conditional formatting**
3. Rule 1: Cell contains "🟢" → Green background
4. Rule 2: Cell contains "🟡" → Yellow background
5. Rule 3: Cell contains "🔴" → Red background

**For Velocity column:**
1. Select column I (Velocity)
2. **Format > Conditional formatting**
3. Rule 1: Greater than or equal to 6.5 → Green
4. Rule 2: Between 4 and 6.4 → Yellow
5. Rule 3: Less than 4 → Red

### 3. Pin Key Sheets
- Right-click on DASHBOARD sheet tab
- Select **"Protect sheet"** → Uncheck "Show a warning"
- This prevents accidental edits to formulas

### 4. Mobile Access
- Install Google Sheets app
- You can check progress on the go
- Quick update after sessions even from phone

---

## 📊 Understanding the Auto-Calculations

### What Updates Automatically?

When you enter "Stories Refined" in SESSION LOG:

**In SESSION LOG:**
- ✅ Cumulative (column G) = Sum of all stories refined so far
- ✅ Remaining (column H) = 84 - Cumulative
- ✅ Velocity (column I) = Stories refined this session
- ✅ Status (column J) = 🟢 if velocity ≥6.5, 🟡 if 4-6.4, 🔴 if <4

**In DASHBOARD:**
- ✅ Completed So Far = Sum from SESSION LOG
- ✅ Remaining = 84 - Completed
- ✅ Progress % = Completed / 84 * 100
- ✅ Current Velocity = Average of last 3 sessions
- ✅ Sessions Behind = (Target cumulative) - (Actual cumulative)
- ✅ Projected Completion = Based on current velocity
- ✅ Status = Overall health indicator
- ✅ Risk Level = Based on sessions behind

**In BURNDOWN:**
- ✅ Ideal Line = Linear decrease (84 → 0)
- ✅ Actual Line = Pulls from SESSION LOG Remaining column
- ✅ Variance = Actual - Ideal
- ✅ Status = Color indicator

**In BURNUP:**
- ✅ Target Line = Linear increase (0 → 84)
- ✅ Actual Line = Pulls from SESSION LOG Cumulative column
- ✅ Gap = Actual - Target

**In WEEKLY REPORT:**
- ✅ Entire text auto-generates using TODAY() function
- ✅ Counts sessions and stories from last 7 days
- ✅ Calculates all percentages
- ✅ Determines if on track for Sprint 5

---

## 🚨 Troubleshooting

### "Formulas showing as text"
**Fix**: The formulas need to be in the formula bar, not as text
1. Click on a cell with formula (should start with =)
2. If it shows as text, delete the cell
3. Click in formula bar and type: `=SUM(...)`
4. Google Sheets should recognize it as formula

### "Charts not updating"
**Fix**: Check chart data range
1. Click on chart > 3 dots > Edit chart
2. Verify Data range includes all rows
3. Update range if needed

### "#REF! errors"
**Fix**: Sheet reference broken
1. Check if all sheet names match exactly
2. "SESSION LOG" not "Session Log" (case-sensitive)
3. Re-enter formula if needed

### "Conditional formatting not applying"
**Fix**: Re-apply the rules
1. Select the range
2. Format > Conditional formatting
3. Delete existing rules
4. Add new rules as per instructions above

---

## ✅ Success Checklist

After setup, verify:
- [ ] Both files imported to Google Sheets
- [ ] Multiple sheets created (6 in Tracker, 9 in Planner)
- [ ] Formulas working (test by entering a number in SESSION LOG)
- [ ] DASHBOARD showing current metrics
- [ ] Charts created (optional but recommended)
- [ ] Shared with team (view access)
- [ ] Bookmarked both Google Sheets URLs
- [ ] Tested weekly report auto-generation

---

## 🎉 You're Ready!

**What you need to do each week:**
1. **Monday**: 5 min - Check SESSION_PLANNER, send prep email
2. **After each session**: 2 min - Enter ONE number in REFINEMENT_TRACKER
3. **Wednesday**: 3 min - Copy & paste auto-generated report

**Total time**: 10 minutes per week!
**Result**: Complete tracking, reporting, and planning system!

---

## 💡 Next Steps

**This Week (Session 3)**:
1. Implement the 5 "Velocity Quick Wins" from SESSION_PLANNER
2. Target 5-7 stories (realistic improvement from 0.5 velocity)
3. See if pre-session prep + time-boxing helps

**Next Week**:
1. Review velocity trend
2. Adjust if needed
3. Continue PDCA cycle

**Remember**: Progress over perfection. The system is designed to adapt as you learn!

---

**Questions?** Check the detailed .md files for more context:
- REFINEMENT_TRACKING_DASHBOARD.md (what all the metrics mean)
- REFINEMENT_PLANNING_GUIDE_backlog_status_COMPLETE.md (strategies and tips)

**Good luck! 🚀 You've got the tools to succeed!**
