#!/usr/bin/env python3
"""
Script to add time estimates to all actions in the timeline HTML
"""

import re

# Time estimates mapping based on action patterns
time_estimates = {
    # Documentation actions
    "Created PI_01_ESTIMATION_CHALLENGE.md": "~30min",
    "Created DESCOPING_STRATEGY_V2.md": "~45min",
    "Created BACKLOG_ROADMAP_ANALYSIS.md": "~30min",
    "Created PI_02_SPRINT_SUMMARY.md": "~20min",
    "Created PI_02_SPRINT_07.md": "~20min",
    "Created PI_02_SPRINT_08.md": "~20min",
    "Created PI_02_SPRINT_09_to_12.md": "~25min",
    "Created README.md for PWA": "~15min",
    "Documented Docker filesystem workaround": "~20min",
    "Created Backlog SSF ALT - V003 - Sprints - Enhanced.csv": "~20min",
    "Created JIRA_WORKFLOW_SETUP_GUIDE.md": "~45min",
    "Created MDR README.md (250+ lines)": "~1h",
    "Wrote vessel selection AC (10 scenarios)": "~30min",
    "Created error handling acceptance criteria": "~20min",
    "Created JIRA_FORMATTING_GUIDE.md": "~30min",
    "Updated PROJECT_CONTEXT.md (JIRA standards)": "~15min",
    "Updated USER_STORY_GUIDE.md (two-format approach)": "~20min",
    "Wrote SSF-141 AC (8 scenarios)": "~25min",
    "Created SSF-141_Acceptance_Criteria.md": "~15min",
    "Created SSF-147_Register_New_Gear_Backend.md": "~20min",
    "Created SSF-142_Register_New_Gear_Form_Submission_Mobile.md": "~20min",
    "Created SSF-144_Vessel_Gear_Screen_Gear_List_Mobile.md": "~20min",
    "Created SSF-148_List_Vessel_Gear_New_Gear_Backend.md": "~20min",
    "Created SSF-149_List_Vessel_Gear_Retrieval_Backend.md": "~20min",
    "Created SSF-141_Register_New_Gear_Init_Creation_Form_Mobile.md": "~20min",
    "Created sprint-report-workflow.json": "~10min",
    "Created user-story-generator-workflow.json": "~15min",
    
    # Development actions
    "Built interactive Sprint Management PWA": "~3h",
    "Created index.html": "~30min",
    "Created styles.css (Classic Grey theme)": "~1h",
    "Created data.js (24 stories embedded)": "~20min",
    "Created app.js (400+ lines)": "~1h",
    "Created export.js": "~30min",
    "Created manifest.json": "~10min",
    "Created sw.js": "~20min",
    "Implemented responsive grid layout": "~30min",
    "Added expandable card UX pattern": "~45min",
    "Fixed PWA presentation responsive design": "~20min",
    "Added comprehensive mobile CSS breakpoints": "~25min",
    "Enabled scrolling (min-height vs height)": "~10min",
    "Created n8n automation templates (JavaScript)": "~45min",
    'Created "MDR Data for SSF App" folder': "~5min",
    
    # Setup actions
    "Installed n8n Community Edition": "~15min",
    "Started n8n at localhost:5678": "~5min",
    "Created n8n owner account": "~5min",
    "Fixed Jira domain format (added https://)": "~10min",
    "Set up Filesystem MCP server": "~30min",
    "Added MCP server to Cline settings": "~15min",
    "Fixed Miro OAuth scopes (boards:write)": "~20min",
    "Set up Jira Cloud test account": "~15min",
    "Generated Jira Cloud API token": "~10min",
    "Downloaded 19 MDR files (~10 MB)": "~20min",
    "Connected n8n to EC Jira Server": "~30min",
    "Fixed Docker file permission issue": "~1h",
    "Troubleshot SSF Jira Server integration": "~45min",
    
    # Integration actions
    "Built Sprint Report workflow (foundation)": "~45min",
    "Completed Sprint Report workflow via n8n API": "~30min",
    "Generated sprint-report-2025-11-04-1821.md": "~2min",
    "Generated sprint-report-2025-11-04-1838.md": "~2min",
    "Built Jira → Miro integration workflow": "~1h",
    "Created 101 Miro sticky notes from Jira": "~5min",
    "Converted Miro sticky notes to cards": "~30min",
    "Fixed Jira browse URL construction": "~15min",
    "Debugged User Story Generator workflow": "~45min",
    "Redesigned workflow (HTTP → AI Agent)": "~1h",
    "Generated 3 stories from SSF-93 epic": "~10min",
    "Connected workflow to Jira Cloud": "~30min",
    "Created 3 tasks in Jira Cloud automatically": "~5min",
    
    # Testing actions
    "Tested Sprint Report workflow (101 stories)": "~15min",
    "Re-tested workflow (validation run)": "~10min",
}

def add_time_to_line(line, action_text, time_estimate):
    """Add time estimate to a tool line if not already present"""
    if "• Time:" not in line and action_text in time_estimates:
        # Find the closing </div> and insert time before it
        line = line.replace("</div>", f" • Time: {time_estimate}</div>")
    return line

def process_html_file(filepath):
    """Read HTML file, add time estimates, and write back"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process each action to add time estimates
    for action_text, time_estimate in time_estimates.items():
        # Find the pattern: action line followed by tool line
        pattern = rf'(<div class="action">{re.escape(action_text)}</div>\s*<div class="tool">.*?)(</div>)'
        
        def replacer(match):
            full_match = match.group(0)
            if "• Time:" not in full_match:
                return match.group(1) + f" • Time: {time_estimate}" + match.group(2)
            return full_match
        
        content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Time estimates added to {filepath}")
    print(f"   Total estimates added: {len(time_estimates)}")

if __name__ == "__main__":
    process_html_file("index.html")
    print("\n🎉 All time estimates have been added!")
