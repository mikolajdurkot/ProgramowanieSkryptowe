import argparse
import sys
import operations
import cut
import grep

def main():
    parser = argparse.ArgumentParser(description="skrypt1 i skrypt2 w jednym")
    parser.add_argument("command", choices=["skrypt1", "skrypt2"], help="Wybierz skrypt")
    parser.add_argument("-d", "--delimiter", help="man cut -> -d")
    parser.add_argument("-f", "--field", type=int, help="man cut -> -f")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="man grep -> -i")
    parser.add_argument("-w", "--whole-word", action="store_true", help="man grep -> -w")
    parser.add_argument("search_string", nargs="?", help="String dla grepa")

    args = parser.parse_args()

    if args.command == "skrypt1":
        if not args.search_string:
            print("Musisz podac jakiegos stringa do edycji.")
            sys.exit(1)

        print(operations.first_character(args.search_string))
        print(operations.first_two_characters(args.search_string))
        print(operations.all_characters_except_first_two(args.search_string))
        print(operations.penultimate_character(args.search_string))
        print(operations.last_three_characters(args.search_string))
        print(operations.all_characters_in_even_positions(args.search_string))
        print(operations.merge_characters_and_duplicate(args.search_string))
    
    elif args.command == "skrypt2":
        input_data = sys.stdin.read()
        if args.delimiter and args.field:
            output = cut.cut(input_data, args.delimiter, args.field)
        elif args.search_string:
            ignore_case = args.ignore_case
            whole_word = args.whole_word
            output = grep.grep(input_data, args.search_string, ignore_case, whole_word)
        else:
            print("Invalid arguments for skrypt2.")
            sys.exit(1)

        print(output, end='')

if __name__ == "__main__":
    main()

#$ ./skrypt3.py skrypt1 <search_string>
#$ ./skrypt3.py skrypt2 -d <delimiter> -f <field> ... <input_data>
#$ ./skrypt3.py skrypt2 -i -w <search_string> ... <input_data>
