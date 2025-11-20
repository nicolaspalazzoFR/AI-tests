# 🔧 FORMULA FIXES - Google Sheets Refinement Tracker

## Sheet Names Confirmed
- DASHBOARD
- SESSION LOG
- BURNDOWN CHART DATA
- BURNUP CHART DATA
- EPIC PROGRESS

---

## DASHBOARD SHEET - Formula Fixes

### Fix #1: Cell C11 - Completed So Far
**Current**: `=SUM('Session Log'!F:F)` → **#REF! error**

**Fixed Formula**:
```
=SUM('SESSION LOG'!F:F)
```
**Note**: Sheet name must be exactly "SESSION LOG" (all caps, with space)

---

### Fix #2: Cell C12 - Remaining
**Current**: `=C8-C11` → May work if C11 is fixed

**Fixed Formula** (with error protection):
```
=IF(ISBLANK(C11),84,84-C11)
```
**This prevents errors if C11 is empty**

---

### Fix #3: Cell C13 - Progress %
**Current**: `=C11/C8*100` → **#DIV/0! error**

**Fixed Formula**:
```
=IF(C11=0,0,C11/C8*100)
```
**This prevents division by zero**

---

### Fix #4: Cell F2 - Current Velocity
**Current**: `=AVERAGE('Session Log'!F2:F3)` → **#REF! error**

**Fixed Formula**:
```
=IF(COUNTA('SESSION LOG'!F2:F16)=0,0,AVERAGE('SESSION LOG'!F2:F16))
```
**This calculates average of all completed sessions**

---

### Fix #5: Cell E1 - Status
**Current**: `=IF(F2>=6.5,"🟢 On Track",IF(F2>=4,"🟡 At Risk","🔴 Critical"))` → **#ERROR!**

**Fixed Formula**:
```
=IF(F2="","-",IF(F2>=6.5,"🟢 On Track",IF(F2>=4,"🟡 At Risk","🔴 Critical")))
```
**This handles empty F2**

---

### Fix #6: Cell E2 - Risk Level
**Current**: `=IF(H8-G8>5,"🔴 HIGH",IF(H8-G8>2,"🟡 MEDIUM","🟢 LOW"))` → **#ERROR!**

**Fixed Formula** (this references non-existent cells, need to recalculate):
```
=IF(C12>60,"🔴 HIGH",IF(C12>40,"🟡 MEDIUM","🟢 LOW"))
```
**This uses Remaining stories (C12) as risk indicator**

---

### Fix #7: Cell F6 - Projected Completion
**Current**: `=IF(F2>0,"Sprint "&ROUNDUP(C10/F2/3+1,0),"TBD")` → **#ERROR!**

**Fixed Formula**:
```
=IF(OR(F2=0,F2=""),"TBD","Sprint "&ROUNDUP(C12/F2/3+1,0))
```
**Uses Remaining (C12) divided by velocity to project sprint**

---

## SESSION SUMMARY (LAST 3) - Rows 18-20

### Fix #8: Row 18 - Latest Session
**Column B** (Session):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!A:A,COUNTA('SESSION LOG'!A:A)))
```

**Column C** (Sprint):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!B:B,COUNTA('SESSION LOG'!A:A)))
```

**Column D** (Date):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!C:C,COUNTA('SESSION LOG'!A:A)))
```

**Column E** (Stories Refined):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!F:F,COUNTA('SESSION LOG'!A:A)))
```

**Column F** (Cumulative):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!G:G,COUNTA('SESSION LOG'!A:A)))
```

**Column G** (Status):
```
=IF(COUNTA('SESSION LOG'!A:A)<=1,"",INDEX('SESSION LOG'!J:J,COUNTA('SESSION LOG'!A:A)))
```

---

### Fix #9: Row 19 - Second Latest Session
Use same formulas as Row 18 but change `COUNTA('SESSION LOG'!A:A)` to `COUNTA('SESSION LOG'!A:A)-1`

**Column B**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!A:A,COUNTA('SESSION LOG'!A:A)-1))
```

