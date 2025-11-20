# 📝 Manual Setup Guide for Microsoft 365 Online

**Total Time:** ~35 minutes  
**Result:** Fully functional tracker with PI Progress and Charts  
**Compatible:** 100% Microsoft 365 Online

---

## 🎯 Overview

This guide will help you manually create all the features you need directly in Excel Online, avoiding all Python compatibility issues.

**What You'll Create:**
- ✅ JIRA DATA with Labels + PI columns
- ✅ PI PROGRESS sheet
- ✅ Fixed EPIC PROGRESS  
- ✅ SESSION LOG with PI tracking
- ✅ PI SESSION LOG sheets
- ✅ PI BURNDOWN sheets with CHARTS

---

## 📂 Part 1: Update JIRA DATA Sheet (5 minutes)

### Step 1.1: Add Labels Column

1. Open `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx` in Excel Online
2. Go to **JIRA DATA** sheet
3. Right-click column **H** header
4. Click **Insert** → **Insert Columns to the Left**
5. Click cell **H2**
6. Type: `Labels`
7. Format: Bold, White text, Blue background (to match other headers)

### Step 1.2: Add PI Column

1. Right-click column **J** header  
2. Click **Insert** → **Insert Columns to the Left**
3. Click cell **J2**
4. Type: `PI`
5. Format: Bold, White text, Blue background

### Step 1.3: Import Data

1. Open `SSF_BACKLOG_EXPORT_10_11.xlsx` in a **second tab**
2. In that file, select rows 5-95 (all 91 data rows)
3. Copy (Ctrl+C)
4. Go back to tracker file, JIRA DATA sheet
5. Click cell **A3**
6. Paste (Ctrl+V)
7. Data should fill columns A-I

### Step 1.4: Extract PI Labels

1. Click cell **J3**
2. Paste this formula:
   ```excel
   =IF(ISNUMBER(SEARCH("SSF_PI#",H3)),MID(H3,SEARCH("SSF_PI#",H3),10),"")
   ```
3. Press Enter
4. Click cell **J3** again
5. Drag the fill handle down to row 93 (or double-click it)
6. Column J now has PI labels extracted!

**✅ Part 1 Complete!**

---

## 📊 Part 2: Fix EPIC PROGRESS (2 minutes)

### Step 2.1: Update Epic Names

The formulas are already there, we just need to update Column A from Epic IDs to Epic Names.

1. Go to **EPIC PROGRESS** sheet
2. **Manually type** these epic names in Column A (starting row 3):

```
Row 3:  App Menu
Row 4:  Data Exchange w/FMC
Row 5:  Departure Declaration
Row 6:  Gear Management
Row 7:  Hauls
Row 8:  Home Screen
Row 9:  INFRA
Row 10: Language Management
Row 11: Login
Row 12: Logs
Row 13: Map Integrations
Row 14: TECH REQUIREMENTS
Row 15: Vessel Tracking
```

3. Press Enter after each one
4. Formulas will automatically recalculate!
5. You should see numbers appear in columns C, D, E

**✅ Part 2 Complete!**

---

## 📈 Part 3: Create PI PROGRESS Sheet (5 minutes)

### Step 3.1: Create New Sheet

1. Click **+** at bottom to add new sheet
2. Rename it: `PI PROGRESS`
3. Drag it to position 3 (after DASHBOARD)

### Step 3.2: Add Title

1. Click cell **A1**
2. Type: `PI PROGRESS TRACKER`
3. Format: Bold, Size 16, White text, Blue background
4. Merge cells A1:H1

### Step 3.3: Add Headers (Row 2)

Click each cell and type:
```
A2: PI Label
B2: Total Stories
C2: Refined (Ready)
D2: To Refine (Open)
E2: Other Status
F2: % Complete
G2: Progress
H2: Status
```

Format all: Bold, White text, Green background

### Step 3.4: Add PI Data

**Row 3 - SSF_PI#01:**

