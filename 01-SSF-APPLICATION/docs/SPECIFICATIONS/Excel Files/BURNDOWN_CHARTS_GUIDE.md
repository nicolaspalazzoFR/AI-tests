# 📉 Burndown Charts & PI Tracking Guide

**Updated:** November 15, 2025  
**File:** `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx`

---

## 🎯 What's New

### ✅ Fixed Issues
1. **EPIC PROGRESS now works** - Shows correct counts (was showing 0s)
2. **PI-level burndown charts** - Separate charts for SSF_PI#01 and SSF_PI#02
3. **Flexible session counts** - Change target sessions anytime
4. **Filtered session logs** - Each PI has its own session tracking

---

## 📊 New Sheet Structure

```
1. JIRA DATA                  → Source data
2. DASHBOARD                  → Overview metrics
3. PI PROGRESS                → PI-level summary
4. SESSION CALENDAR           → Session schedule
5. SESSIONS AGENDA            → Session planning
6. SESSION LOG                → MASTER log (you update this!)
7. BURNDOWN CHART DATA        → Overall burndown
8. EPIC PROGRESS              → ✅ FIXED - Now shows correct values
9. BURNUP CHART DATA          → Overall burnup

🆕 10. SSF_PI#01 SESSION LOG   → Auto-filtered from master
🆕 11. SSF_PI#01 BURNDOWN      → PI#01 ideal vs actual chart
🆕 12. SSF_PI#02 SESSION LOG   → Auto-filtered from master  
🆕 13. SSF_PI#02 BURNDOWN      → PI#02 ideal vs actual chart
```

---

## 🔧 How EPIC PROGRESS Now Works

### What Changed
- **Before:** Column A had Epic IDs (SSF-123) → formulas found nothing → showed 0
- **After:** Column A has Epic Names (Gear Management) → formulas work correctly

### Current Epic Data (from JIRA export 10/11/2025)

| Epic Name | Total | Open | Ready | % Complete |
|-----------|-------|------|-------|------------|
| Gear Management | 14 | 13 | 1 | 7.1% |
| Departure Declaration | 5 | 5 | 0 | 0% |
| Login | 16 | 3 | 8 | 50% |
| Tracking | 8 | 1 | 6 | 75% |
| (13 epics total) | | | | |

### To Track Epic Progress by PI
1. Go to **EPIC PROGRESS** sheet
2. Find your epic (e.g., "Gear Management" in Column A)
3. In **Column J (PI Filter)**, enter: `SSF_PI#02`
4. Columns K, L, M auto-calculate:
   - **K (Refined in PI):** 1
   - **L (Total in PI):** 14
   - **M (PI Progress):** "1/14"

---

## 📝 How to Use: Master SESSION LOG

This is the ONLY place you need to enter data manually. All other sheets auto-update from here!

### Workflow After Each Refinement Session

1. **Open SESSION LOG sheet**

2. **Find the session row** (e.g., Session 3 = Row 5)

3. **Fill in Column K "PI(s) Worked":**
   ```
   Examples:
   - Working on PI#02 only: SSF_PI#02
   - Working on multiple PIs: SSF_PI#01, SSF_PI#02
   - Leave blank if session didn't work on specific PIs
   ```

4. **Fill in Column F "Stories Refined":**
   ```
   Example: 5
   (Number of stories moved to "Ready" status)
   ```

5. **Everything else auto-calculates:**
   - Cumulative (Column G)
   - Remaining (Column H)
   - Velocity (Column I)
   - PI-specific session logs update
   - All burndown charts update

---

## 📉 Understanding PI Burndown Charts

### Sheet: SSF_PI#02 BURNDOWN

#### Configuration (YOU CAN EDIT!)

```
Cell B1: TARGET SESSIONS = 15  ← EDITABLE! Change anytime
Cell B2: TOTAL STORIES = 35    ← Auto-calculated from JIRA
```

#### What the Chart Shows

**Two Lines:**
1. **IDEAL (Blue)** - Perfect pace to finish on time
   - Starts at 35 stories
   - Decreases by 35/15 = 2.33 stories per session
   - Reaches 0 at session 15

