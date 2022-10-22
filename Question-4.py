def printValidPar(left, right, out):
  if right==0:
    return

  elif left==0:
    print(out+right*")")

  elif left==right:
    printValidPar(left-1, right, out+"(")

  else:
    printValidPar(left-1, right, out+"(") 
    printValidPar(left, right-1, out+")") 


#driver function
def validPar(n):
  printValidPar(n,n,"")


s = int(input())
validPar(n)