Click each cell and paste:
```
A3: SSF_PI#01
B3: =COUNTIF('JIRA DATA'!J:J,A3)
C3: =COUNTIFS('JIRA DATA'!J:J,A3,'JIRA DATA'!E:E,"Ready")
D3: =COUNTIFS('JIRA DATA'!J:J,A3,'JIRA DATA'!E:E,"Open")
E3: =B3-C3-D3
F3: =IF(B3=0,0,C3/B3)
G3: =C3&"/"&B3
H3: =IF(F3>0.7,"🟢",IF(F3>0.3,"🟡","🔴"))
```

**Row 4 - SSF_PI#02:**

Click each cell and paste:
```
A4: SSF_PI#02
B4: =COUNTIF('JIRA DATA'!J:J,A4)
C4: =COUNTIFS('JIRA DATA'!J:J,A4,'JIRA DATA'!E:E,"Ready")
D4: =COUNTIFS('JIRA DATA'!J:J,A4,'JIRA DATA'!E:E,"Open")
E4: =B4-C4-D4
F4: =IF(B4=0,0,C4/B4)
G4: =C4&"/"&B4
H4: =IF(F4>0.7,"🟢",IF(F4>0.3,"🟡","🔴"))
```

### Step 3.5: Format Column F

1. Select cells F3:F4
2. Right-click → Format Cells
3. Choose: Percentage, 1 decimal place

**✅ Part 3 Complete! You now have PI PROGRESS!**

---

## 📝 Part 4: Add PI Column to SESSION LOG (2 minutes)

### Step 4.1: Add Column

1. Go to **SESSION LOG** sheet
2. Click cell **K2**
3. Type: `PI(s) Worked`
4. Format: Bold, White text, Green background

### Step 4.2: Add Instructions

1. Click cell **K3**
2. Type: `Enter PI labels: SSF_PI#01, SSF_PI#02, etc.`
3. Format: Italic, Gray text

**✅ Part 4 Complete!**

---

## 📊 Part 5: Create PI SESSION LOGS (10 minutes each PI)

### Step 5.1: Create SSF_PI#01 SESSION LOG

1. Click **+** to add new sheet
2. Rename: `SSF_PI#01 SESSION LOG`

**Title (Row 1):**
```
A1: SSF_PI#01 REFINEMENT SESSION LOG
Merge A1:I1, Bold, Size 14, White text, Blue background
```

**Headers (Row 2):**
```
A2: Session #
B2: Sprint
C2: Date
D2: PI(s) Worked
E2: Target Stories
F2: Stories Refined
G2: Cumulative
H2: Remaining
I2: Velocity
```
Format: Bold, White text, Green background

**Formulas (Copy these to rows 3-19):**

Row 3 formulas:
```
A3: 1
B3: ='SESSION LOG'!B3
C3: ='SESSION LOG'!C3
D3: ='SESSION LOG'!K3
E3: ='SESSION LOG'!E3
F3: =IF(ISNUMBER(SEARCH("SSF_PI#01",'SESSION LOG'!K3)),'SESSION LOG'!F3,0)
G3: =SUM($F$3:F3)
H3: =COUNTIF('JIRA DATA'!J:J,"SSF_PI#01")-G3
I3: =F3
```

Row 4 formulas:
```
A4: 2
B4: ='SESSION LOG'!B4
C4: ='SESSION LOG'!C4
D4: ='SESSION LOG'!K4
E4: ='SESSION LOG'!E4
F4: =IF(ISNUMBER(SEARCH("SSF_PI#01",'SESSION LOG'!K4)),'SESSION LOG'!F4,0)
G4: =SUM($F$3:F4)
H4: =COUNTIF('JIRA DATA'!J:J,"SSF_PI#01")-G4
I4: =AVERAGE($F$3:F4)
```

**Copy rows 4 down to row 19** (change row numbers accordingly)
- Column A: increment session numbers (3, 4, 5...)
- Columns B-I: adjust row references (B5, C5, etc.)

### Step 5.2: Create SSF_PI#02 SESSION LOG

