class Slist:
    def __init__(self, *args):
        self.numbers = []
        for item in args:
            self.numbers.append(item)
            
    def __radd__(self,other):
      a = []
      for item in self.numbers:
        a.append(other + item)
      return(a)
    def __rsub__(self,other):
      a = []
      for item in self.numbers:
        a.append(other - item)
      return(a)    
    def __rmul__(self,other):
      a = []
      for item in self.numbers:
        a.append(other * item)
      return(a)
    def __rtruediv__(self,other):
      a = []
      for item in self.numbers:
        a.append(other / item)
      return(a)
    def __rfloordiv__(self,other):
      a = []
      for item in self.numbers:
        a.append(other // item)
      return(a)
    def __rmod__(self,other):
      a = []
      for item in self.numbers:
        a.append(other % item)
      return(a)
    def __rpow__(self,other):
      a = []
      for item in self.numbers:
        a.append(other ** item)
      return(a)
      
    def __add__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] + other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item + other)
      return(a)
      
    def __sub__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] - other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item - other)
      return(a)
    def __mul__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] * other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item * other)
      return(a)
    def __truediv__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] / other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item / other)
      return(a)
      
    def __floordiv__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] // other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item // other)
      return(a)
   
    def __mod__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] % other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item % other)
      return(a)
      
    def __pow__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(other.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] ** other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item ** other)
      return(a)
      
    def __repr__(self):
      return(str(self.numbers))

"""        
instance = Slist(1, 2, 3, 4, 5)
instance2 = Slist(1, 1, 1, 1, 1)

print()

#The test code for addition
print(1 + instance2)
print(instance2 + 1)
print(instance + instance2)

#The test code for subtraction
print(1 - instance2)
print(instance2 - 1)
print(instance - instance2)

#The test code for multiplication
print(2 * instance2)
print(instance2 * 2)
print(instance * instance2)

#The test code for true division
print(1 / instance2)
print(instance2 / 1)
print(instance / instance2)

#The test code for floor division
print(1 // instance2)
print(instance2 // 1)
print(instance // instance2)

#The test code for modulas
print(1 % instance2)
print(instance2 % 1)
print(instance % instance2)

#The test code for exponent
print(0 ** instance2)
print(instance2 ** 0)
print(instance ** instance2)
"""