**Column C**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!B:B,COUNTA('SESSION LOG'!A:A)-1))
```

**Column D**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!C:C,COUNTA('SESSION LOG'!A:A)-1))
```

**Column E**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!F:F,COUNTA('SESSION LOG'!A:A)-1))
```

**Column F**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!G:G,COUNTA('SESSION LOG'!A:A)-1))
```

**Column G**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=2,"",INDEX('SESSION LOG'!J:J,COUNTA('SESSION LOG'!A:A)-1))
```

---

### Fix #10: Row 20 - Third Latest Session
Same pattern, change to `COUNTA('SESSION LOG'!A:A)-2`

**Column B**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!A:A,COUNTA('SESSION LOG'!A:A)-2))
```

**Column C**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!B:B,COUNTA('SESSION LOG'!A:A)-2))
```

**Column D**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!C:C,COUNTA('SESSION LOG'!A:A)-2))
```

**Column E**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!F:F,COUNTA('SESSION LOG'!A:A)-2))
```

**Column F**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!G:G,COUNTA('SESSION LOG'!A:A)-2))
```

**Column G**:
```
=IF(COUNTA('SESSION LOG'!A:A)<=3,"",INDEX('SESSION LOG'!J:J,COUNTA('SESSION LOG'!A:A)-2))
```

---

## WEEKLY REPORT - Cell B24

### Fix #11: Auto-Generated Report Text

**Fixed Formula**:
```
="REFINEMENT PROGRESS - Week of "&TEXT(TODAY(),"MMM DD, YYYY")&CHAR(10)&CHAR(10)&"✅ STORIES REFINED THIS WEEK"&CHAR(10)&"   • Sessions conducted: "&COUNTIFS('SESSION LOG'!C:C,">="&TODAY()-7,'SESSION LOG'!C:C,"<="&TODAY())&CHAR(10)&"   • Stories moved to Ready: "&SUMIFS('SESSION LOG'!F:F,'SESSION LOG'!C:C,">="&TODAY()-7,'SESSION LOG'!C:C,"<="&TODAY())&CHAR(10)&"   • Cumulative progress: "&C11&"/84 ("&ROUND(C13,0)&"%)"&CHAR(10)&CHAR(10)&"📈 VELOCITY METRICS"&CHAR(10)&"   • Current velocity: "&ROUND(F2,1)&" stories/session"&CHAR(10)&"   • Target velocity: 6.5 stories/session"&CHAR(10)&"   • Status: "&E1&CHAR(10)&CHAR(10)&"📅 TIMELINE"&CHAR(10)&"   • Sessions remaining: "&(15-COUNTA('SESSION LOG'!F2:F16))&CHAR(10)&"   • Projected completion: "&F6&CHAR(10)&"   • On track for Sprint 5: "&IF(F6="Sprint 5","YES ✅",IF(F6="Sprint 6","ALMOST ⚠️","NO ❌"))
```

---

## SESSION LOG SHEET - Formula Fixes

### Fix #12: Column G - Cumulative (Starting Row 2)

**Row 2** (Session 1):
```
=SUM($F$2:F2)
```

**Row 3** (Session 2):
```
=SUM($F$2:F3)
```

**Row 4** (Session 3):
```
=SUM($F$2:F4)
```

**Continue pattern for all rows through Row 16 (Session 15)**

---

### Fix #13: Column H - Remaining (Starting Row 2)

**All rows (2-16)**:
```
=84-G2
```
(Adjust row number: G3 for row 3, G4 for row 4, etc.)

---

### Fix #14: Column I - Velocity (Starting Row 2)

**All rows (2-16)**:
```
=F2
```
(Adjust row number: F3 for row 3, F4 for row 4, etc.)

---

### Fix #15: Column J - Status (Starting Row 2)

