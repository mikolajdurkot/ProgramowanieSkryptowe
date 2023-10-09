from s1 import run, display

def test_display_show_index_true():
    args = ['arg1', 'arg2', 'arg3']
    expected_output = ["args[0] = arg1", "args[1] = arg2", "args[2] = arg3"]
    assert display(args, True) == expected_output

def test_display_show_index_false():
    args = ['arg1', 'arg2', 'arg3']
    expected_output = ["arg1", "arg2", "arg3"]
    assert display(args, False) == expected_output

def test_run():
    moves = ['f', 'f', 'r', 'b', 'l']
    move_descriptions = {
        'f': 'Zwierzak idzie do przodu',
        'b': 'Zwierzak idzie do tyłu',
        'r': 'Zwierzak skręca w prawo',
        'l': 'Zwierzak skręca w lewo',
    }
    expected_output = [
        'Zwierzak idzie do przodu',
        'Zwierzak idzie do przodu',
        'Zwierzak skręca w prawo',
        'Zwierzak idzie do tyłu',
        'Zwierzak skręca w lewo'
    ]
    assert run(moves, move_descriptions) == expected_output