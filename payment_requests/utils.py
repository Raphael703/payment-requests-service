def format_name(name):
    if not name:
        return ''
    name_parts = name.split()
    initials = name_parts.pop(0) + ' '
    for name_part in name_parts:
        initials += f'{name_part[:1]}.'
    return initials.strip()
