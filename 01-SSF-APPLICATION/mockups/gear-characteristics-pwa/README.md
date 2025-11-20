# Gear Characteristics Interactive Mockups (PWA)

## 🚀 Quick Start

Simply open `index.html` in your browser to view the interactive mockups!

### Option 1: Double-click
- Double-click `index.html`
- Opens in your default browser

### Option 2: Command line
```bash
open index.html  # macOS
```

### Option 3: Local server (recommended for full PWA experience)
```bash
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

---

## ✨ Features

### ✅ Interactive Form Viewer
- **Dropdown selector** with all 64 gear types
- **Dynamic forms** that adapt to each gear type
- **Real input fields** you can interact with
- **Proper field types**: numeric inputs, dropdowns, text areas
- **Visual distinction**: Mandatory vs Optional fields

### ✅ Mobile-Optimized
- Responsive design for iPhone/Android
- Touch-friendly controls (48px minimum)
- Proper mobile input keyboards
- Smooth animations and transitions

### ✅ Data-Driven
- All data generated from MDR Excel file
- 64 gear types with correct characteristics
- Mandatory/optional rules per gear type
- Proper units displayed (m, mm, pieces, hooks, lines)
- Field codes visible (GM, HE, ME, etc.)

### ✅ PWA Capable
- Works offline after first load
- Installable to home screen
- Fast loading with caching
- Manifest file included

---

## 📁 Files

- `index.html` - Main application
- `styles.css` - Mobile-optimized styling
- `app.js` - Form rendering logic
- `gear-data.js` - All 64 gear type definitions (auto-generated)
- `manifest.json` - PWA manifest
- `sw.js` - Service worker for offline support
- `generate_gear_data.py` - Script to regenerate gear-data.js from MDR Excel

---

## 🎯 How to Use

1. **Open the app** (index.html in browser)
2. **Select a gear type** from the dropdown
3. **View the form** with mandatory and optional fields
4. **Interact with fields** - enter values, select options
5. **Switch gear types** to see different configurations

---

## 📊 What You'll See

### For Each Gear Type:
- **Gear header** with code and name
- **Mandatory fields** section (red title, marked with *)
- **Optional fields** section (gray title)
- **Field labels** with codes: "Overall Length (GM) *"
- **Proper inputs**:
  - Numeric with units: `[____] m`
  - Dropdowns: Mesh Type, Devices, Twine Type
  - Text areas: Gear Description
- **Info note**: Required fields disclaimer
- **Action buttons**: Cancel and Save Gear

### Examples:
- **Simple gear** (DRB - Dredges): 2 mandatory fields
- **Gillnets** (GNS): 4 mandatory (length, height, mesh size, mesh type)
- **Longlines** (LL): 3 mandatory including NEW hook size (2026)
- **Trawls** (OTB): 3 mandatory + optional technical fields

---

## 🔄 Regenerating Data

If MDR Excel file is updated:

```bash
python3 generate_gear_data.py
```

This will regenerate `gear-data.js` with the latest gear characteristics.

---

## 📱 Mobile Testing

### Test on Real Device:
1. Start local server: `python3 -m http.server 8000`
2. Find your IP: `ifconfig | grep inet`
3. On phone, visit: `http://[YOUR_IP]:8000`
4. Test all interactions

### Install as PWA:
1. Open in Chrome/Safari on mobile
2. Tap "Add to Home Screen"
3. App icon appears on home screen
4. Opens like a native app

---

## 💡 Advantages Over Static Wireframes

✅ **Instantly accessible** - No special software needed
✅ **Interactive** - Real form behavior and validation
✅ **Mobile-native** - Actual mobile experience
✅ **Easy sharing** - Just send the folder or URL
✅ **Quick iteration** - Edit HTML/CSS and refresh
✅ **Works offline** - PWA caching
✅ **Installable** - Add to phone home screen

---

## 🎨 Customization

### Change Colors:
Edit `styles.css` - Search for color values:
- Primary blue: `#2563eb`
- Red for mandatory: `#dc2626`
- Gray for optional: `#6b7280`

### Add More Devices/Attachments:
Edit `gear-data.js` - Add to `DEVICES_ATTACHMENTS` array

### Modify Field Descriptions:
Edit `generate_gear_data.py` - Update `FIELD_DESCRIPTIONS`

---

## 📋 Coverage

✅ All 64 gear types from MDR IGv3
✅ Mandatory/optional split per gear type
✅ Field codes visible (GM, HE, ME, HS, etc.)
✅ Full English descriptions
✅ Proper units (m, mm, pieces, hooks, lines)
✅ NEW 2026 field badge (Hook Size)
✅ EU Regulation 2025/2196 compliant
✅ Effective date: January 10, 2026

---

## 🆘 Troubleshooting

### Forms not loading?
- Check browser console (F12) for errors
- Ensure gear-data.js was generated
- Try refreshing the page

### PWA not installing?
- Must use HTTPS or localhost
- Check manifest.json is valid
- Try Chrome/Safari mobile

### Data not matching Excel?
- Regenerate gear-data.js
- Check MDR Excel file path in generate script

---

**Status:** ✅ READY TO USE  
**Format:** Progressive Web App (HTML/CSS/JS)  
**Data Source:** MDR IGv3  
**Compliance:** EU Regulation 2025/2196
