# 📊 DG_MARE_TEAMS_SSF_Refinement_Tracker - Update Summary

**Date:** November 15, 2025  
**Updated File:** `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx`

---

## ✅ What Was Done

### 1. **JIRA DATA Sheet - Enhanced Structure**
- ✅ Added **Labels column (H)** to match JIRA export format
- ✅ Added **PI column (J)** that auto-extracts PI from Labels (e.g., "SSF_PI#02")
- ✅ Imported **91 issues** from `SSF_BACKLOG_EXPORT_10_11.xlsx`
- ✅ All existing formulas updated to work with new column structure

**Column Layout:**
```
A: Issue Type
B: Issue key
C: Issue id
D: Summary
E: Status
F: Epic Link
G: Story Points
H: Labels (NEW)
I: Sprint
J: PI (NEW - auto-extracted from Labels)
```

### 2. **PI PROGRESS Sheet - NEW!**
- ✅ Created dedicated sheet for PI-level tracking
- ✅ Automatically counts stories per PI
- ✅ Shows Refined vs To Refine breakdown
- ✅ Includes progress indicators (🟢/🟡/🔴)

**Current PI Status:**
```
SSF_PI#01: 40 stories
SSF_PI#02: 35 stories ✓ (matches your requirement)
```

### 3. **EPIC PROGRESS Sheet - Enhanced**
- ✅ Added 4 new columns for PI-specific tracking:
  - **PI Filter** (Column J): Enter PI label to filter (e.g., "SSF_PI#02")
  - **Refined in PI** (Column K): Auto-counts refined stories for Epic+PI
  - **Total in PI** (Column L): Auto-counts total stories for Epic+PI
  - **PI Progress** (Column M): Shows format like "3/13"

**How to Use:**
1. In EPIC PROGRESS sheet, column J (PI Filter)
2. Enter "SSF_PI#02" next to "Gear Management"
3. Columns K, L, M will automatically show Gear Management progress for PI#02

### 4. **DASHBOARD Sheet**
- ✅ Added reference to PI PROGRESS sheet
- ✅ All existing metrics still working

---

## 📊 Current Data Analysis (from JIRA Export 10/11/2025)

### Overall Status
- **Total Issues:** 91
- **Status Breakdown:**
  - Open: 57 (62.6%)
  - Ready: 19 (20.9%)
  - Done: 9 (9.9%)
  - In review: 2 (2.2%)
  - To Deploy: 2 (2.2%)
  - In Progress: 1 (1.1%)
  - Canceled: 1 (1.1%)

### PI Breakdown
| PI | Total Stories | % of Backlog |
|----|--------------|--------------|
| SSF_PI#01 | 40 | 44.0% |
| SSF_PI#02 | 35 | 38.5% |
| No PI assigned | 16 | 17.5% |

### Gear Management Epic (Your Focus Area)

**Status as of JIRA Export (10/11/2025):**
```
Total Stories: 14
Refined (Ready): 1 (7.1%)
To Refine (Open): 13 (92.9%)
```

