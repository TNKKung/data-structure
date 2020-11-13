
def findMaximum(data):
   if len(data) == 1 :
      return data[0]
   else :
      maxnumber = findMaximum(data[1:])
      Max = data[0]
      if maxnumber > Max :
         Max = maxnumber 
      return Max

data = list(map(int,input('Enter Number : ').split(' ')))
print(findMaximum(data))