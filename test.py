import matplotlib.pyplot as plt
import numpy as np
from beam import Beam

arr = np.array([[1.0, 16.0, -1.0], [2.5, 8.0, -1.0], [4.5, 15.0, 1.0], [0.0, 9.0, 1]])
arr = arr[arr[:,0].argsort()]
rows, col = arr.shape
nrows = rows-1
rangex = np.zeros((nrows,2))

for i in range(len(arr[:,1])-1):
    rangex[i,0] = arr[i,0]
    rangex[i,1] = arr[i+1,0]

temp = []
for i in range(1, len(arr[:,1])):
    s = sum(arr[i:rows, 1]*arr[i:rows, 2])
    temp.append([s,s])

#Displacement
# sigma = P*L/A*E

a = 1
e = 1
beam = Beam([0, 2.5, 4.5], [1.595769122, 1.1283791], [29000, 29000], coefficient_thermal = [1,1], partitions = 1)
#(self, length, diameter, elastic_modulus, coefficient_thermal, partitions = 0):
print(beam)
sigma_lst = []
for i in range(len(temp)):
    length = rangex[i,1] - rangex[i,0]
    middle = (rangex[i,1] + rangex[i,0])/2
    p = temp[i][0]
    e = beam.elastic(middle)
    a = round(beam.area(middle), 4)
    print(f"{p}x{length}/({a}x{e})")
    sigma_lst.append(p*length/(a*e))

#sigmaT = alpha*deltaT*len
delta_T = 10
lengths = beam.give_l()
alphas = beam.give_t()
for l, a in zip(lengths, alphas):
    print(f"sigma = {a}x{delta_T}x{l})")
    sigma_lst.append(a*delta_T*l)

print(sigma_lst)
print(sum(sigma_lst))

# for i in range(len(temp)):
#     plt.plot(rangex[i], temp[i])
# plt.xlabel('X')
# plt.ylabel('P(X)')
# plt.grid(True, which="Both")
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.show()
