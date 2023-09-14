import json
import re

def evaluate_checkmarks(section):
    checkmarks = re.findall(r'- \[[xX ]\]', section)
    if not checkmarks:
        return None
    return all(mark == '- [x]' or mark == '- [X]' for mark in checkmarks)

def apply_strikethrough(section):
    lines = section.split('\n')
    for i in range(len(lines)):
        if lines[i] and not lines[i].startswith('-'):
            lines[i] = '~~' + lines[i] + '~~'
    return '\n'.join(lines)

def add_compliant(section):
    return section.rstrip() + ' COMPLIANT\n'

def main():
    with open('event.json', 'r') as f:
        event_data = json.load(f)

    issue_data = event_data['event']['issue']
    issue_title = issue_data['title']
    issue_body = issue_data['body']

    sections = re.split(r'(### .*\n)', issue_body)

    for i in range(1, len(sections), 2):
        evaluation = evaluate_checkmarks(sections[i+1])
        if evaluation is None:
            continue
        elif evaluation:
            sections[i] = add_compliant(sections[i])
        else:
            sections[i] = apply_strikethrough(sections[i].rstrip() + '\n')
            sections[i+1] = apply_strikethrough(sections[i+1])
            if i+2 < len(sections):
                sections[i+2] = apply_strikethrough(sections[i+2])

    new_issue_body = ''.join(sections)

    with open(f'{issue_title}.md', 'w') as f:
        f.write(f'# {issue_title}\n\n{new_issue_body}')

if __name__ == "__main__":
    main()
