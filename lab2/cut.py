def cut(input_string, delimiter, field):
    lines = input_string.split('\n')
    result = []

    for line in lines:
        parts = line.split(delimiter)
        if len(parts) >= field:
            result.append(parts[field - 1])

    return '\n'.join(result)