**All rows (2-16)**:
```
=IF(ISBLANK(I2),"",IF(I2>=6.5,"🟢",IF(I2>=4,"🟡","🔴")))
```
(Adjust row number: I3 for row 3, I4 for row 4, etc.)

---

## BURNDOWN CHART DATA SHEET - Formula Fixes

### Fix #16: Column C - Stories Remaining (Ideal)

**Row 2**:
```
=84-5.6
```

**Row 3**:
```
=84-5.6*2
```

**Row 4**:
```
=84-5.6*3
```

**Pattern**: `=84-5.6*[row number minus 1]`

For all 15 sessions, or simplified formula for Row 2:
```
=84-5.6*(ROW()-1)
```
(Copy down to row 16)

---

### Fix #17: Column D - Stories Remaining (Actual)

**All rows (2-16)**:
```
=INDEX('SESSION LOG'!H:H,ROW())
```
**This pulls the "Remaining" value from SESSION LOG**

---

### Fix #18: Column E - Variance

**All rows (2-16)**:
```
=D2-C2
```
(Adjust row numbers: D3-C3 for row 3, etc.)

---

### Fix #19: Column F - Status

**All rows (2-16)**:
```
=IF(E2>=0,"🟢",IF(E2>=-5,"🟡","🔴"))
```
(Adjust row numbers)

---

## BURNUP CHART DATA SHEET - Formula Fixes

### Fix #20: Column C - Stories Refined (Target)

**Row 2**:
```
=5.6
```

**Row 3**:
```
=5.6*2
```

**Or simplified**:
```
=5.6*(ROW()-1)
```
(Copy down to row 16)

---

### Fix #21: Column D - Stories Refined (Actual)

**All rows (2-16)**:
```
=INDEX('SESSION LOG'!G:G,ROW())
```
**This pulls the "Cumulative" value from SESSION LOG**

---

### Fix #22: Column E - Total Scope

**All rows (2-16)**:
```
=84
```
(Just the number 84)

---

### Fix #23: Column F - Gap

**All rows (2-16)**:
```
=D2-C2
```
(Adjust row numbers)

---

## EPIC PROGRESS SHEET - Formula Fixes

### Fix #24: Column G - % Complete

**Row 2** (SSF-123):
```
=IF(C2=0,0,E2/C2*100)
```

**Copy this formula down for all Epic rows**
(E3/C3*100 for row 3, E4/C4*100 for row 4, etc.)

---

## 🎯 QUICK FIX ORDER

### Start Here (Most Important):

1. **SESSION LOG** first:
   - Fix columns G, H, I, J (Fixes #12-15)
   - These feed all other sheets

2. **DASHBOARD** next:
   - Fix C11, C12, C13 (Fixes #1-3)
   - Fix F2, E1, E2, F6 (Fixes #4-7)
   - These show your main metrics

3. **SESSION SUMMARY**:
   - Fix rows 18-20 (Fixes #8-10)
   - Shows recent progress

4. **BURNDOWN/BURNUP** sheets:
   - Fix formulas (Fixes #16-23)
   - For charts

5. **WEEKLY REPORT**:
   - Fix B24 (Fix #11)
   - Last, as it depends on others

---

## 💡 Tips

1. **Copy formulas exactly** as shown (including quotes and parentheses)
2. **Sheet names are case-sensitive**: Use "SESSION LOG" not "session log"
3. **Test each fix**: Enter a number in SESSION LOG F2 to see if calculations work
4. **Save frequently**: Google Sheets auto-saves but good to verify

---

## ✅ Verification Checklist

After applying all fixes:
- [ ] No #ERROR! messages
- [ ] No #REF! messages
- [ ] No #DIV/0! messages
- [ ] No #VALUE! messages
- [ ] Enter "7" in SESSION LOG cell F2
- [ ] Check DASHBOARD shows: Completed=7, Remaining=77, Progress=8.3%
- [ ] Check velocity shows: 7.0
- [ ] Check status shows: 🟢 On Track

If all checks pass, your tracker is working! 🎉
