# 🔧 Troubleshooting #NAME? Error in EPIC PROGRESS

## 📋 Issue Description

After running the tracker update scripts, you may see **#NAME?** errors in the EPIC PROGRESS sheet, specifically in columns C, D, E, F, G, K, L, and M.

---

## 🎯 Root Cause

The #NAME? error occurs when Excel doesn't recognize a formula or function name. In our case, this happens because:

1. **Formulas were written programmatically** using Python (openpyxl)
2. **Excel hasn't calculated them yet** - it shows the text of the formula instead of evaluating it
3. **Sheet references** using single quotes (e.g., `'JIRA DATA'`) sometimes need Excel to "wake up"

**Important:** The formulas ARE correct! Excel just needs to recalculate them.

---

## ✅ Solution (Quick Fix)

### Option 1: Force Recalculation (Fastest)

1. **Open** `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx` in Excel
2. **Press** `Ctrl+Alt+F9` on your keyboard
3. **Wait** a few seconds for Excel to recalculate
4. **Save** the file

### Option 2: Use Excel's Calculate Now Feature

1. **Open** the tracker file in Excel
2. **Go to** the Formulas tab
3. **Click** "Calculate Now" button
4. **Wait** for Excel to recalculate
5. **Save** the file

### Option 3: Re-run the Fix Script

If the above doesn't work, run:

```bash
cd "SSF DOCS/Excel Files"
python3 fix_name_error.py
```

Then open the file in Excel and save it immediately.

---

## 📊 What Should You See After Fix?

### EPIC PROGRESS Sheet - Expected Values:

| Epic Name | Total | Open | Ready | % Complete |
|-----------|-------|------|-------|------------|
| Gear Management | 14 | 13 | 1 | 7.1% |
| Login | 16 | 3 | 8 | 50% |
| Tracking | 8 | 1 | 6 | 75% |
| (etc.) | | | | |

**All values should be numbers, NOT #NAME?**

---

## 🔍 Why This Happens

When Python writes formulas to Excel files:
1. Python creates the formula as a **string** (e.g., `"=COUNTIF('JIRA DATA'!F:F,A3)"`)
2. openpyxl marks it as a formula
3. But Excel doesn't **evaluate** it until you open the file and trigger calculation

### Common Triggers for #NAME? Error:
- ❌ Sheet names with spaces need single quotes
- ❌ Function names in wrong language (e.g., CONTAR vs COUNTIF)
- ❌ Excel hasn't calculated yet after programmatic write
- ❌ Circular references

### Why Our Formulas Are Correct:
- ✅ Sheet names properly quoted: `'JIRA DATA'!F:F`
- ✅ English function names: COUNTIF, COUNTIFS, IF
- ✅ No circular references
- ⚠️  Just need Excel to calculate them!

---

## 🧪 Testing the Fix

After applying one of the solutions above:

1. **Go to EPIC PROGRESS sheet**
2. **Click on cell C3** (should show the epic "App Menu")
3. **Look at the formula bar** - should show: `=COUNTIF('JIRA DATA'!F:F,A3)`
4. **Check the cell value** - should be a number (not #NAME?)

If cell C3 works, all formulas should work!

---

## 🔄 Alternative: Manual Formula Entry

If automatic recalculation doesn't work, you can manually re-enter ONE formula:

1. **Click cell C3** in EPIC PROGRESS
2. **Press F2** to edit
3. **Press Enter** without changing anything
4. **Excel should recalculate ALL similar formulas**

---

## 📝 Formula Reference for EPIC PROGRESS

For manual verification, here are the correct formulas:

### Row 3 Example (App Menu):

- **C3 (Total):** `=COUNTIF('JIRA DATA'!F:F,A3)`
- **D3 (Open):** `=COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Open")`
- **E3 (Ready):** `=COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!E:E,"Ready")`
- **F3 (Other):** `=C3-D3-E3`
- **G3 (% Complete):** `=IF(C3=0,0,E3/C3)`
- **K3 (Refined in PI):** `=IF(J3="","-",COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!J:J,J3,'JIRA DATA'!E:E,"Ready"))`
- **L3 (Total in PI):** `=IF(J3="","-",COUNTIFS('JIRA DATA'!F:F,A3,'JIRA DATA'!J:J,J3))`
- **M3 (PI Progress):** `=IF(J3="","-",K3&"/"&L3)`

---

## 🚨 If Nothing Works

If you've tried everything and still see #NAME? errors:

1. **Check Excel language settings**
   - Function names might need to be in your local language
   - Example: COUNTIF in English = CONTAR in Spanish

2. **Verify JIRA DATA sheet name**
   - Make sure it's exactly "JIRA DATA" (with space)
   - Check there are no extra spaces

3. **Re-run the complete fix:**
   ```bash
   cd "SSF DOCS/Excel Files"
   python3 fix_tracker_charts.py
   python3 fix_name_error.py
   ```

4. **Contact support** with screenshot showing:
   - The #NAME? error
   - The formula bar content
   - Your Excel version

---

## ✅ Success Checklist

After fixing, verify:

- ✅ EPIC PROGRESS Column C shows numbers (Total count)
- ✅ EPIC PROGRESS Column D shows numbers (Open count)
- ✅ EPIC PROGRESS Column E shows numbers (Ready count)
- ✅ EPIC PROGRESS Column G shows percentages
- ✅ All formulas in EPIC PROGRESS work
- ✅ PI PROGRESS sheet shows numbers (not formulas)
- ✅ PI BURNDOWN sheets work correctly

---

## 💡 Prevention for Next Time

When updating the tracker in the future:

1. **After running update scripts**, immediately open in Excel
2. **Force recalculation** (Ctrl+Alt+F9)
3. **Save the file** in Excel
4. **Close and reopen** to verify

This ensures formulas are "activated" in Excel.

---

**Last Updated:** November 15, 2025  
**File:** `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx`
