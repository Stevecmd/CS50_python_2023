def main():
    names = []

    # print("Enter names one per line (Ctrl-D to end):")
    print("Name:")
    while True:
        try:
            name = input()
            names.append(name.strip())
        except EOFError:
            break

    # Check if names were added
    if names:
        print(format_adieu(names))
    else:
        print("No names have been provided!")

def format_adieu(names):
    if len(names) == 1: # one name entry
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2: # two name entries
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        all_except_last_two_names = ', '.join(names[:-2])
        second_to_last = names[-2]
        last_name = names[-1]
        return f"Adieu, adieu, to {all_except_last_two_names}, {second_to_last}, and {last_name}"

if __name__ == "__main__":
    main()
