import math

class Beam():
    def __init__(self):
        self.partitions = int(input('Enter the number of partitions (MAX 1):\n'))
        if self.partitions == 0:
            self.x1 = float(input('Enter the Initial X Position (Length):\n'))
            self.x2 = float(input('Enter the Final X Position (Length):\n'))
            self.l1 = float(self.x2 - self.x1)
            self.d1 = float(input('Enter the Diameter:\n'))
            self.A1 = float(math.pi/4*(self.d1)**2)
            self.e1 = float(input('Enter the Elastic Modulus:\n'))
            self.t1 = float(input('Enter the Thermal Coefficient Modulus:\n'))

        elif self.partitions == 1:
            self.x1 = float(input('Enter the Initial X Position (Length):\n'))
            self.x2 = float(input('Enter the Second X Position (Length):\n'))
            self.x3 = float(input('Enter the Final X Position (Length):\n'))
            self.l1 = float(self.x2 - self.x1)
            self.l2 = float(self.x3 - self.x2)
            self.d1 = float(input('Enter the First Diameter:\n'))
            self.d2 = float(input('Enter the Second Diameter:\n'))
            self.A1 = float(math.pi/4*(self.d1)**2)
            self.A2 = float(math.pi/4*(self.d2)**2)
            self.e1 = float(input('Enter the First Elastic Modulus:\n'))
            self.e2 = float(input('Enter the Second Elastic Modulus:\n'))
            self.t1 = float(input('Enter the First Thermal Coefficient Modulus:\n'))
            self.t2 = float(input('Enter the Second Thermal Coefficient Modulus:\n'))
        
    #Determines the elastic modulus based on the point given.
    def elastic(self, point):
        if self.partitions == 0:
            if self.x1 < point and point < self.x2:
                return self.e1
            else:
                return
        else:
            if self.x1 < point and point < self.x2:
                return self.e1
            elif self.x2 < point and point < self.x3:
                return self.e2
            else:
                return 
        
    def thermal_coeff(self, point):
        if self.partitions == 0:
            if self.x1 < point and point < self.x2:
                return self.t1
            else:
                return
        else:
            if self.x1 < point and point < self.x2:
                return self.t1
            elif self.x2 < point and point < self.x3:
                return self.t2
            else:
                return 
            
    def area(self, point):
        if self.partitions == 0:
            if self.x1 < point and point < self.x2:
                return self.A1
            else:
                return
        else:
            if self.x1 < point and point < self.x2:
                return self.A1
            elif self.x2 < point and point < self.x3:
                return self.A2
            else:
                return 
    
    def give_l(self):
        if self.partitions == 0:
            return (self.l1)
        else:
            return (self.l1, self.l2)

    def give_x(self):
        if self.partitions == 0:
            return (self.x1, self.x2)
        else:
            return (self.x1, self.x2, self.x3)

    def give_t(self):
        if self.partitions == 0:
            return (self.t1)
        else:
            return (self.t1, self.t2)
    def give_e(self):
        if self.partitions == 0:
            return (self.e1)
        else:
            return (self.e1, self.e2)

    def __repr__(self):
        s = "\nThis Beam has:\n"
        s += f"{self.partitions} Partitions\n"
        if self.partitions == 0:   
            s += f"Length of: {self.l1}\n"
            s += f"X0 coordinate: {self.x1}\n"
            s += f"X1 coordinate: {self.x2}\n"
            s += f"Diameter: {self.d1}\n"
            s += f"Area: {self.A1}\n"
            s += f"Elastic Modulus: {self.e1}\n"
            s += f"Thermal Coefficient: {self.t1}\n"           
        else:
            s += f"Length 1 of: {self.l1}\n"
            s += f"Length 2 of: {self.l2}\n"
            s += f"X0 coordinate: {self.x1}\n"
            s += f"X1 coordinate: {self.x2}\n"
            s += f"X2 coordinate: {self.x3}\n"
            s += f"Diameter 1: {self.d1}\n"
            s += f"Diameter 2: {self.d2}\n"
            s += f"Area 1: {self.A1}\n"
            s += f"Area 2: {self.A2}\n"
            s += f"Elastic Modulus 1: {self.e1}\n"
            s += f"Elastic Modulus 2: {self.e2}\n"
            s += f"Thermal Coefficient 1: {self.t1}\n"
            s += f"Thermal Coefficient 2: {self.t2}\n"
        return s  