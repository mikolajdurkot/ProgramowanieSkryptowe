'''
def first_character(tekst):
    if len(tekst) > 0:
        return tekst[0]
    else:
        return ''
def first_two_characters(tekst):
    if len(tekst) >= 2:
        return tekst[0]+tekst[1]
    else:
        return ''
def all_characters_except_first_two(tekst):
    if len(tekst) > 2:
        return tekst[2:]
    else:
        return ''
def penultimate_character(tekst):
    if len(tekst) > 1:
        return tekst[-2]
    else:
        return ''
def last_three_characters(tekst):
    if len(tekst) > 2:
        return tekst[-3:]
    else:
        return ''
def all_characters_in_even_positions(tekst):
    if len(tekst) > 0:
        return tekst[::2]
    else:
        return ''
'''
def first_character(tekst):
    if len(tekst) > 0: return tekst[0]
    else: return ''
def first_two_characters(tekst):
    if len(tekst) > 1: return tekst[0]+tekst[1]
    else: return ''
def all_characters_except_first_two(tekst):
    if len(tekst) > 2: return tekst[2:]
    else: return ''
def penultimate_character(tekst):
    if len(tekst) > 1: return tekst[-2]
    else: return ''
def last_three_characters(tekst):
    if len(tekst) > 2: return tekst[-3:]
    else: return ''
def all_characters_in_even_positions(tekst):
    if len(tekst) > 0: return tekst[::2]
    else: return ''
def merge_characters_and_duplicate(string):
    first = first_character(string)
    penultimate = penultimate_character(string)
    
    if not first or not penultimate: return ""
    
    result = (first + penultimate) * len(string)
    return result
