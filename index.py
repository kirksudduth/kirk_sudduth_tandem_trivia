
# WELCOME
def build_menu():
    print("? ? ? ? ? ? ? ? ? ? ? ? ?")
    print("? ? WELCOME TO TRIVIA ? ?")
    print("? ? ? ? ? ? ? ? ? ? ? ? ?")
    print("")
    print("1. Start trivia.")
    print("2. I need a moment.")


def main_menu():
    build_menu()
    choice = input(">> ")

    if choice == "1":
        start_trivia()


build_menu()