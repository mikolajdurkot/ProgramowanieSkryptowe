import sys


def run(moves, move_descriptions):
    output = []
    for move in moves:
        if move in move_descriptions:
            output.append(move_descriptions[move])
    return output


def display(args, show_index):
    output = []
    if show_index:
        for i, arg in enumerate(args):
            output.append(f'args[{i}] = {arg}')
    else:
        output = args
    return output


show_index = True #or False
args = sys.argv[0:]
flag = 0

move_descriptions = {
    'f': 'Zwierzak idzie do przodu',
    'b': 'Zwierzak idzie do tyłu',
    'r': 'Zwierzak skręca w prawo',
    'l': 'Zwierzak skręca w lewo',
}

for arg in args:
    if arg in ('f', 'b', 'r', 'l'):
        flag = 1
        args = sys.argv[1:]
        args = run(args, move_descriptions)
        break


print("Start")
if flag == 1:
    for i in range (0,len(args)):
        print(display(args, False)[i])
else:
    for i in range (0,len(args)):
        print(display(args, show_index)[i])
print("Stop")