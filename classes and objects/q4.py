class Shape:
     def __init__(self):
         pass
     def perimeter():
         pass
class circle:
     def __init__(self,radius):
         self.r=radius
     def perimeter(self):
         return 2*3.14*self.r
class square:
     def __init__(self,side):
         self.r=side
     def perimeter(self):
         return 4*self.r
class rectangle:
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def perimeter(self):
         return 2*(self.length+self.breadth)
class equilateralTriangle:
     def __init__(self,side):
         self.base=side
     def perimeter(self):
         return 3*self.base
shape=circle(2)
print(shape.perimeter())
shape=square(2)
print(shape.perimeter())
shape=rectangle(2,4)
print(shape.perimeter())
shape=equilateralTriangle(3)
print(shape.perimeter())

