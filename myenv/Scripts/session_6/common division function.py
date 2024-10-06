# list for common division function for 3 numbers:

def dividors(num1 , num2 ,num3):
  minimum = min(min(num1,num2),num3)
  common_dividor = [] 
  for i in range (1,minimum+1):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0 :
      common_dividor.append(i)

  return common_dividor

dividors(10,20,30) 