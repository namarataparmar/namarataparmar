class ComplexNumber:
     def __init__(self, real, imaginary):
         self.real = real
         self.imaginary = imaginary
 
     def __add__(self, other):
         return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
 
     def __sub__(self, other):
         return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
 
     def __mul__(self, other):
         real = self.real * other.real - self.imaginary * other.imaginary
         imaginary = self.real * other.imaginary + self.imaginary * other.real
         return ComplexNumber(real, imaginary)
     def __truediv__(self, other):
         denominator = other.real ** 2 + other.imaginary ** 2
         real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
         imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
         return ComplexNumber(real, imaginary)
     def printc(self):
        print(self.real,"+j",self.imaginary)


c1 = ComplexNumber(4, 5)    
c2 = ComplexNumber(2, -3)


c1.printc()
c2.printc()

c3=c1+c2
c3.printc()

c4=c1-c2
c4.printc()

c5=c1*c2
c5.printc()

c6=c1/c2
c6.printc()

