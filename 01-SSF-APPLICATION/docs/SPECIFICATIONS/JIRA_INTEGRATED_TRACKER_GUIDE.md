# 📊 SSF Refinement Tracker - JIRA Integrated Version

## 🎯 Overview

This version of the tracker **automatically updates** Epic Progress and Dashboard metrics by pulling data directly from your JIRA exports. No more manual counting!

---

## 📁 File Comparison

### Original File: `SSF_Refinement_Tracker_Session_Planner.xlsx`
- ✅ Great for standalone use
- ❌ Epic counts are hardcoded
- ❌ Requires manual updates when backlog changes

### JIRA-Integrated File: `SSF_Refinement_Tracker_JIRA_Integrated.xlsx`
- ✅ **Auto-updates from JIRA exports**
- ✅ Epic counts calculated dynamically
- ✅ Reusable across multiple PIs
- ✅ Always reflects current JIRA status

---

## 📋 Sheet Structure (7 Sheets)

### 1. 🆕 JIRA DATA (NEW!)
**Your JIRA Import Sheet**
- Paste raw JIRA exports here
- Pre-loaded with your current PI 01 backlog (91 stories)
- Column structure matches JIRA export format

### 2. DASHBOARD
**Auto-updates from JIRA DATA + SESSION LOG**
- Total Stories: `=COUNTA('JIRA DATA'!A:A)-2`
- To Refine (Open): `=COUNTIF('JIRA DATA'!E:E,"Open")`
- Already Refined (Ready): `=COUNTIF('JIRA DATA'!E:E,"Ready")`
- Velocity and projections from SESSION LOG

### 3. SESSION LOG
**Manual Entry - No Change**
- Update column F (Stories Refined) after each session
- Header clearly shows: "Stories Refined (ENTER THIS)"
- Everything else auto-calculates

### 4. BURNDOWN CHART DATA
**Auto-updates from JIRA + SESSION LOG**
- Ideal line: Dynamically calculated from total stories in JIRA
- Actual line: Pulls from SESSION LOG remaining count
- Includes embedded chart

### 5. BURNUP CHART DATA
**Auto-updates from JIRA + SESSION LOG**
- Target line: Dynamically calculated from total stories
- Actual line: Pulls from SESSION LOG cumulative count
- Total scope line: Adjusts to JIRA total
- Includes embedded chart

### 6. EPIC PROGRESS
**Auto-calculated from JIRA DATA**
- Total Stories: `=COUNTIF('JIRA DATA'!F:F,A3)` (counts by Epic ID)
- Open: `=COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Open")`
- Ready: `=COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Ready")`
- % Complete: `=IF(C3=0,0,E3/C3*100)`

### 7. SESSION CALENDAR
**Reference Schedule - No Change**
- All 15 sessions with dates
- Pre-configured for PI 01

---

## 🔄 How to Use - Two Workflows

### Workflow A: After Each JIRA Export (Weekly/Bi-weekly)

1. **Export from JIRA**
   - Use same export format as `EXPORT_JIRA_10_11_2025_backlog_status.csv`
   - Must include columns: Issue Type, Issue key, Issue id, Summary, Status, Epic Link, Story Points

2. **Open JIRA DATA sheet**
   - Select all data in rows 3 and below
   - Delete (keep row 1 instructions and row 2 headers)

3. **Paste new JIRA data**
   - Start at row 3
   - Paste values only

4. **Magic happens! 🎩✨**
   - DASHBOARD metrics update instantly
   - EPIC PROGRESS recalculates
   - BURNDOWN/BURNUP charts adjust to new totals

### Workflow B: After Each Refinement Session

1. **Go to SESSION LOG sheet**

2. **Find your session row** (e.g., Session 3, row 5)

3. **Enter number in column F**
   - Example: If you refined 7 stories, enter `7`

4. **Everything updates:**
   - Cumulative count
   - Remaining stories
   - Velocity
   - Status indicator (🟢/🟡/🔴)
   - Charts update
   - Dashboard summary refreshes

---

## 💡 Key Benefits

### Dynamic Adaptation
- **Scope changes?** Paste new JIRA export → Everything adjusts
- **New epics?** Add Epic ID/Name in EPIC PROGRESS → Formulas count automatically
- **Stories moved between epics?** JIRA export handles it

### Cross-PI Reusability
Starting PI 02?
1. Export new PI 02 backlog from JIRA
2. Paste into JIRA DATA sheet
3. Update SESSION LOG dates
4. Reset session counts
5. **Ready to track PI 02!**

### No Manual Counting
- Epic story counts: ✅ Automatic
- Status breakdown: ✅ Automatic
- Total stories: ✅ Automatic
- % completion per epic: ✅ Automatic

---

## 📊 Formula Reference

### JIRA DATA → EPIC PROGRESS

```excel
Total:    =COUNTIF('JIRA DATA'!F:F,A3)
Open:     =COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Open")
Ready:    =COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Ready")
Other:    =C3-D3-E3
% Done:   =IF(C3=0,0,E3/C3*100)
```

