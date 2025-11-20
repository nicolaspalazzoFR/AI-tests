# AI Handoff Guide

## 🤖 For the Next AI Assistant

This document provides essential context for any AI (Claude Code, Cline, ChatGPT, etc.) taking over this workspace.

**Created:** November 20, 2025  
**Last AI:** Cline (Claude 3.5 Sonnet via Amazon Bedrock)  
**Next AI:** Your turn!

---

## ⚡ TL;DR - Essential Context

**Working on:** SSF (Small-Scale Fisheries) Application for EU Commission  
**Current Focus:** Gear characteristics data entry forms  
**Latest Achievement:** Interactive PWA with 64 gear types deployed  
**Technology:** PWA (HTML/CSS/JS), Python data generation, GitHub Pages  
**Repository:** https://github.com/nicolaspalazzoFR/AI-tests

---

## 📍 Start Here - Read These 3 Files First

1. **`00-WORKSPACE-DOCS/README.md`** - Workspace overview
2. **`01-SSF-APPLICATION/docs/PROJECT_CONTEXT.md`** - SSF project details
3. **`01-SSF-APPLICATION/docs/WIREFRAMES_PROJECT_LOG.md`** - Recent work history

**Time to get context:** ~10 minutes reading

---

## 🎯 Current Project State

### What's Done ✅

**Gear Characteristics Wireframes (Nov 19-20, 2025):**
- Interactive PWA with autocomplete search
- All 64 fishing gear types from MDR IGv3
- Regulatory-compliant labels from ANNEX XVI
- Gear-specific field descriptions
- Deployed to: https://nicolaspalazzofr.github.io/AI-tests/
- **Live and working!**

### What's Next ⏳

**Immediate:**
1. Complete workspace reorganization
2. Backend API architecture
3. FMC integration planning

**Short Term:**
1. Electronic logbook forms
2. Vessel tracking UI
3. Landing declaration screens

**Medium Term:**
1. Full FMC integration
2. Offline sync
3. Multi-language support

---

## 📂 Where Everything Is

### SSF Application (Main Project)
```
01-SSF-APPLICATION/
├─ docs/
│  ├─ PROJECT_CONTEXT.md        ← Read this!
│  ├─ WIREFRAMES_PROJECT_LOG.md ← Recent work
│  ├─ REGULATORY/                ← EU laws
│  ├─ SPECIFICATIONS/            ← Technical specs
│  ├─ USER_STORIES/              ← Requirements
│  └─ PLANNING/                  ← Sprint plans
│
├─ data/
│  └─ MDR-codelists/             ← Master data (64 gear types)
│
├─ mockups/
│  └─ gear-characteristics-pwa/  ← Interactive PWA ⭐
│
└─ tools/
   └─ generate_gear_data.py      ← Data generator
```

### Key Files to Understand:

| File | Purpose | Why Important |
|------|---------|---------------|
| `MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx` | Defines mandatory/optional fields per gear | Core business rules |
| `Annexes_Commission Implementing Regulation_control_FINAL.docx` | ANNEX XVI - gear descriptions | Regulatory labels |
| `gear-data.js` | 4,140 lines - all 64 gear types | Generated from MDR |
| `SSF_Law_18_09_25.pdf` | EU Regulation 2023/2842 | Legal requirements |

---

## 🛠️ Technical Context

### Technologies Used:
- **PWA:** Vanilla HTML/CSS/JavaScript (no frameworks)
- **Data Processing:** Python 3.9+ with pandas, openpyxl
- **Version Control:** Git + GitHub
- **Deployment:** GitHub Pages (automatic from main branch)

### Code Architecture:
- **gear-data.js** - Auto-generated from MDR Excel files
- **app.js** - Dynamic form rendering based on gear selection
- **styles.css** - Mobile-first responsive design
- **generate_gear_data.py** - Regeneration script

