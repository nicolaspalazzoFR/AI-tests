# 📊 How to Use the SSF Refinement Tracker & Session Planner

## 🎯 Quick Start

Your Excel file **SSF_Refinement_Tracker_Session_Planner.xlsx** has been created with 6 sheets, all with corrected formulas that work perfectly with Google Sheets.

---

## 📥 Step 1: Import to Google Sheets

1. Go to [Google Sheets](https://sheets.google.com)
2. Click **File** → **Import**
3. Select **Upload** tab
4. Drag and drop `SSF_Refinement_Tracker_Session_Planner.xlsx`
5. Choose **Replace spreadsheet** (if updating) or **Create new spreadsheet**
6. Click **Import data**

✅ **All formulas will work automatically!** No manual fixes needed.

---

## 📋 Step 2: After Each Refinement Session

**ONLY UPDATE ONE COLUMN:**

1. Go to the **SESSION LOG** sheet
2. Find the row for the session you just completed
3. **Enter the number of stories refined** in column F (Stories Refined)
4. That's it! Everything else updates automatically.

### Example:
If you completed Session 3 and refined 7 stories:
- Go to row 5 (Session 3)
- Enter `7` in cell F5
- All dashboards, charts, and metrics update automatically

---

## 📊 What's in Each Sheet

### 1. DASHBOARD
- **Quick Metrics**: Total stories, progress %, velocity
- **Status Indicators**: On track / At risk / Critical
- **Session Summary**: Last 3 sessions
- **Weekly Report**: Auto-generated text you can copy/paste

### 2. SESSION LOG
- **The only sheet you need to update manually**
- All 15 sessions pre-configured with dates
- Just enter numbers in column F after each session

### 3. BURNDOWN CHART DATA
- Tracks stories remaining vs. ideal burndown
- Use this data to create a line chart
- Shows if you're ahead or behind schedule

### 4. BURNUP CHART DATA
- Tracks stories completed vs. target
- Shows cumulative progress toward 84 stories
- Visualizes the gap between actual and target

### 5. EPIC PROGRESS
- Breakdown by Epic
- Shows % complete for each feature area
- Helps prioritize which epics need focus

### 6. SESSION CALENDAR
- All 13 remaining sessions with dates
- Pre-prep deadlines (48h before)
- Status tracking per session

---

## 📈 Built-in Charts

### Burndown Chart (BURNDOWN CHART DATA sheet)
**Automatically included!** Shows actual progress vs. ideal burndown:
- **Blue line**: Ideal burndown (target pace to finish 84 stories)
- **Orange line**: Actual progress (stories remaining after each session)
- Updates automatically as you enter data in SESSION LOG

**What it shows:** If the orange line is above blue, you're behind schedule. If it's below blue, you're ahead!

### Burnup Chart (BURNUP CHART DATA sheet)
**Automatically included!** Shows cumulative progress vs. target:
- **Blue line**: Target progress (ideal pace)
- **Green line**: Actual progress (stories completed)
- **Gray dashed line**: Total scope (84 stories goal)
- Updates automatically as you enter data in SESSION LOG

**What it shows:** The gap between green and blue shows if you're on track. The green line should reach the gray line by Session 15.

### Creating Additional Charts in Google Sheets (Optional)
If you want to create custom charts:

**Epic Progress Bar Chart:**
1. Go to **EPIC PROGRESS** sheet
2. Select columns A and G (Epic ID and % Complete)
3. Click **Insert** → **Chart**
4. Choose **Bar chart**
5. Sort by % complete to see which epics are ready

---

## ✅ Key Features

### ✨ Automatic Calculations
- **Cumulative Stories**: Adds up all refined stories automatically
- **Remaining Stories**: Subtracts from 84 total
- **Velocity**: Calculates average stories per session
- **Progress %**: Shows completion percentage
- **Status Indicators**: 🟢 On Track / 🟡 At Risk / 🔴 Critical
- **Projected Completion**: Estimates which sprint you'll finish in

### 📈 Real-Time Metrics
- Current velocity vs. target (6.5 stories/session)
- Risk level based on remaining stories
- Session summary showing last 3 sessions
- Weekly report with key metrics

### 🔧 All Formulas Fixed
All the formula errors from the CSV version are corrected:
- ✅ No #REF! errors
- ✅ No #DIV/0! errors
- ✅ No #VALUE! errors
- ✅ Sheet name references work correctly
- ✅ INDEX/COUNTA formulas properly configured

---

## 💡 Tips for Success

1. **Update immediately after each session** - Don't wait, the data stays fresh
2. **Check the DASHBOARD weekly** - Monitor velocity and status
3. **Use the weekly report** - Copy/paste into Slack or email for team updates
4. **Review Epic Progress** - Ensure balanced progress across all epics
5. **Adjust dates in SESSION CALENDAR** - If your sprint schedule changes

---

## 🎯 Target Metrics

- **Target Velocity**: 6.5 stories per session
- **Total Stories to Refine**: 84 stories
- **Total Sessions**: 15 sessions
- **Target Completion**: End of Sprint 5

### Status Thresholds
- 🟢 **On Track**: Velocity ≥ 6.5 stories/session
- 🟡 **At Risk**: Velocity between 4.0 and 6.5
- 🔴 **Critical**: Velocity < 4.0 stories/session

---

## 🔄 If You Need to Start Over

Simply run the Python script again:
```bash
cd "SSF DOCS"
python3 generate_tracker.py
```

This will create a fresh copy of the Excel file.

---

## 📞 Need Help?

All formulas are documented in:
- `FORMULA_FIXES_Google_Sheets.md` - Complete formula reference
- `QUICK_START_GUIDE_Google_Sheets.md` - Setup instructions

---

**Happy tracking! 🚀**
