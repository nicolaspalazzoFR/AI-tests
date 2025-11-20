# AI Workspaces - Master README

## 👋 Welcome

This workspace contains multiple projects related to fisheries management, project management tools, and AI experimentation.

**Last Updated:** November 20, 2025  
**Primary Project:** SSF Application (Small-Scale Fisheries)

---

## 📁 Workspace Structure

```
/Users/nicolas.palazzo/Documents/AI Workspaces/
│
├─📁 00-WORKSPACE-DOCS/           ← START HERE
│  ├─ README.md                    (This file)
│  ├─ PROJECT_INDEX.md             (All projects catalog)
│  └─ AI_HANDOFF_GUIDE.md          (For switching AIs)
│
├─📁 01-SSF-APPLICATION/           ← MAIN: Fisheries App
│  ├─ docs/PROJECT_CONTEXT.md      (Read this first!)
│  ├─ docs/REGULATORY/             (EU regulations)
│  ├─ docs/SPECIFICATIONS/         (Technical specs)
│  ├─ docs/USER_STORIES/           (Requirements)
│  ├─ docs/PLANNING/               (Sprint planning)
│  ├─ data/MDR-codelists/          (Master data)
│  ├─ mockups/gear-characteristics-pwa/ (Live PWA)
│  ├─ tools/                       (Scripts)
│  └─ archive/                     (Old files)
│
├─📁 02-AI-PM-TOOLKIT/             ← PM Tools & Automation
├─📁 03-OTHER-PROJECTS/            ← Miscellaneous
└─📁 [Legacy Folders]              ← To be cleaned/archived
```

---

## 🚀 Quick Start

### For Anyone (Human or AI):

**1. Understand the workspace:**
```bash
cd 00-WORKSPACE-DOCS
cat PROJECT_INDEX.md
```

**2. Work on SSF Application:**
```bash
cd 01-SSF-APPLICATION
cat docs/PROJECT_CONTEXT.md
```

**3. View live mockups:**
```bash
open mockups/gear-characteristics-pwa/index.html
# OR visit: https://nicolaspalazzofr.github.io/AI-tests/
```

---

## 🤖 For AI Assistants (Cline, Claude, etc.)

**Essential Reading Order:**
1. `00-WORKSPACE-DOCS/AI_HANDOFF_GUIDE.md` (Context & current state)
2. `01-SSF-APPLICATION/docs/PROJECT_CONTEXT.md` (SSF overview)
3. `01-SSF-APPLICATION/docs/WIREFRAMES_PROJECT_LOG.md` (Recent work)

**Key Files:**
- Regulations: `01-SSF-APPLICATION/docs/REGULATORY/`
- Data: `01-SSF-APPLICATION/data/MDR-codelists/`
- Live Code: `01-SSF-APPLICATION/mockups/gear-characteristics-pwa/`

---

## 📋 Active Projects

### 01-SSF-APPLICATION ⭐ (Primary)
**Status:** Active Development  
**Phase:** Mockups & Planning  
**Last Work:** Gear characteristics PWA (Nov 19-20, 2025)  
**Next:** Backend development, FMC integration

### 02-AI-PM-TOOLKIT
**Status:** Reference/Tools  
**Purpose:** Project management automation  
**Use:** Supporting SSF development

### 03-OTHER-PROJECTS
**Status:** Mixed  
**Contains:** Unrelated projects, experiments

---

## 🔗 Important Links

- **GitHub:** https://github.com/nicolaspalazzoFR/AI-tests
- **Live PWA:** https://nicolaspalazzofr.github.io/AI-tests/
- **JIRA:** (If applicable)

---

## ⚠️ Known Issues

### Current State:
- ✅ New organized folders created (`00-*`, `01-*`)
- ⏳ Files being copied to new structure
- ⏳ Legacy folders still present (to be archived)
- ⏳ Some duplication during transition

### To Clean:
- Old "MDR Data for SSF App" folder (after verification)
- Old "SSF DOCS" folder (after migration)
- Root-level PWA files (keep only for GitHub Pages)

---

## 📝 Workspace Guidelines

### File Organization:
- **Use numbered prefixes** (00-, 01-, 02-) for main folders
- **Group by project** - Keep related files together
- **Document everything** - README in every major folder
- **Archive old work** - Don't delete, move to archive/

### Naming Conventions:
- **UPPERCASE_WITH_UNDERSCORES.md** - Documentation
- **lowercase-with-dashes/** - Folders
- **camelCase.js** - JavaScript files
- **snake_case.py** - Python files

### Git Practices:
- **Commit often** - Small, focused commits
- **Descriptive messages** - Explain what and why
- **Push regularly** - Keep remote up to date

---

## 🆘 Need Help?

### Finding Something:
1. Check `PROJECT_INDEX.md` - Catalog of all projects
2. Search by topic in organized folders
3. Check archive folders for old work

### Starting New Work:
1. Read relevant `PROJECT_CONTEXT.md`
2. Review recent git commits
3. Check documentation in `docs/`

### For AI Assistants:
1. Read `AI_HANDOFF_GUIDE.md` first
2. Review project context
3. Check git status for uncommitted work

---

**Maintained by:** Nicolas Palazzo  
**Workspace Created:** 2025  
**Last Reorganization:** November 20, 2025