### Why These Choices:
- **No frameworks** - Simpler, faster, no build process
- **PWA** - Works offline, installable, mobile-optimized
- **Python** - Easy data processing from Excel
- **GitHub Pages** - Free hosting, easy deployment

---

## 💡 Important Context & Decisions

### Recent Decision History:

**1. Balsamiq → PWA Pivot (Nov 19)**
- **Attempted:** 68 .bmml wireframes + .bmpr project file
- **Issue:** .bmpr file format corruption in Balsamiq
- **Solution:** Built interactive PWA instead
- **Result:** Better outcome - interactive, no software needed

**2. Dropdown → Autocomplete (Nov 19)**
- **Original:** Dropdown with 64 gear types
- **Client request:** Autocomplete search
- **Implementation:** Real-time filtering by code or name
- **Result:** Much better UX

**3. Generic → Regulatory Labels (Nov 20)**
- **Original:** "Gear Dimension - Length/Width (GM)"
- **Requirement:** ANNEX XVI specific descriptions
- **Solution:** Gear-specific label mapping
- **Result:** "Overall length of lines (GM)" for longlines

### Client Preferences:
- ⚡ Speed over perfection
- 📱 Mobile-first always
- 📊 Regulatory compliance critical
- 🎯 Practical solutions preferred

---

## 🔄 For Claude Code Specifically

### Context You'll Have:
- ✅ All workspace files
- ✅ Git history with commit messages
- ✅ Documentation files
- ✅ Technical artifacts
- ✅ This handoff guide

### Context You WON'T Have:
- ❌ Previous conversation with Cline (~150 exchanges)
- ❌ Real-time client feedback during development
- ❌ Implicit preferences learned through interaction
- ❌ Detailed rationale for some micro-decisions

### How to Compensate:
1. **Read git commit messages** - They explain key decisions
2. **Check WIREFRAMES_PROJECT_LOG.md** - Detailed work history
3. **Review code comments** - Inline documentation
4. **Ask user** - When uncertain about preferences

---

## 📊 Data Flow Understanding

### How Gear Data Works:

```
1. MDR Excel Files (EU Official Data)
   └─> MDR_GEAR_CHARACT_BY_GEAR_TYPE-IGv3-v2025-11-04.xlsx

2. Python Script Reads Excel
   └─> generate_gear_data.py

3. Generates JavaScript Data Object
   └─> gear-data.js (4,140 lines)

4. PWA Reads JavaScript
   └─> app.js dynamically renders forms

5. User Interacts
   └─> Searches, selects gear, fills form
```

**Key Point:** gear-data.js is GENERATED, not hand-written. Always regenerate if MDR data changes!

---

## ⚠️ Current Known Issues

### During Transition:
1. **File Duplication** - PWA exists in root AND nested folders
   - Root: For GitHub Pages deployment
   - Nested: Source of truth
   - **Action:** Keep both synchronized

2. **Legacy Folders** - Old structure still present
   - Not deleted yet (being reorganized)
   - Some files duplicated during copy
   - **Action:** Will clean after verification

3. **Incomplete Reorganization** - Work in progress
   - New folders created
   - Files copied, not moved yet
   - **Action:** Complete migration, then delete old folders

---

## 🎓 Domain Knowledge Required

### Fisheries Concepts:
- **Gear types** - Different fishing methods (trawls, nets, lines, traps)
- **Characteristics** - Dimensions (length, height, mesh size, etc.)
- **MDR** - Master Data Registry (EU official code lists)
- **FMC** - Fisheries Monitoring Centre (24/7 vessel tracking)
- **Mandatory/Optional** - Regulatory requirements vary by gear type

### Regulatory Framework:
- **EU Regulation 2023/2842** - Main fisheries control law
- **Effective:** January 10, 2026
- **ANNEX XVI** - Gear characteristics requirements
- **IGv3** - Implementation Guidance version 3

You don't need to be a fishing expert - the data files contain everything!

---

## 🚀 How to Continue Work

