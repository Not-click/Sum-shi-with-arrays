class Slist:
    def __init__(self, *args):
        self.numbers = []
        for item in args:
            self.numbers.append(item)
            
    def __radd__(self,other):
      a = []
      for item in self.numbers:
        a.append(item + other)
      return(a)
      
    def __add__(self,other):
      try:
        a = []
        if (isinstance(self.numbers,list)) and (isinstance(self.numbers,list)):
          for item in range(len(self.numbers)):
            a.append(self.numbers[item] + other.numbers[item])
          return(a)
      except:
        pass
      
      for item in self.numbers:
        a.append(item + other)
      return(a)
      
    def __repr__(self):
      return(str(self.numbers))
