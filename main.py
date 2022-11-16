import axial

def main():
    print_welcome()
    menu()

def menu():
    print_menu()
    option = input('Choose an option:\n')
    while option != 'q':
        execute_menu(option)
        print_menu()
        option = input('Choose an option:\n') 

def execute_menu(option):
    if option == 'a':
        axial.axial_loading()

def print_menu():
    print("\nSelect a Type of Problem to Solve")
    print("a - Axial Loading")
    print("q - Quit")

def print_welcome():
    print('''
--EXTRA CREDIT PROJECT --
--ENG 104 --
--Axial Loading--
--TEAM # --
#########################''')

if __name__ == "__main__":
    main()