**Stories:**
1. ✅ SSF-140 - [MOB] Vessel's Empty Gear Management Screen - **Ready** (PI#02)
2. ⏳ SSF-141 - [MOB] Register new gear - Init Creation Form - Open (PI#02)
3. ⏳ SSF-142 - [MOB] Register new gear - Form submission - Open (PI#02)
4. ⏳ SSF-143 - [MOB] Register new gear - Gear characteristics - Open (PI#02)
5. ⏳ SSF-144 - [MOB] Vessel's Gear Screen - Gear List - Open (PI#02)
6. ⏳ SSF-145 - [MOB] Edit Gear - Open (PI#02)
7. ⏳ SSF-146 - [MOB] Delete Gear - Open (PI#02)
8. ⏳ SSF-147 - [BACK] Register new gear - Open (PI#02)
9. ⏳ SSF-148 - [BACK] List of vessel's gear - New Gear - Open (PI#02)
10. ⏳ SSF-149 - [BACK] List of vessel's gear - Retrieval - Open (PI#02)
11. ⏳ SSF-150 - [BACK] Edit Gear - Open (PI#02)
12. ⏳ SSF-151 - [BACK] Delete Gear - Open (PI#02)
13. ⏳ SSF-152 - [BACK] Error Management / Security - Open (PI#02)
14. ⏳ SSF-188 - [MOB] Error Management / Messages - Open (PI#02)

---

## 🎯 How to Use the Updated Tracker

### For PI-Level Tracking

1. **Open PI PROGRESS sheet**
2. View overall PI status with auto-calculated metrics
3. Formulas will update automatically as you update JIRA DATA

### For Epic-Level Tracking within a PI

1. **Open EPIC PROGRESS sheet**
2. **Find your epic** (e.g., "Gear Management" in column A)
3. **Enter PI label** in column J (e.g., "SSF_PI#02")
4. **View results** in columns K, L, M:
   - Refined in PI: X
   - Total in PI: Y
   - PI Progress: "X/Y"

**Example for Gear Management + PI#02:**
```
Column J: SSF_PI#02
Column K: 1 (auto-calculated)
Column L: 14 (auto-calculated)
Column M: 1/14 (auto-calculated)
```

### Updating with Fresh JIRA Data

When you have new JIRA exports:

1. **Export from JIRA** with same column format
2. **Run the update script:**
   ```bash
   cd "SSF DOCS/Excel Files"
   python3 update_tracker.py
   ```
3. **Or manually update:**
   - Go to JIRA DATA sheet
   - Delete rows 3+ (keep headers)
   - Paste new data starting at row 3
   - Column J (PI) will auto-populate

---

## 📝 Note About Your Requirements

You mentioned:
- ✅ PI#02 has 35 stories → **CONFIRMED** (35 stories found)
- ⚠️ Gear Management has 13 stories → **ACTUAL: 14 stories**
- ⚠️ 3 tickets refined → **ACTUAL: 1 ticket with "Ready" status**

**Possible Reasons for Discrepancy:**
1. JIRA export is from **10/11/2025** - may need fresh export
2. Some tickets might have been refined after the export
3. Status definitions: Only tickets marked "Ready" count as refined (per your specification)

**To Update:**
1. Update ticket statuses in JIRA to "Ready" for refined tickets
2. Export fresh JIRA data
3. Re-run the update script or manually refresh JIRA DATA

---

## 🔄 Maintenance Workflow

### Weekly/Bi-weekly: Update JIRA Data

```bash
cd "SSF DOCS/Excel Files"
python3 update_tracker.py
```

### After Each Refinement Session

1. Update JIRA tickets to "Ready" status
2. Export from JIRA
3. Run update script
4. Go to SESSION LOG sheet
5. Enter number of stories refined in column F

---

## 🎨 Sheet Overview

```
1. JIRA DATA       → Source data with Labels & PI columns
2. DASHBOARD       → Overview metrics + link to PI PROGRESS
3. PI PROGRESS     → NEW! PI-level tracking
4. SESSION CALENDAR → Session schedule
5. SESSIONS AGENDA  → Session planning
6. SESSION LOG     → Record refinement sessions
7. BURNDOWN CHART  → Visual progress (ideal vs actual)
8. EPIC PROGRESS   → Epic tracking with PI breakdown
9. BURNUP CHART    → Cumulative progress
```

---

## ✨ Key Features

### Auto-Calculated Metrics
- ✅ Total stories per PI
- ✅ Refined vs To Refine counts
- ✅ Epic progress within specific PIs
- ✅ Progress percentages
- ✅ Status indicators

### Formula-Driven
- ✅ All metrics update when JIRA DATA changes
- ✅ No manual counting needed
- ✅ Add new epics → formulas work automatically

### Flexible
- ✅ Works across multiple PIs
- ✅ Track epics independently or by PI
- ✅ Easy to update with fresh exports

---

## 🆘 Troubleshooting

### Issue: PI PROGRESS shows "None"
**Solution:** File needs to be opened in Excel/Google Sheets for formulas to calculate. The `data_only=True` flag when reading shows None.

### Issue: Different numbers than expected
**Solution:** Check JIRA export date. Data reflects state at export time (10/11/2025).

### Issue: Want to track more PIs
**Solution:** Just export JIRA data with additional PI labels. Script auto-detects all PIs.

---

## 📞 Quick Reference Commands

```bash
# Navigate to folder
cd "SSF DOCS/Excel Files"

# Run update script
python3 update_tracker.py

# Check validation
python3 -c "import openpyxl; wb = openpyxl.load_workbook('DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx'); print(f'Total issues: {wb[\"JIRA DATA\"].max_row - 2}')"
```

---

**File Location:** `/Users/nicolas.palazzo/Documents/AI Workspaces/SSF DOCS/Excel Files/DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx`

**Last Updated:** November 15, 2025  
**Data Source:** SSF_BACKLOG_EXPORT_10_11.xlsx (exported 10/11/2025)
