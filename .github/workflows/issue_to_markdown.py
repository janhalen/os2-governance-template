import json
import re

def evaluate_checkmarks(section):
    """
    Evaluate if all checkmarks in a section are marked.
    If no checkmarks are found, return None.
    """
    checkmarks = re.findall(r'- \[[xX ]\]', section)
    if not checkmarks:
        return None
    return all(mark == '- [x]' or mark == '- [X]' for mark in checkmarks)

def add_emoji(section, compliant):
    """
    Add a check mark emoji to compliant sections and a cross mark to non-compliant ones.
    """
    if compliant:
        return section.rstrip() + ' ✅\n'
    else:
        return section.rstrip() + ' ❌\n'

def main():
    """
    Main function to evaluate GitHub issue sections and generate a markdown file.
    """
    try:
        with open('event.json', 'r') as f:
            event_data = json.load(f)
    except FileNotFoundError:
        print("The file 'event.json' was not found.")
        return

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
