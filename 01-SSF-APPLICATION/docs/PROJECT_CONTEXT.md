# SSF Application - Project Context

## 📋 Project Overview

**Project Name:** Small-Scale Fisheries (SSF) Application  
**Client:** DG MARE / European Commission  
**Purpose:** Digital platform for EU fisheries compliance, monitoring, and reporting  
**Regulation:** EU Regulation 2023/2842 (Fisheries Control)  
**Effective Date:** January 10, 2026

---

## 🎯 Project Objectives

### Primary Goals:
1. **Compliance Tool** - Help fishers comply with EU fisheries regulations
2. **Data Collection** - Capture fishing activities, catches, gear characteristics
3. **FMC Integration** - Connect with Fisheries Monitoring Centres
4. **Traceability** - Track fishery products from catch to first sale
5. **Reporting** - Automate mandatory reporting requirements

### Target Users:
- Small-scale fishers (vessels <12m)
- Fishing vessel masters
- Vessel owners/operators
- National fisheries authorities
- FMCs (Fisheries Monitoring Centres)

---

## 📊 Current Status (November 2025)

### ✅ Completed Work

**1. Gear Characteristics Wireframes/Mockups (Nov 19, 2025)**
- Interactive PWA with all 64 gear types
- Autocomplete search functionality
- Regulatory-compliant labels from ANNEX XVI
- Deployed to GitHub Pages
- **Location:** `01-SSF-APPLICATION/mockups/gear-characteristics-pwa/`
- **Live URL:** https://nicolaspalazzofr.github.io/AI-tests/
- **Documentation:** `docs/WIREFRAMES_PROJECT_LOG.md`

**2. User Stories Generated**
- 9 user stories for gear registration
- Backend and mobile specifications
- **Location:** `docs/USER_STORIES/`

**3. Planning & Tracking Tools**
- Refinement trackers
- Sprint planning guides
- Jira integration workflows
- **Location:** `docs/PLANNING/`

### ⏳ Pending/In Progress

- Backend API development
- FMC integration implementation
- Vessel tracking features  
- Electronic logbook system
- Landing declarations
- Sales notes

---

## 📁 Project Structure

```
01-SSF-APPLICATION/
├─ docs/
│  ├─ PROJECT_CONTEXT.md (this file)
│  ├─ REGULATORY/
│  │  ├─ SSF_Law_18_09_25.pdf
│  │  └─ Annexes_*.docx
│  ├─ SPECIFICATIONS/
│  │  ├─ GEAR_CHARACTERISTICS_BUSINESS_RULES.md
│  │  ├─ GEAR_REGISTRATION_DATA_MODEL.md
│  │  └─ (all SSF DOCS content)
│  ├─ USER_STORIES/
│  │  └─ SSF-14X series
│  └─ PLANNING/
│     └─ Critical context files
├─ data/
│  └─ MDR-codelists/ (Master Data Registry)
├─ mockups/
│  └─ gear-characteristics-pwa/ (Interactive PWA)
├─ tools/
│  └─ (Python scripts, generators)
└─ archive/
   └─ (Deprecated files)
```

---

## 🔑 Key Concepts

### MDR (Master Data Registry)
- **Code lists** defining fishing gear types, species, areas, etc.
- **IGv3** - Implementation Guidance version 3
- **Effective:** January 10, 2026
- **Source:** EU Commission

### Gear Characteristics
- **64 gear types** covered (trawls, gillnets, longlines, etc.)
- **19 field types** (GM, HE, ME, MS, HS, DA, GD, etc.)
- **Mandatory vs Optional** - Varies by gear type
- **ANNEX XVI** - Defines specific requirements per gear

### FMC (Fisheries Monitoring Centre)
- **Purpose:** Monitor fishing vessels 24/7
- **Data:** Vessel position, fishing activities, catches
- **Requirements:** Real-time tracking, automatic alerts

---

## 🛠️ Technical Stack

### Frontend
- **PWA** - Progressive Web App (HTML/CSS/JavaScript)
- **Mobile-first** design (iPhone X viewport)
- **Offline-capable** - Service worker caching
- **Responsive** - Touch-optimized

### Data Processing
- **Python** - Data generation scripts
- **pandas** - Excel file processing
- **openpyxl** - Excel reading

### Deployment
- **GitHub** - https://github.com/nicolaspalazzoFR/AI-tests
- **GitHub Pages** - Live deployment
- **Git** - Version control

### Backend (Planned)
- To be determined
- API integration with FMC
- Database for catches, gear, vessels

---

## 📜 Regulatory Framework

### Primary Regulation
**EU Regulation 2023/2842**
- Amends Regulation (EC) No 1224/2009
- Establishes fisheries control system
- Defines data requirements
- **Location:** `docs/REGULATORY/SSF_Law_18_09_25.pdf`

### Key Requirements
1. **Vessel Monitoring** - Position data transmission
2. **Electronic Logbooks** - Digital catch recording
3. **Gear Registration** - Characteristics documentation
4. **Prior Notifications** - Before landing
5. **Weighing** - Mandatory at landing
6. **Traceability** - From catch to first sale

---

## 👥 Stakeholders

### Primary
- **DG MARE** - European Commission Fisheries Directorate
- **Member States** - National fisheries authorities
- **Fishers** - End users of the application

### Technical
- **FMCs** - Fisheries Monitoring Centres
- **EFCA** - European Fisheries Control Agency
- **National Control Authorities**

---

## 🔗 Related Projects

### Same Workspace:
- **AI PM Toolkit** - Project management tools
- **Shall We Dance** - Unrelated project (can be moved)
- **PWA Journey Presentation** - Presentation tool

### External:
- **n8n workflows** - Automation workflows
- **JIRA** - Project tracking

---

## 📈 Recent Work History

### November 19-20, 2025
- Analyzed MDR code lists
- Created 68 Balsamiq wireframes (had format issues)
- Pivoted to interactive PWA solution
- Implemented autocomplete search
- Updated labels with ANNEX XVI descriptions
- Deployed to GitHub Pages
- Documented in WIREFRAMES_PROJECT_LOG.md

---

## 🚀 Next Steps

### Immediate Priorities:
1. Complete workspace reorganization
2. Create AI handoff documentation
3. Define backend architecture
4. Plan FMC integration approach

### Medium Term:
1. Implement electronic logbook
2. Build vessel tracking features
3. Develop landing declaration forms
4. Create sales notes functionality

### Long Term:
1. Full FMC integration
2. Multi-language support
3. Offline synchronization
4. Advanced analytics

---

## 📞 Key Contacts

*(To be filled with actual contacts)*

- Project Manager: 
- Technical Lead:
- DG MARE Contact:
- FMC Representative:

---

## 🔐 Important URLs

- **GitHub Repo:** https://github.com/nicolaspalazzoFR/AI-tests
- **Live PWA:** https://nicolaspalazzofr.github.io/AI-tests/
- **MDR Website:** (EU Commission Fisheries - Master Data Register)

---

**Last Updated:** November 20, 2025  
**Status:** Active Development  
**Phase:** Mockups & Planning
