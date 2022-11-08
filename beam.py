import math

class Beam():
    def __init__(self, length, diameter, elastic_modulus, coefficient_thermal, partitions = 0):
        self.partitions = partitions
        if self.partitions == 0:
            self.x1 = float(length[0])
            self.x2 = float(length[1])
            self.l1 = self.x2 - self.x1
            self.d1 = float(diameter[0])
            self.A1 = math.pi/4*(self.d1)**2
            self.e1 = float(elastic_modulus[0])
            self.t1 = float(coefficient_thermal[0])
        else:
            self.x1 = float(length[0])
            self.x2 = float(length[1])
            self.x3 = float(length[2])
            self.l1 = self.x2 - self.x1
            self.l2 = self.x3 - self.x2
            self.d1 = float(diameter[0])
            self.d2 = float(diameter[1])
            self.A1 = math.pi/4*(self.d1)**2
            self.A2 = math.pi/4*(self.d2)**2
            self.e1 = float(elastic_modulus[0])
            self.e2 = float(elastic_modulus[1])
            self.t1 = float(coefficient_thermal[0])
            self.t2 = float(coefficient_thermal[1])
    
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
            s += f"Thermal Coefficient 2: {self.t1}\n"
        return s  

        

