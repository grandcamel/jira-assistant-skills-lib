"""
Shared constants for JIRA Assistant Skills.

Single source of truth for field IDs and other constants used across modules.
"""

# Default Agile field IDs (common defaults, may vary per JIRA instance)
DEFAULT_AGILE_FIELDS = {
    "epic_link": "customfield_10014",
    "story_points": "customfield_10016",
    "epic_name": "customfield_10011",
    "epic_color": "customfield_10012",
    "sprint": "customfield_10020",
}

# Convenience aliases for commonly used fields
EPIC_LINK_FIELD = DEFAULT_AGILE_FIELDS["epic_link"]
STORY_POINTS_FIELD = DEFAULT_AGILE_FIELDS["story_points"]
EPIC_NAME_FIELD = DEFAULT_AGILE_FIELDS["epic_name"]
EPIC_COLOR_FIELD = DEFAULT_AGILE_FIELDS["epic_color"]
SPRINT_FIELD = DEFAULT_AGILE_FIELDS["sprint"]

# Mock/Default Status Constants
STATUS_TODO = "To Do"
STATUS_IN_PROGRESS = "In Progress"
STATUS_DONE = "Done"

STATUS_IDS = {
    STATUS_TODO: "10000",
    STATUS_IN_PROGRESS: "10001",
    STATUS_DONE: "10002",
}

# Mock/Default Transition Constants
TRANSITIONS = {
    STATUS_TODO: {"id": "11", "name": STATUS_TODO},
    STATUS_IN_PROGRESS: {"id": "21", "name": STATUS_IN_PROGRESS},
    STATUS_DONE: {"id": "31", "name": STATUS_DONE},
}

# Priority Constants
PRIORITY_HIGHEST = "Highest"
PRIORITY_HIGH = "High"
PRIORITY_MEDIUM = "Medium"
PRIORITY_LOW = "Low"
PRIORITY_LOWEST = "Lowest"

PRIORITY_IDS = {
    PRIORITY_HIGHEST: "1",
    PRIORITY_HIGH: "2",
    PRIORITY_MEDIUM: "3",
    PRIORITY_LOW: "4",
    PRIORITY_LOWEST: "5",
}
