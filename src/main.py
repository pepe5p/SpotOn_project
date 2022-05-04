from src.food_search import find_food
import ast


def main() -> None:
    """
    Entrypoint of program.

    Gets input from user by terminal.
    """

    print("\n"
          "Enter ingredients that you have.\n"
          "You can write list or simply write ingredient followed by <ENTER> "
          "e.g. ['rice', 'cheese', 'pork'] or rice\n"
          "When you dont want ingredient or list, place '-' before its name "
          "e.g. -['rice', 'cheese', 'pork'] or -rice\n"
          "If you wrote everything, end with word: 'END'."
          "\n")

    included_ingr = []
    excluded_ingr = []
    while True:
        ingr = input()
        if ingr == 'END':
            break
        elif ingr[0] == '-':
            ingr = ingr[1:]
            if ingr[0] == '[' and ingr[-1] == ']':
                excluded_ingr += ast.literal_eval(ingr)
            else:
                excluded_ingr.append(ingr)
        else:
            if ingr[0] == '[' and ingr[-1] == ']':
                included_ingr += ast.literal_eval(ingr)
            else:
                included_ingr.append(ingr)

    if excluded_ingr:
        find_food(included_ingr, excluded_ingr)
    else:
        find_food(included_ingr)


if __name__ == '__main__':
    main()
