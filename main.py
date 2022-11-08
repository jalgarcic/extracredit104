from beam import Beam
import numpy as np
import matplotlib.pyplot as plt
beam = None
units = "SI"

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
    
def axial_loading():
    option = None
    beam = define_beam()
    print(beam)
    print_axialLoadMenu()
    while option != 'q':
        option = input('Choose an option:\n')
        execute_axial_menu(option)

def statically_det():
    print("Enter Values for Fixed Support and Forces: ")
    fixedsup_x = float(input("Enter the x of the wall: "))
    number_forces = int(input("Enter Number of Forces: "))
    forces_arr = []
    for i in range(number_forces):
        pos = float(input(f"Enter Position (X) of the Force #{i+1}: "))
        mag = float(input("Enter Magnitude Force: "))
        dir = float(input("Enter Direction Force (Enter: 1 for +X / -1 for -X): "))
        forces_arr.append([pos, mag, dir])

    rangex, forcevals = axial_solver(fixedsup_x, forces_arr)
    global beam
    sigma_lst = []
    for i in range(len(forcevals)):
        length = rangex[i,1] - rangex[i,0]
        middle = (rangex[i,1] + rangex[i,0])/2
        p = forcevals[i][0]
        e = beam.elastic(middle)
        a = round(beam.area(middle), 4)
        print(f"{p}x{length}/({a}x{e})")
        sigma_lst.append(p*length/(a*e))
    print(sigma_lst)
    

def axial_solver(fixedsup_x, forces_arr):
    F_fixed = 0.0
    for force in forces_arr:
        F_fixed += force[1]*force[2]
    F_fixed = -F_fixed
    dir = 1.0 if F_fixed > 0 else -1.0
    forces_arr.append([fixedsup_x, F_fixed, dir])
    arr = np.array(forces_arr)
    arr = arr[arr[:,0].argsort()]
    rows, _ = arr.shape
    nrows = rows-1
    rangex = np.zeros((nrows,2))
    for i in range(len(arr[:,1])-1):
        rangex[i,0] = arr[i,0]
        rangex[i,1] = arr[i+1,0]
    temp = []
    for i in range(1, len(arr[:,1])):
        s = sum(arr[i:rows, 1]*arr[i:rows, 2])
        temp.append([s,s])
    print(rangex, temp)
    plot_axial(rangex, temp)
    return rangex, temp

def plot_axial(xrange, yrange):
    pass

def define_beam():
    print("\nLet's Start By Defining the Beam")

    partitions = int(input('Enter the number of partitions (MAX 1):\n'))
    if partitions == 0:
        x0 = input('Enter the Initial X Position (Length):\n')
        x1 = input('Enter the Final X Position (Length):\n')
        d1 = input('Enter the Diameter:\n')
        elastic = [input('Enter the Elastic Modulus:\n')]
        thermal = [input('Enter the Thermal Coefficient Modulus:\n')]
        length = [x0, x1]
        d = [d1]

    elif partitions == 1:
        x0 = input('Enter the Initial X Position (Length):\n')
        x1 = input('Enter the Second X Position (Length):\n')
        x2 = input('Enter the Final X Position (Length):\n')
        d1 = input('Enter the First Diameter:\n')
        d2 = input('Enter the Second Diameter:\n')
        e1 = input('Enter the First Elastic Modulus:\n')
        e2 = input('Enter the Second Elastic Modulus:\n')
        t1 = input('Enter the First Thermal Coefficient Modulus:\n')
        t2 = input('Enter the Second Thermal Coefficient Modulus:\n')
        length = [x0, x1, x2]
        d = [d1, d2]
        elastic = [e1, e2]
        thermal = [t1, t2]

    beam = Beam(length, d, elastic, coefficient_thermal = thermal, partitions = partitions)
    return beam

def execute_menu(option):
    if option == 'a':
        axial_loading()

def execute_axial_menu(option):
    if option == 'a':
        statically_det()
    elif option == 'b':
        pass
    elif option == 'c':
        pass


## Print Functions

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

def print_axialLoadMenu():
    print("Available Solutions")
    print("a - Statically Determinate Displacement with Force")
    print("b - Statically Indeterminate Displacement")
    print("c - Check if Statically Indeterminate")
    print("q - Exit")

if __name__ == "__main__":
    main()