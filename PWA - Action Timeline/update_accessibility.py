#!/usr/bin/env python3
"""
Script to:
1. Calculate total time per category
2. Update HTML with time totals
3. Update CSS with RGAA-compliant pastel colors
"""

import re

def parse_time(time_str):
    """Convert time string like '~2h', '~30min' to hours (float)"""
    if not time_str or 'Time:' not in time_str:
        return 0
    
    time_match = re.search(r'~(\d+)h', time_str)
    if time_match:
        return float(time_match.group(1))
    
    time_match = re.search(r'~(\d+)min', time_str)
    if time_match:
        return float(time_match.group(1)) / 60
    
    return 0

def format_hours(hours):
    """Format hours as '~14h 45min' or '~10h' or '~25min'"""
    if hours >= 1:
        h = int(hours)
        m = int((hours - h) * 60)
        if m > 0:
            return f"~{h}h {m}min"
        return f"~{h}h"
    else:
        m = int(hours * 60)
        return f"~{m}min"

# Calculate totals by parsing the HTML
categories = {
    'planning': [],
    'documentation': [],
    'development': [],
    'setup': [],
    'integration': [],
    'testing': []
}

# Read HTML and extract times
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all time estimates per category
for category in categories.keys():
    pattern = rf'data-category="{category}"[^>]*>.*?Time: ([^<]+)</div>'
    matches = re.findall(pattern, content, re.DOTALL)
    for match in matches:
        time = parse_time(f"Time: {match}")
        if time > 0:
            categories[category].append(time)

# Calculate totals
totals = {}
for category, times in categories.items():
    total = sum(times)
    totals[category] = format_hours(total)
    print(f"{category}: {len(times)} actions, {format_hours(total)} total")

# Update HTML with totals
html_updates = {
    'Planning & Analysis <span class="count">(12)</span>': f'Planning & Analysis <span class="count">(12)</span> <span class="time-total">• {totals["planning"]}</span>',
    'Documentation <span class="count">(27)</span>': f'Documentation <span class="count">(27)</span> <span class="time-total">• {totals["documentation"]}</span>',
    'Development <span class="count">(15)</span>': f'Development <span class="count">(15)</span> <span class="time-total">• {totals["development"]}</span>',
    'Setup & Configuration <span class="count">(13)</span>': f'Setup & Configuration <span class="count">(13)</span> <span class="time-total">• {totals["setup"]}</span>',
    'Integration & Automation <span class="count">(15)</span>': f'Integration & Automation <span class="count">(15)</span> <span class="time-total">• {totals["integration"]}</span>',
    'Testing & Validation <span class="count">(2)</span>': f'Testing & Validation <span class="count">(2)</span> <span class="time-total">• {totals["testing"]}</span>'
}

for old, new in html_updates.items():
    content = content.replace(old, new)

# Write updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ HTML updated with time totals!")

# Now update CSS with RGAA-compliant pastel colors
css_updates = {
    # Remove gradient backgrounds, add solid colors
    '.category-section[data-category="planning"] .category-header': '''background: #E8D5F2;
    color: #2C1654;''',
    
    '.category-section[data-category="documentation"] .category-header': '''background: #FFE5EC;
    color: #6B1C3A;''',
    
    '.category-section[data-category="development"] .category-header': '''background: #D5E8F7;
    color: #1B4965;''',
    
    '.category-section[data-category="setup"] .category-header': '''background: #D4F1D9;
    color: #1E5128;''',
    
    '.category-section[data-category="integration"] .category-header': '''background: #FFE8CC;
    color: #7C4D0A;''',
    
    '.category-section[data-category="testing"] .category-header': '''background: #D5F5F6;
    color: #0D4B4F;'''
}

# Read CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace gradient styles with solid colors
for selector, styles in css_updates.items():
    # Remove old gradient rule if exists
    pattern = rf'{re.escape(selector)} \{{[^}}]+\}}'
    if re.search(pattern, css_content):
        # Replace existing rule
        css_content = re.sub(pattern, f'{selector} {{\n    {styles}\n}}', css_content)
    else:
        # Add new rule at the end of category-specific section
        insert_pos = css_content.find('/* Mobile Responsive for Categories */')
        if insert_pos > 0:
            css_content = css_content[:insert_pos] + f'\n{selector} {{\n    {styles}\n}}\n\n' + css_content[insert_pos:]

# Also update default category-header to not use gradient
css_content = css_content.replace(
    'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
    'background: #E8D5F2;'
).replace(
    'color: white;',
    'color: #2C1654;',
    1  # Only first occurrence in category-header
)

# Write updated CSS
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ CSS updated with RGAA-compliant pastel colors!")
print("\n🎨 Color Palette (WCAG AA compliant):")
print("  Planning: Lavender #E8D5F2 + Dark Purple #2C1654")
print("  Documentation: Soft Pink #FFE5EC + Dark Pink #6B1C3A")
print("  Development: Sky Blue #D5E8F7 + Navy #1B4965")
print("  Setup: Mint Green #D4F1D9 + Dark Green #1E5128")
print("  Integration: Peach #FFE8CC + Brown #7C4D0A")
print("  Testing: Aqua #D5F5F6 + Teal #0D4B4F")
print("\n🎉 All accessibility improvements completed!")
