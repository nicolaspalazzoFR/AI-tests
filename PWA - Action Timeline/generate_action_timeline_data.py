#!/usr/bin/env python3
"""
Generate action timeline data from JOURNEY_LOG.md

This script parses the journey log and extracts all individual actions,
creating a JSON file that the Action Timeline PWA can load dynamically.

Usage: python3 generate_action_timeline_data.py
"""

import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

TIME_OF_DAY_ORDER = {
    "Morning": 0,
    "Afternoon": 1,
    "Evening": 2,
    "Full day": 3
}

def parse_journey_log():
    """Parse JOURNEY_LOG.md and extract all actions"""
    
    # Path to journey log
    journey_log_path = Path(__file__).parent.parent / "AI CODING" / "ai-pm-toolkit" / "docs" / "journey" / "JOURNEY_LOG.md"
    
    if not journey_log_path.exists():
        print(f"❌ Journey log not found at: {journey_log_path}")
        return []
    
    with open(journey_log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    actions = []
    
    # Parse sessions (## 📅 Session: Date)
    session_pattern = r'## 📅 Session: (.+?)(?=## 📅 Session:|## 📊 Monthly Summary:|$)'
    sessions = re.finditer(session_pattern, content, re.DOTALL)
    
    for session_match in sessions:
        session_content = session_match.group(0)
        session_title = session_match.group(1).strip()
        
        # Extract date from session title
        date_match = re.search(r'(\w+ \d+, \d{4})', session_title)
        if not date_match:
            continue
        
        date_str = date_match.group(1)
        
        # Parse time of day if present
        time_of_day = "Full day"
        if "Morning" in session_title or "Afternoon" in session_title or "Evening" in session_title:
            if "Morning" in session_title:
                time_of_day = "Morning"
            elif "Afternoon" in session_title:
                time_of_day = "Afternoon"
            elif "Evening" in session_title:
                time_of_day = "Evening"
        
        # Extract actions from "What We Accomplished" section
        # Match until the next major section (### ⏱️, ### 💡, ### 📈, ### 📝, or ---)
        accomplished_section = re.search(
            r'### 🚀 What We Accomplished(.+?)(?=### ⏱️|### 💡|### 📈|### 📝|---\n\n|## 📅|## 📊|$)',
            session_content,
            re.DOTALL
        )
        
        if not accomplished_section:
            continue
        
        accomplished_text = accomplished_section.group(1)
        
        # Extract individual accomplishments (#### Title)
        accomplishment_pattern = r'#### (.+?)(?=####|###|##|$)'
        accomplishments = re.finditer(accomplishment_pattern, accomplished_text, re.DOTALL)
        
        for accomp_match in accomplishments:
            accomp_title = accomp_match.group(1).strip().split('\n')[0]
            accomp_content = accomp_match.group(1)
            
            # Extract deliverables created
            deliverable_patterns = [
                r'\*\*Deliverable(?:s)? Created\*\*:(.+?)(?=\*\*|####|###)',
                r'\*\*Deliverable\*\*:(.+?)(?=\*\*|####|###)',
                r'Created (.+?\.(?:md|json|csv|html|css|js|py))',
                # Match deliverables section with checkmarks: ✅ Action `filename`
                r'✅\s*(?:Refactored|Enhanced|Updated|Created|Fixed|Added)\s+`([A-Z_\-\.a-z0-9]+\.(?:md|json|csv|html|css|js|py|xml|xls|xlsx))`',
                r'✅\s*(?:Refactored|Enhanced|Updated|Created|Fixed|Added)\s+([A-Z_\-\.a-z0-9]+\.(?:md|json|csv|html|css|js|py|xml|xls|xlsx))',
            ]
            
            for pattern in deliverable_patterns:
                deliverables = re.finditer(pattern, accomp_content, re.DOTALL | re.IGNORECASE)
                for deliv_match in deliverables:
                    filename = None
                    action_verb = "Created"
                    match_text = deliv_match.group(0)
                    
                    # Check if pattern captured filename directly in group 1
                    if len(deliv_match.groups()) > 0 and deliv_match.group(1):
                        filename = deliv_match.group(1)
                        # Determine action verb from pattern
                        if "Refactored" in match_text:
                            action_verb = "Refactored"
                        elif "Enhanced" in match_text:
                            action_verb = "Enhanced"
                        elif "Updated" in match_text:
                            action_verb = "Updated"
                    else:
                        # Extract filename from the match text
                        deliv_text = match_text.strip()
                        file_matches = list(re.finditer(r'([A-Z_\-\.a-z0-9]+\.(?:md|json|csv|html|css|js|py|xml|xls|xlsx))', deliv_text, re.IGNORECASE))
                        if file_matches:
                            filename = file_matches[0].group(1)
                            # Determine action verb from context
                            if "Refactored" in deliv_text:
                                action_verb = "Refactored"
                            elif "Enhanced" in deliv_text:
                                action_verb = "Enhanced"
                            elif "Updated" in deliv_text:
                                action_verb = "Updated"
                    
                    if filename:
                        # Determine icon based on file type
                        icon = get_icon_for_action(filename, accomp_title)
                        
                        actions.append({
                            "date": date_str,
                            "time_of_day": time_of_day,
                            "date_iso": format_date(date_str),
                            "icon": icon,
                            "category": determine_category(accomp_title, filename),
                            "action": f"{action_verb} {filename}",
                            "tool": extract_tool_info(accomp_content) if action_verb == "Created" else f"Deliverable: {accomp_title}",
                            "keywords": f"{filename} {accomp_title.lower()} deliverable document file",
                            "duration_minutes": 0
                        })
            
            # Extract major activities
            action_keywords = [
                ("Analyzed", "📊", "analysis"),
                ("Wrote", "✍️", "writing stories"),
                ("Created", "📋", "creation document"),
                ("Built", "💻", "development build"),
                ("Installed", "🔧", "installation setup"),
                ("Set up", "🔧", "setup configuration"),
                ("Connected", "🔌", "integration connection"),
                ("Fixed", "🔧", "fix solution"),
                ("Tested", "🧪", "testing validation"),
                ("Generated", "📊", "generation output"),
                ("Implemented", "⚙️", "implementation feature"),
                ("Added", "➕", "addition feature"),
                ("Updated", "🔄", "update modification"),
                ("Refactored", "🔄", "refactoring improvement"),
                ("Enhanced", "➕", "enhancement improvement"),
                ("Debugged", "🐛", "debugging troubleshooting"),
                ("Troubleshot", "🔍", "troubleshooting diagnosis"),
                ("Downloaded", "📥", "download data"),
                ("Documented", "📋", "documentation guide"),
                ("Mapped", "🗺️", "mapping organization"),
            ]
            
            for verb, icon, keywords in action_keywords:
                if verb in accomp_title:
                    # Extract the main action description
                    action_text = accomp_title
                    
                    actions.append({
                        "date": date_str,
                        "time_of_day": time_of_day,
                        "date_iso": format_date(date_str),
                        "icon": icon,
                        "category": determine_category(accomp_title, ""),
                        "action": action_text,
                        "tool": extract_tool_info(accomp_content),
                        "keywords": f"{keywords} {action_text.lower()}",
                        "duration_minutes": 0
                    })
                    break
    
    return actions


class TimelineHTMLParser(HTMLParser):
    """HTML parser to extract action card details from index.html."""

    def __init__(self):
        super().__init__()
        self.cards = []
        self.current_card = None
        self.current_field = None
        self.card_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "div":
            classes = attrs_dict.get("class", "").split()

            if self.current_card is None and "action-card" in classes:
                self.current_card = {
                    "date": "",
                    "icon": "",
                    "action": "",
                    "tool": "",
                    "category": attrs_dict.get("data-category", "").strip(),
                    "keywords": attrs_dict.get("data-keywords", "").strip(),
                    "date_iso": attrs_dict.get("data-date", "").strip()
                }
                self.card_depth = 1
            elif self.current_card is not None:
                self.card_depth += 1

                if "date" in classes:
                    self.current_field = "date"
                elif "icon" in classes:
                    self.current_field = "icon"
                elif "action" in classes:
                    self.current_field = "action"
                elif "tool" in classes:
                    self.current_field = "tool"

    def handle_data(self, data):
        if self.current_card is not None and self.current_field is not None:
            self.current_card[self.current_field] += data

    def handle_endtag(self, tag):
        if self.current_card is None:
            return

        if tag == "div":
            if self.current_field:
                # Normalize whitespace
                self.current_card[self.current_field] = re.sub(
                    r"\s+",
                    " ",
                    self.current_card[self.current_field]
                ).strip()
                self.current_field = None

            self.card_depth -= 1

            if self.card_depth == 0:
                self.cards.append(self.current_card)
                self.current_card = None


def parse_existing_html():
    """Fallback parser that extracts actions directly from the current index.html."""
    html_path = Path(__file__).parent / "index.html"
    if not html_path.exists():
        print(f"❌ index.html not found at: {html_path}")
        return []

    parser = TimelineHTMLParser()
    parser.feed(html_path.read_text(encoding="utf-8"))

    actions = []
    for card in parser.cards:
        date_human, time_of_day = split_date_and_time(card.get("date", ""))

        actions.append({
            "date": date_human,
            "time_of_day": time_of_day,
            "date_iso": card.get("date_iso", ""),
            "icon": card.get("icon") or guess_icon_from_keywords(
                card.get("keywords", ""),
                card.get("action", "")
            ),
            "category": card.get("category", ""),
            "action": card.get("action", ""),
            "tool": card.get("tool", ""),
            "keywords": card.get("keywords", ""),
            "duration_minutes": parse_time_to_minutes(card.get("tool", ""))
        })

    return actions


def split_date_and_time(date_text):
    if not date_text:
        return "", "Full day"
    parts = [part.strip() for part in date_text.split(" - ", 1)]
    if len(parts) == 2:
        return parts[0], parts[1] or "Full day"
    return date_text.strip(), "Full day"


def guess_icon_from_keywords(keywords, action_title):
    combined = f"{keywords} {action_title}".lower()
    if "docker" in combined:
        return "🐳"
    if "document" in combined or ".md" in combined:
        return "📋"
    if "workflow" in combined or "integration" in combined:
        return "🔄"
    if "testing" in combined or "validate" in combined:
        return "🧪"
    if "analysis" in combined or "planning" in combined:
        return "📊"
    if "setup" in combined or "install" in combined:
        return "🔧"
    return "📁"


def parse_time_to_minutes(text):
    if not text:
        return 0

    # Look for a "~Xh Ymin" or "~Xh" pattern
    hours_match = re.search(r'~\s*(\d+)\s*h', text, re.IGNORECASE)
    minutes_match = re.search(r'~\s*(\d+)\s*min', text, re.IGNORECASE)

    total_minutes = 0

    if hours_match:
        total_minutes += int(hours_match.group(1)) * 60

    # Prefer explicit minutes following hours (e.g. ~1h 30min)
    minutes_after_hours = re.search(r'~\s*\d+\s*h\s*(\d+)\s*min', text, re.IGNORECASE)
    if minutes_after_hours:
        total_minutes += int(minutes_after_hours.group(1))
    elif minutes_match:
        total_minutes += int(minutes_match.group(1))

    return total_minutes

def get_icon_for_action(filename, title):
    """Determine appropriate icon based on file type and context"""
    
    if any(x in filename.lower() for x in ['docker', 'container']):
        return "🐳"
    elif filename.endswith('.md'):
        return "📋"
    elif filename.endswith(('.json', '.xml')):
        return "📄"
    elif filename.endswith(('.html', '.css', '.js')):
        if 'pwa' in title.lower() or 'web' in title.lower():
            return "💻"
        return "📄"
    elif filename.endswith(('.py', '.sh')):
        return "🤖"
    elif filename.endswith(('.csv', '.xls', '.xlsx')):
        return "📊"
    else:
        return "📋"

def extract_tool_info(content):
    """Extract tool information from content"""
    
    tool_patterns = [
        r'\*\*Tool(?:s)? Used\*\*: (.+?)(?:\n|$)',
        r'Tool: (.+?)(?:\n|$)',
    ]
    
    for pattern in tool_patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1).strip()
    
    return "Tool: Claude 3.5 Sonnet"

