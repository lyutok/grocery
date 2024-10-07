def main():
    sorted_list = list()
    for i in sorted_list:
        print(f"{sorted_list[i]} {i}")


def list():
    groceries = {}

    while True:
        try:
            grocery = input("").upper()
        except EOFError:
            print()
            break
        else:
            if grocery not in groceries:
                # grocery = grocery
                groceries[grocery] = 1
            else:
                groceries[grocery] += 1

    return dict(sorted(groceries.items()))


main()
