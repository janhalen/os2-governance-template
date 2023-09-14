import json
import re

# Load the issue body from the GitHub event
with open('event.json') as f:
    data = json.load(f)
    issue_body = data['event']['issue']['body']

# Split the issue body into sections by headers
    sections = re.split(r'(### .*\n)', issue_body)

# Process each section
for i in range(1, len(sections), 2):
    # Check if all checkboxes are checked
    if re.search(r'- \[[xX ]\]', sections[i]):
    # Not compliant, apply strikethrough to the section header
        sections[i-1] = '~~' + sections[i-1].rstrip() + '~~\n'
    else:
    # Compliant, add "Compliant" to the section header
        sections[i-1] = sections[i-1].rstrip() + ' (Compliant)\n'

# Join the sections back together
    new_issue_body = ''.join(sections)

# Write the new issue body to a markdown file
with open('issue.md', 'w') as f:
    f.write(new_issue_body)
