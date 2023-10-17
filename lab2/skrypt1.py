import sys
import operations

if len(sys.argv) == 1:
    print("Za malo argumentow")
    quit()

a = sys.argv[1]

print(operations.first_character(a))
print(operations.first_two_characters(a))
print(operations.all_characters_except_first_two(a))
print(operations.penultimate_character(a))
print(operations.last_three_characters(a))
print(operations.all_characters_in_even_positions(a))
print(operations.merge_characters_and_duplicate(a))