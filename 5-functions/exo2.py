#   exo1 -
# 
#   Écrire un algorithme qui permettra de faire le modulo de 2 nombres, puis de multiplier le résultat par 60.
#   Le calcul du modulo devra se faire dans une fonction ModuloNumbers qui sera à appeler dans l'algorithme principal.
# 
#
#   SubAlgorithm - ModuloNumbers
#
#   Input Parameters
# 
#       num3 : integer
#       num4 : integer
# 
#   Output Parameters
# 
#       ModuloNumbers : integer
# 
#   Variables
# 
#       num3 : integer
#       num4 : integer
#       ModuloNumber : integer
# 
#   **Instructions**
# 
#       ModuloNumbers <- num3 % num4
#
# 
# --------------------------------------------
#  
# 
#   MainAlgorithm - CalcNumbers
# 
#   Variables
#
#       ModuloNumbers : integer
#       moduloNumber : integer
# 
#   **Instructions**
# 
#       moduloNumber <- {ModuloNumbers} * 60

num3 = 432
num4 = 153

ModuloNumbers = num3 % num4
moduloNumber = ModuloNumbers * 60

print(moduloNumber)