2. **ACTUAL (Red)** - Your real progress
   - Based on stories you actually refined
   - Updates when you fill SESSION LOG

**Variance Column:** Shows if you're ahead (+) or behind (-)

### Example Data

| Session | IDEAL | ACTUAL | Variance |
|---------|-------|--------|----------|
| 0 | 35 | 35 | 0 |
| 1 | 32.67 | 35 | +2.33 (behind) |
| 2 | 30.33 | 33 | +2.67 (behind) |
| 3 | 28 | 28 | 0 (on track!) |

---

## 🔄 How Filtering Works (Option B Implementation)

### Master → PI Session Logs

**You enter in:**
- `SESSION LOG` Column F (Stories Refined)
- `SESSION LOG` Column K (PI(s) Worked)

**Formula in SSF_PI#02 SESSION LOG Column F:**
```excel
=IF(ISNUMBER(SEARCH("SSF_PI#02",'SESSION LOG'!K3)),'SESSION LOG'!F3,0)
```

**What it does:**
- Checks if "SSF_PI#02" is mentioned in SESSION LOG Column K
- If YES → copies the Stories Refined value
- If NO → shows 0

**Example:**
```
SESSION LOG (Master):
Row 3: F=5, K="SSF_PI#02"           → PI#02 log shows: 5
Row 4: F=3, K="SSF_PI#01"           → PI#02 log shows: 0
Row 5: F=7, K="SSF_PI#01, SSF_PI#02" → PI#02 log shows: 7
```

---

## 🎨 Changing Target Sessions

### Why You Might Need This
- Initially planned 15 sessions but now have 20
- Want to compress into 10 intensive sessions
- Adjusting based on team availability

### How to Change

