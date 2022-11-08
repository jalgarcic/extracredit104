import axial

def main():
    print_welcome()
    menu()

def menu():
    print_menu()
    option = input('Choose an option:\n')
    while option != 'q':
        if option in ['a']:
            execute_menu(option)
        print()
        print_menu()
        option = input('Choose an option:\n') 

def execute_menu(option):
    if option == 'a':
        axial.axial_loading()

def print_welcome():
    print('''
--EXTRA CREDIT PROJECT --
--ENG 104 --
--TEAM # --
#########################''')

def print_menu():
    print("\nSelect a Type of Problem to Solve")
    print("a - Axial Loading")
    print("q - Quit")

if __name__ == "__main__":
    main()