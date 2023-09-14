def convert_md_to_yaml(md_file, yaml_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    yaml_dict = []
    section_name = ''
    checkbox_id = 1
    for line in lines:
        if line.startswith('##'):
            section_name = line.strip().split('##')[1].strip()
            yaml_dict.append({
                'type': 'markdown',
                'attributes': {
                    'value': section_name
                }
            })
        elif line.startswith('|'):
            cells = re.split(r'\s*\|\s*', line.strip())[1:-1]
            if len(cells) == 5 and cells[0] not in ('', '#'):
                yaml_dict.append({
                    'type': 'checkboxes',
                    'id': f'checkbox{checkbox_id}',
                    'attributes': {
                        'label': 'Bekræft',
                        'options': [
                            {'label': cells[2]}
                        ]
                    }
                })
                yaml_dict.append({
                    'type': 'input',
                    'id': f'input{checkbox_id}',
                    'attributes': {
                        'label': cells[3]
                    }
                })
                checkbox_id += 1

    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_dict, f)

# Usage:
convert_md_to_yaml('input.md', 'output.yaml')
