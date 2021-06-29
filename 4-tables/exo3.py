# exo3 -
#
#   Qu'affichera cet algorithme ?
#
#   
#   Algorithme LogicTest
#
#   Variables    
#
#       logicNumbers[10] : integer array    
#       count : integer
#
#
#   **Instructions**
#
#       For count from 0 to 20 with a step of 2 do
#       logicNumber[count] <- count
#       EndFor     
#       Write(logicNumber[5])
#
#############
#
#    My answer : on compte de 2 en 2 de 0 à 20
#                on écrit le résultat à index[5]
#                donc le 6ème: 10
#
##############

logicNumbers = list(range(0, 22, 2))

print(logicNumbers[5])