def determine_category(title, filename):
    """Determine category based on title and filename"""
    title_lower = title.lower()
    filename_lower = filename.lower()
    
    # Development files
    if any(x in filename_lower for x in ['.html', '.css', '.js', '.json', 'manifest', 'sw.js']):
        return "development"
    
    # Documentation files
    if filename_lower.endswith('.md') or 'readme' in filename_lower or 'guide' in filename_lower:
        return "documentation"
    
    # Setup/Configuration
    if any(x in title_lower for x in ['setup', 'install', 'configure', 'docker']):
        return "setup"
    
    # Integration/Automation
    if any(x in title_lower for x in ['workflow', 'integration', 'automation', 'api']):
        return "integration"
    
    # Testing
    if any(x in title_lower for x in ['test', 'validate', 'debug']):
        return "testing"
    
    # Planning/Analysis
    if any(x in title_lower for x in ['plan', 'analyze', 'estimate', 'strategy']):
        return "planning"
    
    # Default to documentation
    return "documentation"

def format_date(date_str):
    """Convert date string to ISO format for sorting"""
    try:
        date_obj = datetime.strptime(date_str, "%B %d, %Y")
        return date_obj.strftime("%Y-%m-%d")
    except:
        return date_str

def main():
    print("🔄 Parsing JOURNEY_LOG.md...")
    
    actions = parse_journey_log()
    
    if not actions:
        print("⚠️ Falling back to index.html content...")
        actions = parse_existing_html()
        if not actions:
            print("❌ No actions found in index.html")
            return
    
    # Sort by date
    actions.sort(key=lambda x: format_date(x['date']))
    
    # Write to JSON file
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    output_json_path = data_dir / "action-timeline-data.json"
    output_js_path = data_dir / "action-timeline-data.js"
    
    payload = {
        "generated": datetime.now().isoformat(),
        "total_actions": len(actions),
        "actions": actions
    }

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    js_payload = (
        "window.ACTION_TIMELINE_DATA = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";"
    )

    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
    
    print(f"✅ Generated {len(actions)} actions")
    print(f"📄 JSON Output: {output_json_path}")
    print(f"📄 JS Output: {output_js_path}")
    print("\n🎉 Action timeline data updated!")
    print("   Refresh the timeline in your browser to see changes.")

if __name__ == "__main__":
    main()
