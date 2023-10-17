import sys

def main():
    if len(sys.argv) < 2:
        print("Źle napisana komenda - prawidłowe użycie: ./skrypt2.py <cut/grep> [opcje]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "cut":
        import cut
        if len(sys.argv) < 5:
            print("Źle napisana komenda - prawidłowe użycie: ./skrypt2.py cut -d <delimiter> -f <field>")
            sys.exit(1)
        delimiter = sys.argv[3]
        field = int(sys.argv[5])

        input_data = sys.stdin.read()
        output = cut.cut(input_data, delimiter, field)
        print(output, end='')

    elif command == "grep":
        import grep
        ignore_case = "-i" in sys.argv[2:]
        whole_word = "-w" in sys.argv[2:]

        search_string = sys.argv[-1]
        input_data = sys.stdin.read()
        output = grep.grep(input_data, search_string, ignore_case, whole_word)
        print(output, end='')

    else:
        print("Nieistniejąca komenda: ", command)

if __name__ == "__main__":
    main()