Repeat Step 5.1 exactly, but:
- Sheet name: `SSF_PI#02 SESSION LOG`
- Title: `SSF_PI#02 REFINEMENT SESSION LOG`
- In formulas, replace `"SSF_PI#01"` with `"SSF_PI#02"`

**✅ Part 5 Complete!**

---

## 📉 Part 6: Create PI BURNDOWN Sheets with Charts (15 minutes each)

### Step 6.1: Create SSF_PI#01 BURNDOWN Sheet

1. Click **+** to add new sheet
2. Rename: `SSF_PI#01 BURNDOWN`

**Configuration Cells:**
```
A1: TARGET SESSIONS:
B1: 15
Format B1: Bold, Red text, Yellow background

A2: TOTAL STORIES:
B2: =COUNTIF('JIRA DATA'!J:J,"SSF_PI#01")
Format: Bold
```

**Title:**
```
D1: SSF_PI#01 BURNDOWN DATA
Merge D1:H1, Bold, Size 14, White text, Blue background
```

**Headers (Row 4):**
```
A4: Session #
B4: Sprint
C4: IDEAL Remaining
D4: ACTUAL Remaining
E4: Variance
```
Format: Bold, White text, Green background

**Data Formulas (Rows 5-21):**

Row 5:
```
A5: 0
B5: ='SSF_PI#01 SESSION LOG'!B3
C5: =$B$2-($B$2/$B$1)*A5
D5: ='SSF_PI#01 SESSION LOG'!H3
E5: =D5-C5
```

Row 6:
```
A6: 1
B6: ='SSF_PI#01 SESSION LOG'!B4
C6: =$B$2-($B$2/$B$1)*A6
D6: ='SSF_PI#01 SESSION LOG'!H4
E6: =D6-C6
```

**Continue** for rows 7-21:
- Column A: increment (2, 3, 4...)
- Column B: adjust row ref (B5, B6...)
- Column C: adjust row ref (A7, A8...)
- Column D: adjust row ref (H5, H6...)
- Column E: adjust row ref (D7-C7, D8-C8...)

### Step 6.2: Create the Chart

1. **Select** cells **C4:D21** (IDEAL and ACTUAL columns)
2. Click **Insert** tab
3. Click **Charts** → **Line Chart**
4. Chart appears!

**Format the Chart:**
1. Click chart title
2. Type: `SSF_PI#01 - Ideal vs Actual`
3. Click chart
4. Use Chart Tools to:
   - Axis titles: X = "Session #", Y = "Stories Remaining"
   - Legend: Show IDEAL and ACTUAL
   - Colors: Blue for IDEAL, Red for ACTUAL

### Step 6.3: Create SSF_PI#02 BURNDOWN Sheet

Repeat Steps 6.1-6.2 exactly, but:
- Sheet name: `SSF_PI#02 BURNDOWN`
- Title: `SSF_PI#02 BURNDOWN DATA`
- In formulas, replace `'SSF_PI#01 SESSION LOG'` with `'SSF_PI#02 SESSION LOG'`
- In B2, replace `"SSF_PI#01"` with `"SSF_PI#02"`
- Chart title: `SSF_PI#02 - Ideal vs Actual`

**✅ Part 6 Complete! You have burndowns with charts!**

---

## 🎉 DONE! What You Now Have:

✅ **JIRA DATA** - with Labels (H) and PI (J) columns  
✅ **PI PROGRESS** - shows PI#01 and PI#02 status  
✅ **EPIC PROGRESS** - fixed, showing real numbers  
✅ **SESSION LOG** - with PI(s) Worked column (K)  
✅ **PI SESSION LOGS** - filtered per PI  
✅ **PI BURNDOWN sheets** - with CHARTS showing Ideal vs Actual  

---

## 📝 How To Use Going Forward

### After Each Refinement Session:

1. Go to **SESSION LOG**
2. Find your session row (e.g., Session 3 = Row 5)
3. **Column F:** Enter stories refined (e.g., 5)
4. **Column K:** Enter `SSF_PI#02` (or relevant PI)
5. Save

