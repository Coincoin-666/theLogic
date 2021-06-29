#   exo1 -
#
#   Soit un tableau contenant 10 nombres. Écrire un algorithme qui permettra de faire
#   la multiplication de ces 10 nombres entre eux et d'affecter le résultat à une variable resultCalc.
#
#
#   Variables
#
#       count[10] : integer array
#       resultCalc : integer
#
#
#   **Instructions**
#
#       For count from 0 to 9 do
#           resultCalc <- count[n] * count[n+1]
#           Read(resultCalc)
#           Write(resultCalc)
#       EndFor

counts = list(range(1, 11))

print(counts)

for num in counts:
    resultCalc = num*(num+1)
    print(resultCalc)