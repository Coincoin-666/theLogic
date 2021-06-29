#   exo1 -
# 
#   Écrire un algorithme qui permettra de calculer la somme de 2 nombres, puis de multiplier le résultat par 5.
#   Le calcul de le somme devra se faire dans une fonction SumNumbers qui sera à appeler dans l'algorithme principal.
# 
#
#   SubAlgorithm - SumNumbers
#
#   Input Parameters
# 
#       num1 : integer
#       num2 : integer
# 
#   Output Parameters
# 
#       SumNumbers : integer
# 
#   Variables
# 
#       num1 : integer
#       num2 : integer
#       SumNumbers : integer
# 
#   **Instructions**
# 
#       SumNumbers <- num1 + num2
# 
#
#------------------------------------
#  
# 
#   MainAlgorithm - CalcNumbers
# 
#   Variables
#
#       SumNumbers : integer
#       sumNumber : integer
# 
#   **Instructions**
#       
#       sumNumber <- {SumNumbers} * 5

num1 = 58
num2 = 64

SumNumbers = num1 + num2
sumNumber = SumNumbers * 5

print(sumNumber)