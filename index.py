import os
from start_trivia import start_trivia
from questions import questions_list


def build_menu():
    # line 8 clears the terminal every time main menu is called
    os.system('cls' if os.name == 'nt' else 'clear')

    print("? ? ? ? ? ? ? ? ? ? ? ? ?")
    print("? ? WELCOME TO TRIVIA ? ?")
    print("? ? ? ? ? ? ? ? ? ? ? ? ?")
    print("\n\n1. Start trivia.")
    print("2. Check out questions.")
    print("3. Exit")


def main_menu():
    build_menu()
    while True:
        try:
            print("\nPress number then Enter.")
            choice = int(input("\n>>> "))
            assert 0 < choice <= 3
        except ValueError:
            print("Please enter an integer. (1, 2 or 3)")
        except AssertionError:
            print("Please enter either 1, 2 or 3.")
        else:
            break

    if choice == 1:
        start_trivia()
        main_menu()

    if choice == 2:
        questions_list()
        main_menu()

    if choice != 3:
        main_menu()


main_menu()
