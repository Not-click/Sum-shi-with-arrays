class Slist(list):
  def __init__(self,*args):
    super().__init__(args)
    
  def __add__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            a.append(self[i]+other[i])
          elif(isinstance(self[i],(str)) and (isinstance(other[i],(str)))):
            a.append(self[i]+other[i])
          else:
            raise TypeError(f"Cannot add {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe concider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          a.append(i+other)
        elif(isinstance(i,(str)) and (isinstance(other,(str)))):
          a.append(i+other)
        else:
          raise TypeError(f"Cannot add {type(i)} with {type(other)}")
      return a

  def __radd__(self,other):
    a=Slist()
    if(isinstance(other,(Slist,list))):
      if (len(other) == len(self)):
        for i in range(0,len(other)):
          if(isinstance(other[i],(int,float))) and (isinstance(self[i],(int,float))):
            a.append(other[i]+self[i])
          elif((isinstance(other[i],str)) and (isinstance(self[i],str))):
            a.append(other[i]+self[i])
          else:
            raise TypeError (f"Cannot add {type(other[i])} with {type(self[i])}")
      else:
        raise ValueError (f"{self} and {other} dont have the same number of elements.Maybe consider making their lengths equal")
    elif(isinstance(other,(int,float))):
      for i in self:
        if (isinstance(i,(int,float))):
          a.append(other+i)
        else:
          raise TypeError (f"Cannot add {type(other)} with {type(i)}")
    elif(isinstance(other,str)):
      for i in self:
        if (isinstance(i,str)):
          a.append(other+i)
        else:
          raise TypeError (f"Cannot perform operation of {type(i)} with {type(other)} ")
    else:
      raise TypeError (f"Invalid type operation of {type(self)} with {type(other)}")
    return a

  def __sub__(self,other):
      a=Slist()
      if (isinstance(other,(Slist,list))):
###########   
        if (len(self) == len(other)):
###########      
          for i in range(0,len(self)):
###########
            if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
              a.append(self[i]-other[i])
            else:
              raise TypeError(f"Cannot subtract {type(self[i])} with {type(other[i])}")
          return a
###########
        else:
          raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
      else:
        for i in self:
          if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
            a.append(i-other)
          else:
            raise TypeError(f"Cannot subtract {type(i)} with {type(other)}")
      return a

  def __rsub__(self,other):
    a=Slist()
    if(isinstance(other,(Slist,list))):
      if (len(other) == len(self)):
        for i in range(0,len(other)):
          if(isinstance(other[i],(int,float))) and (isinstance(self[i],(int,float))):
            a.append(other[i]-self[i])
          else:
            raise TypeError (f"Cannot subtract {type(other[i])} with {type(self[i])}")
      else:
        raise ValueError (f"{self} and {other} dont have the same number of elements.Maybe consider making their lengths equal")
    elif(isinstance(other,(int,float))):
      for i in self:
        if (isinstance(i,(int,float))):
          a.append(other-i)
        else:
          raise TypeError (f"Cannot subtract {type(other)} with {type(i)}")
    else:
      raise TypeError (f"Invalid type operation of {type(self)} with {type(other)}")
    return a
    
    
  def __mul__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            a.append(self[i]*other[i])
          else:
            raise TypeError(f"Cannot multiply {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          a.append(i*other)
        else:
          raise TypeError(f"Cannot multiply {type(i)} with {type(other)}")
      return a
      
      
  def __rmul__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            a.append(other[i]*self[i])
          else:
            raise TypeError(f"Cannot multiply {type(other[i])} with {type(self[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          a.append(i*other)
        else:
          raise TypeError(f"Cannot multiply {type(i)} with {type(other)}")
      return a
      
      
  def __truediv__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            if other[i] != 0:
              a.append(self[i]/other[i])
            else:
              raise ZeroDivisionError (f"Trying to divide by zero.Zero found at {other} at index of {i}")
          else:
            raise TypeError(f"Cannot divide {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
            a.append(i/other)
        else:
          raise TypeError(f"Cannot divide {type(i)} with {type(other)}")
        return a
      
      
  def __rtruediv__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(other[i],(int,float)) and (isinstance(self[i],(int,float)))):
            if self[i] != 0:
              a.append(other[i]/self[i])
            else:
              raise ZeroDivisionError (f"Trying to divide by zero.Zero found at {self} at index of {i}")
          else:
            raise TypeError(f"Cannot divide {type(other[i])} with {type(self[i])}")
        return a
###########
      else:
        raise ValueError(f"{other} and {self} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          if i != 0:
            a.append(other/i)
          else:
            raise ZeroDivisionError (f"Trying to divide by zero.Zero found at {self} at index of {i}")
        else:
          raise TypeError(f"Cannot divide {type(other)} with {type(i)}")
      return a
      
      
  def __floordiv__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            if other[i] != 0:
              a.append(self[i]//other[i])
            else:
              raise ZeroDivisionError (f"Trying to int divide by zero.Zero found at {other} at index of {i}")
          else:
            raise TypeError(f"Cannot int divide {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
            a.append(i//other)
        else:
          raise TypeError(f"Cannot int divide {type(i)} with {type(other)}")
        return a
        
  def __rfloordiv__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(other[i],(int,float)) and (isinstance(self[i],(int,float)))):
            if self[i] != 0:
              a.append(other[i]//self[i])
            else:
              raise ZeroDivisionError (f"Trying to int divide by zero.Zero found at {self} at index of {i}")
          else:
            raise TypeError(f"Cannot int divide {type(other[i])} with {type(self[i])}")
        return a
###########
      else:
        raise ValueError(f"{other} and {self} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          if i != 0:
            a.append(other//i)
          else:
            raise ZeroDivisionError (f"Trying to int divide by zero.Zero found at {self} at index of {i}")
        else:
          raise TypeError(f"Cannot int divide {type(other)} with {type(i)}")
      return a
      
  def __mod__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            if other[i] != 0:
              a.append(self[i]%other[i])
            else:
              raise ZeroDivisionError (f"Trying to modulo by zero.Zero found at {other} at index of {i}")
          else:
            raise TypeError(f"Cannot modulo {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
            a.append(i%other)
        else:
          raise TypeError(f"Cannot modulo {type(i)} with {type(other)}")
        return a
        
         
  def __rmod__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(other[i],(int,float)) and (isinstance(self[i],(int,float)))):
            if self[i] != 0:
              a.append(other[i]%self[i])
            else:
              raise ZeroDivisionError (f"Trying to modulo by zero.Zero found at {self} at index of {i}")
          else:
            raise TypeError(f"Cannot modulo {type(other[i])} with {type(self[i])}")
        return a
###########
      else:
        raise ValueError(f"{other} and {self} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          if i != 0:
            a.append(other%i)
          else:
            raise ZeroDivisionError (f"Trying to modulo by zero.Zero found at {self} at index of {i}")
        else:
          raise TypeError(f"Cannot modulo {type(other)} with {type(i)}")
      return a
        
        
  def __pow__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            a.append(self[i]**other[i])
          else:
            raise TypeError(f"Cannot power {type(self[i])} with {type(other[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          a.append(i**other)
        else:
          raise TypeError(f"Cannot power {type(i)} with {type(other)}")
      return a
      
  def __rpow__(self,other):
    a=Slist()
    if (isinstance(other,(Slist,list))):
###########   
      if (len(self) == len(other)):
###########      
        for i in range(0,len(self)):
###########
          if(isinstance(self[i],(int,float)) and (isinstance(other[i],(int,float)))):
            a.append(other[i]**self[i])
          else:
            raise TypeError(f"Cannot power {type(other[i])} with {type(self[i])}")
        return a
###########
      else:
        raise ValueError(f"{self} and {other} dont have the same length.Maybe consider making their lengths equal")
    else:
      for i in self:
        if(isinstance(i,(int,float)) and (isinstance(other,(int,float)))):
          a.append(i**other)
        else:
          raise TypeError(f"Cannot power {type(i)} with {type(other)}")
      return a

#Testing area do not cross  
List = Slist(0,1,2,3,4,5)
List2 = Slist(1,1,1,1,1,1)
List3 = Slist("0","1","2","3","4","5")
List4 = List + List2
List5 = Slist(2,3)
List6 = Slist(0,1,2,3,4,5)
