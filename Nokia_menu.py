def handle_phonebook():
    phonebook_menu = """
    Nokia 3310 Phonebook
    Press
    1 -> Search
    2 -> Service Nos.1
    3 -> Add name
    4 -> Erase
    5 -> Edit
    6 -> Assign tone
    7 -> Send b'card
    8 -> Options
    9 -> Speed dials
    10 -> Voice tags
    0 -> Go back to main menu
    """

    while True:
        print(phonebook_menu)
        phonebook_choice = int(input("Enter your choice: "))

        if phonebook_choice == 1:
            print("Search")
        elif phonebook_choice == 2:
            print("Service Nos.1")
        elif phonebook_choice == 3:
            print("Add name")
        elif phonebook_choice == 4:
            print("Erase")
        elif phonebook_choice == 5:
            print("Edit")
        elif phonebook_choice == 6:
            print("Assign tone")
        elif phonebook_choice == 7:
            print("Send b'card")
        elif phonebook_choice == 8:
            print("Options")
            while True:
                print("""
                Nokia 3310 Option
                Press
                1 -> Type of view
                2 -> Memory status
                0 -> Go back to Phonebook menu
                """)
                option_choice = int(input("Enter your choice: "))
                if option_choice == 1:
                    print("Type of view")
                elif option_choice == 2:
                    print("Memory status")
                elif option_choice == 0:
                    break
                else:
                    print("Enter a correct number")
        elif phonebook_choice == 9:
            print("Speed dials")
        elif phonebook_choice == 10:
            print("Voice tags")
        elif phonebook_choice == 0:
            print("Going back to main menu...")
            break
        else:
            print("Enter a correct number")


def handle_messages():
    message_menu = """
    Nokia 3310 messages
    Press
    1 -> Write messages
    2 -> Inbox
    3 -> Out box
    4 -> Picture messages
    5 -> Template
    6 -> Smileys
    7 -> Message settings
    8 -> Info service
    9 -> Voice mailbox number
    10 -> Service command editor
    0 -> Go back to main menu
    """

    while True:
        print(message_menu)
        message_choice = int(input("Enter your choice: "))

        if message_choice == 1:
            print("Write messages")
        elif message_choice == 2:
            print("Inbox")
        elif message_choice == 3:
            print("Out box")
        elif message_choice == 4:
            print("Picture messages")
        elif message_choice == 5:
            print("Template")
        elif message_choice == 6:
            print("Smileys")
        elif message_choice == 7:
            print("Message settings")
            while True:
                print("""
                Nokia 3310 settings
                Press
                1 -> Set 1
                2 -> Common
                0 -> Go back to Message menu
                """)
                message_setting_choice = int(input("Enter your choice: "))
                if message_setting_choice == 1:
                    print("Set 1")
                elif message_setting_choice == 2:
                    print("Common")
                elif message_setting_choice == 0:
                    break
                else:
                    print("Enter a correct number")
        elif message_choice == 8:
            print("Info service")
        elif message_choice == 9:
            print("Voice mailbox number")
        elif message_choice == 10:
            print("Service command editor")
        elif message_choice == 0:
            print("Going back to main menu...")
            break
        else:
            print("Enter a correct number")


def main():
    while True:
        print("""
        Mr.Chibuzor's Assignment !!!
        Nokia 3310 Menu
        Press
        1 -> Phone book
        2 -> Messages
        3 -> Chat
        4 -> Call register
        5 -> Tones
        6 -> Settings
        7 -> Call divert
        8 -> Games
        9 -> Calculator
        10 -> Reminders
        11 -> Clock
        12 -> Profiles
        13 -> SIM services
        0 -> Exit
        """)

        choice = int(input("Welcome Martin Select Option(or 0 to exit): "))

        if choice == 1:
            handle_phonebook()
        elif choice == 2:
            handle_messages()
        # Add handling for other menu options
        elif choice == 0:
            print("Exiting... Goodbye")
            break
        else:
            print("Enter a correct number")


if __name__ == "__main__":
    main()
