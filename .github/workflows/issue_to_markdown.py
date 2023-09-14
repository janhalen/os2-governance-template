import json
import re

def evaluate_checkmarks(section):
    # This function checks if all checkmarks in a section are marked
    checkmarks = re.findall(r'- \[[xX ]\]', section)
    return all(mark == '- [x]' or mark == '- [X]' for mark in checkmarks)

def main():
    # Load the GitHub event data
    with open('event.json', 'r') as f:
        event_data = json.load(f)

    # Get the issue data
    issue_data = event_data['issue']
    issue_title = issue_data['title']
    issue_body = issue_data['body']

    # Split the issue body into sections
    sections = re.split(r'(### .*\n)', issue_body)

    # Evaluate each section and modify the headers if necessary
    for i in range(1, len(sections), 2):
        if evaluate_checkmarks(sections[i+1]):
            sections[i] = sections[i].rstrip() + ' COMPLIANT\n'

    # Join the sections back together
    new_issue_body = ''.join(sections)

    # Write to a Markdown file
    with open(f'{issue_title}.md', 'w') as f:
        f.write(f'# {issue_title}\n\n{new_issue_body}')

if __name__ == "__main__":
    main()