### If User Says: "Continue the SSF work"

**Step 1:** Read context (10 min)
```bash
cd 01-SSF-APPLICATION/docs
cat PROJECT_CONTEXT.md
cat WIREFRAMES_PROJECT_LOG.md
```

**Step 2:** Check current state
```bash
git status
git log --oneline -10
```

**Step 3:** Ask clarifying questions
- "Which part of SSF should I focus on?"
- "Do you want me to continue the reorganization?"
- "Should I start on backend development?"

### If User Says: "Build something new"

**Step 1:** Understand requirements
**Step 2:** Check if related to existing projects
**Step 3:** Follow existing patterns (PWA, Python scripts, etc.)

---

## 💾 Git Workflow Context

### Repository State:
- **Remote:** GitHub (nicolaspalazzoFR/AI-tests)
- **Branch:** main
- **GitHub Pages:** Enabled (deploys from root)
- **Latest commits:** PWA with regulatory labels

### Important Git Notes:
1. **Root PWA files** must stay for GitHub Pages
2. **Always pull before push** (might have remote changes)
3. **Descriptive commit messages** used throughout
4. **Small commits preferred** over large batches

---

## 📝 Communication Style

### With User (Nicolas):
- Direct, technical communication
- Prefers quick solutions over lengthy discussions
- Values regulatory compliance
- Appreciates clear explanations
- Time-sensitive work

### Documentation Style:
- Use emojis for visual scanning
- Clear sections with headers
- Technical but accessible
- Include examples
- Link to relevant files

---

## ✅ Quality Standards

### For This Project:
- ✅ Regulatory compliance is NON-NEGOTIABLE
- ✅ Mobile-first design required
- ✅ All data from official sources (MDR)
- ✅ Field codes visible for reference
- ✅ Professional UI/UX expected
- ✅ Works offline (PWA)

### Code Quality:
- Clean, readable code
- Comments for complex logic
- Reusable functions
- Self-documenting where possible

---

## 🎁 Quick Wins for You

### To Gain Trust Fast:
1. **Read this guide thoroughly** (~15 min)
2. **Test the live PWA** - See what was built
3. **Review recent git commits** - Understand decisions
4. **Ask clarifying questions** - Don't assume

### To Add Value Immediately:
1. Complete workspace reorganization (if needed)
2. Improve documentation (always appreciated)
3. Fix any bugs in PWA
4. Plan next development phase

---

## 🆘 When Stuck

### Resources:
1. **Check PROJECT_INDEX.md** - Find related files
2. **Search git history** - Previous solutions
3. **Review MDR Excel files** - Official source
4. **Read regulatory PDFs** - Legal requirements
5. **Ask user** - They know the business context

### Common Pitfalls:
- ❌ Don't assume you understand fisheries domain
- ❌ Don't skip reading regulatory docs
- ❌ Don't modify MDR data (it's official!)
- ❌ Don't break GitHub Pages deployment
- ✅ DO ask when uncertain
- ✅ DO test before committing
- ✅ DO follow established patterns

---

## 📅 Timeline Context

### Recent History:
- **Nov 19 AM:** MDR analysis started
- **Nov 19 PM:** Balsamiq wireframes attempted
- **Nov 19 PM:** Pivot to PWA solution
- **Nov 19 PM:** PWA deployed to GitHub
- **Nov 20 PM:** Labels updated with ANNEX XVI
- **Nov 20 PM:** Workspace reorganization started

### Work Pace:
- Fast iterations preferred
- Pragmatic over perfect
- Client has tight deadlines
- Regulatory deadline: Jan 10, 2026

---

**Good luck! You have all the context you need. The work is well-documented. Trust the files, ask questions when needed, and build great things! 🚀**

---

**Questions? Start with:**
- "I've read the handoff guide. Should I continue [specific task]?"
- "I see the SSF project context. What's the priority?"
- "The PWA is working. What should we build next?"
