#   exo3 = exo3 + {exo2 + exo1}
#
#   Grâce aux sous-algorithmes (fonctions)
#   que vous avez déjà créés dans les exercices 1 et 2,
#   donner la valeur de resultCalc à la fin de cet algorithme.
#
#
# ----------------------------------------------------------------
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
#       SumNumbers : integer
# 
#   **Instructions**
# 
#       ModuloNumbers <- num3 % num4
#
## 
# ---------------------------------------------------------
#
#
#   MainAlgorithm - CalcNumbers
# 
#   Variables
# 
#       num1 : integer
#       num2 : integer
#       num3 : integer
#       num4 : integer
#       sumNumber : integer
#       moduloNumber : integer
#       resultCalc : integer
# 
#   **Instructions**
# 
#       num1 <- 58
#       num2 <- 64
#       num3 <- 432
#       num4 <- 153
#       sumNumber <- SumNumbers(num1, num2)
#       moduloNumber <- ModuloNumbers(num3, num4)
#       resultCalc <- sumNumber * moduloNumber
# 
##################
#
#
#   My answer : sumNumber : 610
#               moduloNumber : 7560
#               resultCalc : 610 * 7560 = 4,611,600
#
#
##################

num1 = 58
num2 = 64
num3 = 432
num4 = 153

SumNumbers = num1 + num2
sumNumber = SumNumbers * 5

ModuloNumbers = num3 % num4
moduloNumber = ModuloNumbers * 60

resultCalc = sumNumber * moduloNumber

print(resultCalc)