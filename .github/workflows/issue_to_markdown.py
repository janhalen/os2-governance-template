import json
import re

def evaluate_checkmarks(section):
    checkmarks = re.findall(r'- \[[xX ]\]', section)
    if not checkmarks:
        return None
    return all(mark == '- [x]' or mark == '- [X]' for mark in checkmarks)

def add_emoji(section, compliant):
    if compliant:
        return section.rstrip() + ' ✅\n'  # Add a green check mark emoji
    else:
        return section.rstrip() + ' ❌\n'  # Add a red cross mark emoji

def main():
    with open('event.json', 'r') as f:
        event_data = json.load(f)

    issue_data = event_data['event']['issue']
    issue_title = issue_data['title']
    issue_body = issue_data['body']

    sections = re.split(r'(### .*\n)', issue_body)

    for i in range(1, len(sections), 2):
        evaluation = evaluate_checkmarks(sections[i+1])
        if evaluation is not None:
            sections[i] = add_emoji(sections[i], evaluation)

    new_issue_body = ''.join(sections)

    with open(f'{issue_title}.md', 'w') as f:
        f.write(f'# {issue_title}\n\n{new_issue_body}')

if __name__ == "__main__":
    main()
