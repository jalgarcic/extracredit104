from beam import Beam
import numpy as np
import matplotlib.pyplot as plt

beam = None

def axial_loading():
    option = None
    global beam
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
    delta_T = float(input("Enter change in temperature: "))
    forces_arr = []
    for i in range(number_forces):
        pos = float(input(f"Enter Position (X) of the Force #{i+1}: "))
        mag = float(input("Enter Magnitude Force: "))
        dir = float(input("Enter Direction Force (Enter: 1 for +X / -1 for -X): "))
        forces_arr.append([pos, mag, dir])

    range_x, forcevals = make_intervals(fixedsup_x, forces_arr)

    global beam
    sigma_lst = []
    for i in range(len(forcevals)):
        length = range_x[i,1] - range_x[i,0]
        middle = (range_x[i,1] + range_x[i,0])/2
        p = forcevals[i][0]
        e = beam.elastic(middle)
        a = round(beam.area(middle), 4)
        print(f"Sigma {i} = {p}x{length}/({a}x{e})")
        sigma_lst.append(p*length/(a*e))
    lengths = beam.give_l()
    alphas = beam.give_t()
    if beam.partitions == 0:
        print(f"Sigma = {alphas}x{delta_T}x{lengths}")
        sigma_lst.append(alphas*delta_T*lengths)
    else:
        for l, a in zip(lengths, alphas):
            print(f"Sigma = {a}x{delta_T}x{l})")
            sigma_lst.append(a*delta_T*l)

    print("Sigma Total =",sum(sigma_lst))
        

def make_intervals(fixedsup_x, forces_arr):
    # First we solve for resultant at f_fixed and append it with all the forces.
    F_fixed = 0.0
    for force in forces_arr:
        F_fixed += force[1]*force[2] # Mag * Direction
    F_fixed = -F_fixed 
    dir = 1.0 if F_fixed > 0 else -1.0
    forces_arr.append([fixedsup_x, F_fixed, dir])
    # Now make a numpy array for easy sorting.
    arr = np.array(forces_arr)
    arr = arr[arr[:,0].argsort()]
    rows, _ = arr.shape
    nrows = rows-1
    range_x = np.zeros((nrows,2))
    for i in range(len(arr[:,1])-1): # Make a list of intervals depending on force locations.
        range_x[i,0] = arr[i,0] # X(i)
        range_x[i,1] = arr[i+1,0] # X(i+1)
    p_vals = []
    for i in range(1, len(arr[:,1])):
        s = sum(arr[i:rows, 1]*arr[i:rows, 2]) # Sum the forces depending on the beam segment.
        p_vals.append([s,s])
    print(range_x, p_vals)
    plot_axial(range_x, p_vals)
    return range_x, p_vals

def plot_axial(rangex, yrange):
    for i in range(len(yrange)):
        plt.plot(rangex[i], yrange[i])
    plt.xlabel('X')
    plt.ylabel('P(X)')
    plt.grid(True, which="Both")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

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

def execute_axial_menu(option):
    if option == 'a':
        statically_det()
    elif option == 'b':
        pass
    elif option == 'c':
        pass

def print_axialLoadMenu():
    print("Available Solutions")
    print("a - Statically Determinate Displacement with Force")
    print("b - Statically Indeterminate Displacement")
    print("c - Check if Statically Indeterminate")
    print("q - Exit")