**Everything auto-updates:**
- PI PROGRESS recalculates
- EPIC PROGRESS updates
- PI SESSION LOGS filter the data
- PI BURNDOWN sheets + charts update
- ACTUAL line on charts moves

### To Track Epic Progress by PI:

1. Go to **EPIC PROGRESS**
2. Find epic row (e.g., "Gear Management")
3. **Column J:** Type `SSF_PI#02`
4. Columns K, L, M automatically show progress for that epic in that PI

### To Adjust Target Sessions:

1. Go to PI BURNDOWN sheet
2. Click cell **B1**
3. Change number (e.g., 15 → 20)
4. IDEAL line recalculates automatically
5. Chart updates

---

## 🔧 Troubleshooting

### Formulas Show as Text?

- Click the cell
- Press F2 to edit
- Press Enter
- Should calculate

### #NAME? Error?

- Click any cell with error
- Press F2
- Press Enter
- All similar formulas recalculate

### Chart Not Showing?

- Make sure you selected C4:D21 (both columns)
- Try Insert → Recommended Charts → Line

---

## 💾 Saving Your Work

**Important:** Save frequently!
- After each major section
- Before creating charts
- After creating charts

This ensures you don't lose progress.

---

## 📊 Expected Results

### PI PROGRESS Sheet:
```
SSF_PI#01: 40 total stories
SSF_PI#02: 35 total stories
```

### EPIC PROGRESS:
```
Gear Management: 14 total, 13 open, 1 ready
(All should show numbers, no #NAME?)
```

### PI BURNDOWN Charts:
- Blue line: IDEAL (straight diagonal)
- Red line: ACTUAL (will update as you enter sessions)
- Should cross at target session if on track

---

## ✅ Quality Check

Before sharing with client, verify:
- [ ] JIRA DATA has 91 rows of data
- [ ] Column H (Labels) has data
- [ ] Column J (PI) has extracted PIs
- [ ] PI PROGRESS shows 2 PIs with numbers
- [ ] EPIC PROGRESS shows numbers (no errors)
- [ ] SESSION LOG has Column K header
- [ ] Both PI SESSION LOG sheets exist
- [ ] Both PI BURNDOWN sheets exist
- [ ] Charts display in burndown sheets
- [ ] Can edit and save file

---

## 🎯 Quick Formula Reference

### PI Extraction (JIRA DATA J3):
```excel
=IF(ISNUMBER(SEARCH("SSF_PI#",H3)),MID(H3,SEARCH("SSF_PI#",H3),10),"")
```

### PI Progress Total (PI PROGRESS B3):
```excel
=COUNTIF('JIRA DATA'!J:J,A3)
```

### PI Progress Refined (PI PROGRESS C3):
```excel
=COUNTIFS('JIRA DATA'!J:J,A3,'JIRA DATA'!E:E,"Ready")
```

### Filtered Sessions (PI SESSION LOG F3):
```excel
=IF(ISNUMBER(SEARCH("SSF_PI#01",'SESSION LOG'!K3)),'SESSION LOG'!F3,0)
```

### Ideal Remaining (PI BURNDOWN C5):
```excel
=$B$2-($B$2/$B$1)*A5
```

---

## 💡 Tips

1. **Copy formulas carefully** - one wrong character breaks it
2. **Adjust row/column references** when copying down
3. **Save after each section**
4. **Test formulas** by entering dummy data in SESSION LOG
5. **Charts update automatically** when data changes

---

## 📞 If You Get Stuck

Common issues and fixes:

**Issue:** Formulas don't calculate
- **Fix:** Press Ctrl+Alt+F9

**Issue:** Can't find sheet reference
- **Fix:** Sheet names must be exact (case-sensitive)

**Issue:** Chart doesn't update
- **Fix:** Right-click chart → Refresh Data

---

**This manual approach works 100% in Microsoft 365 Online!**

No Python compatibility issues, no file corruption, fully editable!
