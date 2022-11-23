import numpy as np
import matplotlib.pyplot as plt
from beam import Beam

beam = None

def axial_loading():
    global beam
    beam = Beam()
    print(beam)
    print_axialLoadMenu()
    option = input('Choose an option:\n')
    while option != 'q':
        execute_axial_menu(option)
        print_axialLoadMenu()
        option = input('Choose an option:\n')

def determine_displacement():
    global beam

    print("Enter Values for Fixed Support and Forces: ")
    print("We Assume First Wall is at X=0")
    number_forces = int(input_num("Enter Number of Forces: "))
    delta_T = input_num("Enter change in temperature: ")

    # Forces_arr will be a matrix with each row describing a force in the form of 
    # [[Position_F_1, Magnitude_F_1, Direction_F_1], ...
    # [Position_F_n, Magnitude_F_n, Direction_F_n]]
    # This is NOT a Numpy array and thus should be accessed as forces_arr[row][col]
    forces_arr = []
    for i in range(number_forces):
        pos = input_num(f"Enter Position (X) of the Force #{i+1}: ")
        mag = input_num("Enter Magnitude Force: ")
        dir = input_num("Enter Direction Force (Enter: 1 for +X / -1 for -X): ")
        forces_arr.append([pos, mag, dir])

    range_x, pvals = make_intervals(0, forces_arr)
    
    return total_displacement(range_x, pvals, delta_T)
    
def total_displacement(range_x, pvals, delta_T):
    # We use the Beam class methods to get properties depending on the x values.
    # Ww use it to calculate sigma.
    sigma_lst = []
    for i in range(len(pvals)):
        length = range_x[i,1] - range_x[i,0]
        middle = (range_x[i,1] + range_x[i,0])/2
        p = pvals[i][0]
        e = beam.elastic(middle)
        a = round(beam.area(middle), 4)
        print(f"Sigma p_{i} = {p}x{length}/({a}x{e})")
        sigma_lst.append(p*length/(a*e))

    lens = beam.give_l()
    alphas = beam.give_t()
    if beam.partitions == 0:
        print(f"Sigma_T = {alphas}x{delta_T}x{lens}")
        sigma_lst.append(alphas*delta_T*lens)
    else:
        for l, a in zip(lens, alphas):
            print(f"Sigma_T = {a}x{delta_T}x{l}")
            sigma_lst.append(a*delta_T*l)

    print("Sigma Total =",sum(sigma_lst))
    return sum(sigma_lst)

def indeterminate():
    print("Enter Values for Fixed Support and Forces: ")
    print("We Assume First Wall (A) is at X=0 and Second Wall (B) is at X = L")
    print("We assume we have a Force (P)")
    
    sigma_lst = []
    lens = beam.give_l()
    alphas = beam.give_t()
    forces_arr = []

    delta_T = input_num("Enter change in temperature: ")
    sigma_user = input_num("Enter sigma between beam and B: ")

    mag = input_num("Enter Magnitude Force: ")
    dir = input_num("Enter Direction Force (Enter: 1 for +X / -1 for -X): ")
    forces_arr.extend([0, mag, dir])

    if beam.partitions == 0:
        pos = input_num("Enter Position Force: ")
        l1 = pos
        l2 = beam.x2 - pos
        print(f"Sigma_T = {alphas}x{delta_T}x{lens}")
        sigma_lst.append(alphas*delta_T*lens)
        a = np.array(
            [[1, 1],
            [l1/(beam.A1*beam.e1), -l2/(beam.A1*beam.e1)]])
        b = np.array([forces_arr[1]*forces_arr[2], sigma_user - sum(sigma_lst)])
        solution = np.linalg.solve(a, b)
        print("FA:", solution[0], "FB", solution[1])
    else:
        for l, a in zip(lens, alphas):
            print(f"Sigma_T = {a}x{delta_T}x{l}")
            sigma_lst.append(a*delta_T*l)
        a = np.array(
            [[1, 1],
            [lens[0]/(beam.A1*beam.e1), -lens[1]/(beam.A2*beam.e2)]])
        b = np.array([forces_arr[1]*forces_arr[2], sigma_user - sum(sigma_lst)])
        solution = np.linalg.solve(a, b)
        print("FA:", solution[0], "FB", solution[1])

def make_intervals(fixedsup_x, forces_arr):
    # First we solve for resultant at f_fixed and append it with all the forces.
    # Note that direction should be opposite to resultant.
    f_fixed = 0.0
    for force in forces_arr:
        f_fixed += force[1]*force[2] # Mag * Direction
    dir = -1.0 
    forces_arr.append([fixedsup_x, f_fixed, dir])

    # Now make a numpy array for easy sorting.
    # Note: Numpy slicing is in the form of [rows, cols]
    arr = np.array(forces_arr)
    arr = arr[arr[:,0].argsort()]
    rows, _ = arr.shape

    # Nrows refers to the number of intervals.
    nrows = rows-1

    # range_x will be a matrix for intervals in the form of 
    # [[X0, X1], ..., [Xn-1, Xn]] where n is nrows
    range_x = np.zeros((nrows, 2))
    for i in range(nrows): 
        range_x[i,0] = arr[i,0] 
        range_x[i,1] = arr[i+1,0] 
    
    # p_vals will be an array for compression/tension force at each interval.
    p_vals = []

    # We use the method of sections and we get force  equal at each
    # "n" interval equals the sum of forces from sigma(n -> final force).
    for i in range(1, rows):
        s = sum(arr[i:rows, 1]*arr[i:rows, 2]) # Magnitude*Direction
        p_vals.append([s,s])

    plot_axial(range_x, p_vals)
    return range_x, p_vals

def plot_axial(range_x, range_y):
    for i in range(len(range_y)):
        plt.plot(range_x[i], range_y[i])
        plt.axvline(x=range_x[i][1], linestyle='--')
    plt.xlabel('X')
    plt.ylabel('P(X)')
    plt.grid(True, which="Both")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

def determine_state(calc_displacement):
    user_disp = input_num("\nEnter the distance from the beam to the other wall: ")
    if calc_displacement >= user_disp:
        print("\nStatically Indeterminate: Please Use Option c from Menu")
    else:
        print("\nStatically Determinate: Please Use Option b from Menu")

def execute_axial_menu(option):
    if option == 'a':
        calc_displacement = determine_displacement()
        determine_state(calc_displacement)

    elif option == 'b':
        determine_displacement()
    elif option == 'c':
        indeterminate()

def print_axialLoadMenu():
    print("\nAvailable Solutions")
    print("a - Check if Statically Indeterminate")
    print("b - Statically Determinate Displacement")
    print("c - Statically Indeterminate Displacement")
    print("q - Exit")
           
def input_num(text):
    num = input(text)
    cond = True
    while cond:
        try:
            num = float(num)
            cond = False
        except:
            print("Please Enter a Valid Number!")
            num = input(text)
    return num