### JIRA DATA → DASHBOARD

```excel
Total Stories:         =COUNTA('JIRA DATA'!A:A)-2
To Refine (Open):      =COUNTIF('JIRA DATA'!E:E,"Open")
Already Refined:       =COUNTIF('JIRA DATA'!E:E,"Ready")
Completed So Far:      =SUM('SESSION LOG'!F:F)
Remaining:             =IF(ISBLANK(C9),C7,C7-C9)
```

### SESSION LOG → CHARTS

```excel
Remaining:   =DASHBOARD!$C$7-G3  (Total from JIRA - Cumulative)
Ideal Line:  =DASHBOARD!$C$7-(DASHBOARD!$C$7/15)*(row-3)
```

---

## 🎯 JIRA Export Requirements

Your JIRA export CSV must have these columns (in this order):

| Column | Name | Purpose |
|--------|------|---------|
| A | Issue Type | Story, Bug, Task, etc. |
| B | Issue key | SSF-123, SSF-96, etc. |
| C | Issue id | Unique ID |
| D | Summary | Story title |
| E | **Status** | Open, Ready, Done, etc. |
| F | **Custom field (Epic Link)** | SSF-123, SSF-96, etc. |
| G | Custom field (Story Points) | 1, 2, 3, 5, etc. |

**Critical columns:** E (Status) and F (Epic Link) - these are used in formulas!

---

## 🚀 Getting Started

### First Time Setup

1. **Import to Google Sheets**
   ```
   File → Import → Upload → SSF_Refinement_Tracker_JIRA_Integrated.xlsx
   ```

2. **Verify JIRA DATA**
   - Should have 91 stories pre-loaded
   - Check Epic IDs in column F

3. **Check EPIC PROGRESS**
   - Should show counts for each epic
   - Total should equal 91

4. **Update SESSION LOG**
   - Enter completed session data (Sessions 1-2 already have data)

### For Each New PI

1. **Export JIRA backlog for new PI**

2. **Replace JIRA DATA sheet**
   - Delete old data (rows 3+)
   - Paste new PI backlog

3. **Update SESSION CALENDAR**
   - Adjust dates for new PI schedule

4. **Reset SESSION LOG**
   - Clear column F entries
   - Update dates if needed

5. **Continue tracking!**

---

## 🔧 Troubleshooting

### Issue: Epic counts show 0
**Solution:** Check Epic IDs in JIRA DATA column F match Epic IDs in EPIC PROGRESS column A

### Issue: #REF! errors after pasting JIRA data
**Solution:** Make sure you kept row 2 headers intact. Only delete/replace data in rows 3+

### Issue: Charts not updating
**Solution:** Charts update from SESSION LOG, not JIRA DATA. Enter session data in column F.

### Issue: Wrong status counts
**Solution:** Verify your JIRA export has exact status names ("Open", "Ready", etc.) in column E

---

## 📈 Advanced: Adding New Epics

If you get new epics in later PIs:

1. **Go to EPIC PROGRESS sheet**

2. **Add new row** (e.g., row 16)

3. **Enter manually:**
   - A16: Epic ID (e.g., "SSF-200")
   - B16: Epic Name (e.g., "New Feature")
   - H16: Priority (HIGH/MEDIUM/LOW)
   - I16: Sprint Target (e.g., "6-7")

4. **Formulas auto-fill:**
   - C16: `=COUNTIF('JIRA DATA'!F:F,A16)`
   - D16: `=COUNTIFS('JIRA DATA'!F:F,A16,'JIRA DATA'!E:E,"Open")`
   - E16: `=COUNTIFS('JIRA DATA'!F:F,A16,'JIRA DATA'!E:E,"Ready")`
   - F16: `=C16-D16-E16`
   - G16: `=IF(C16=0,0,E16/C16*100)`

---

## 🎊 Success Checklist

After pasting new JIRA data, verify:

- ✅ DASHBOARD "Total Stories" matches your backlog count
- ✅ DASHBOARD "To Refine (Open)" shows correct number
- ✅ DASHBOARD "Already Refined (Ready)" shows correct number
- ✅ EPIC PROGRESS totals add up to overall total
- ✅ Each epic shows correct Open/Ready breakdown
- ✅ No #REF! or #VALUE! errors anywhere

---

## 📞 Quick Reference

| Task | Sheet | Action |
|------|-------|--------|
| Import new JIRA backlog | JIRA DATA | Paste rows 3+ |
| Track refinement session | SESSION LOG | Enter value in column F |
| Check epic status | EPIC PROGRESS | Review auto-calculated counts |
| View velocity trends | DASHBOARD | Check velocity metrics |
| See progress visually | BURNDOWN/BURNUP | View embedded charts |

---

**File Location:** `/Users/nicolas.palazzo/Documents/AI Workspaces/SSF DOCS/SSF_Refinement_Tracker_JIRA_Integrated.xlsx`

**Happy tracking! 🚀**
