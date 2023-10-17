import re

def grep(input_string, search_string, ignore_case=False, whole_word=False):
    lines = input_string.split('\n')
    result = []

    for line in lines:
        line1 = line
        if ignore_case:
            line = line.lower()
            search_string = search_string.lower()

        if whole_word:
            pattern = r'\b{}\b'.format(re.escape(search_string))
            if re.search(pattern, line):
                result.append(line1)
        else:
            if search_string in line:
                result.append(line1)

    return '\n'.join(result)