1. **Open PI BURNDOWN sheet** (e.g., SSF_PI#02 BURNDOWN)

2. **Click cell B1** (currently shows 15)

3. **Type new number** (e.g., 20)

4. **Press Enter**

5. **IDEAL line automatically recalculates!**
   - New slope: 35/20 = 1.75 stories per session
   - Chart updates instantly

### Effect on Different Sheets

| Sheet | Effect |
|-------|--------|
| SSF_PI#02 BURNDOWN | ✅ IDEAL line updates |
| SSF_PI#02 SESSION LOG | ❌ No change (shows actual data) |
| SESSION LOG (master) | ❌ No change (your input) |

---

## 📈 Typical Workflow Example

### Day 1: Setup
1. Open tracker
2. Check PI PROGRESS to see totals
3. Note: PI#02 has 35 stories

### After Session 1 (Nov 5):
1. Go to SESSION LOG
2. Row 3 (Session 1):
   - Column F: Enter `5` (refined 5 stories)
   - Column K: Enter `SSF_PI#02`
3. Save file
4. Check SSF_PI#02 BURNDOWN → Chart updates!
5. ACTUAL line shows: 35 → 30

### After Session 2 (Nov 7):
1. Go to SESSION LOG
2. Row 4 (Session 2):
   - Column F: Enter `3`
   - Column K: Enter `SSF_PI#02`
3. Check SSF_PI#02 BURNDOWN → Now shows: 30 → 27
4. Check velocity trend

### Week 3: Scope Change
1. Management says: "We need 20 sessions, not 15"
2. Go to SSF_PI#02 BURNDOWN
3. Change B1 from 15 to 20
4. IDEAL line becomes gentler slope
5. Continue tracking as normal

---

## 🎯 Reading the Charts

### You're On Track When:
- ✅ ACTUAL line follows IDEAL closely
- ✅ Variance near 0
- ✅ Consistent velocity

### You're Ahead When:
- 🟢 ACTUAL below IDEAL
- 🟢 Negative variance
- 🟢 More stories refined than planned

### You're Behind When:
- 🔴 ACTUAL above IDEAL
- 🔴 Positive variance
- 🔴 Fewer stories refined than planned

### Action Items Based on Chart

**Scenario 1: Consistently Behind**
```
Action: 
- Increase session frequency
- Adjust target sessions upward
- Identify refinement blockers
```

**Scenario 2: Ahead of Schedule**
```
Action:
- Consider adding more stories
- Help other PIs
- Reduce session frequency
```

**Scenario 3: Erratic Pattern**
```
Action:
- Investigate session quality
- Check story size consistency
- Review team availability
```

---

## 🔍 Troubleshooting

### Issue: Epic Progress Still Shows 0

**Cause:** Epic names might not match exactly

**Solution:**
1. Check JIRA DATA Column F for exact epic name
2. Update EPIC PROGRESS Column A to match exactly
3. Or re-run: `python3 fix_tracker_charts.py`

### Issue: PI Burndown Not Updating

**Possible Causes:**
1. ❌ Forgot to enter PI in SESSION LOG Column K
2. ❌ Typo in PI label (case-sensitive!)
3. ❌ File not saved after entering data

**Solution:**
1. Verify Column K has correct PI label
2. Check spelling: "SSF_PI#02" not "SSF-PI#02"
3. Save file and reopen

### Issue: Want Different Target Sessions for Different PIs

**This is normal!** Each PI can have its own target:
- SSF_PI#01 BURNDOWN B1 = 10 sessions
- SSF_PI#02 BURNDOWN B1 = 20 sessions

They're independent.

### Issue: Chart Shows Wrong Total Stories

**Cause:** JIRA data might be outdated

**Solution:**
1. Export fresh JIRA data
2. Run: `python3 update_tracker.py`
3. Cell B2 in burndown will update automatically

---

## 📚 Formulas Reference

### Master SESSION LOG

| Column | Formula | Purpose |
|--------|---------|---------|
| F | Manual entry | Stories refined this session |
| G | `=SUM($F$3:F3)` | Cumulative total |
| H | `=DASHBOARD!$C$7-G3` | Stories remaining |
| K | Manual entry | PI(s) worked on |

### PI SESSION LOG (e.g., SSF_PI#02)

| Column | Formula | Purpose |
|--------|---------|---------|
| F | `=IF(ISNUMBER(SEARCH("SSF_PI#02",...))` | Filtered stories refined |
| G | `=SUM($F$3:F3)` | PI-specific cumulative |
| H | `=COUNTIF('JIRA DATA'!J:J,"SSF_PI#02")-G3` | PI stories remaining |

### PI BURNDOWN

| Column | Formula | Purpose |
|--------|---------|---------|
| C | `=$B$2-($B$2/$B$1)*A5` | IDEAL remaining |
| D | `='SSF_PI#02 SESSION LOG'!H3` | ACTUAL remaining |
| E | `=D5-C5` | Variance |

---

## 💡 Best Practices

### 1. Consistent Data Entry
- ✅ Enter session data immediately after sessions
- ✅ Use standard PI label format: `SSF_PI#XX`
- ✅ Be accurate with refined story counts

### 2. Regular Reviews
- 📅 Weekly: Check all PI burndowns
- 📅 Bi-weekly: Update target sessions if needed
- 📅 Monthly: Review EPIC PROGRESS by PI

### 3. Team Communication
- 📢 Share burndown charts in standup
- 📢 Discuss variance in retrospectives
- 📢 Celebrate when ahead of schedule!

### 4. Adjustments
- 🔄 Don't be afraid to adjust target sessions
- 🔄 Update as you learn actual velocity
- 🔄 Realistic targets > optimistic ones

---

## 🆘 Quick Commands

```bash
# Navigate to folder
cd "SSF DOCS/Excel Files"

# Update from fresh JIRA export
python3 update_tracker.py

# Regenerate all PI burndowns
python3 fix_tracker_charts.py

# Check epic counts
python3 -c "import openpyxl; wb=openpyxl.load_workbook('DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx'); [print(f'{wb[\"EPIC PROGRESS\"].cell(r,1).value}: {wb[\"EPIC PROGRESS\"].cell(r,3).value}') for r in range(3,10)]"
```

---

## 📞 Support

For issues or questions:
1. Check this guide first
2. Review TRACKER_UPDATE_SUMMARY.md
3. Verify formulas in sheets
4. Re-run fix script if needed

---

**Remember:** The tracker is a tool to help you, not restrict you. Adjust it to fit your team's needs!

**File Location:** `/Users/nicolas.palazzo/Documents/AI Workspaces/SSF DOCS/Excel Files/DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx`
