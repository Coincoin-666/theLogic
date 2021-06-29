#   exo1 - forLoop
#
#   Variables
#
#        count : integer
#        result : integer OR string
#
# 
#   **Instructions**
#
#       count <- 0
#       For count from 0 to 30 with a step of 5 do
#           If result % 2 == 0:
#               Write(result)
#           Else:
#               Write(oops)
#           EndIf
#       EndFor

count = 0

for count in range(0, 30, 5):
    if count % 2 == 0:
        print(count)
    else:
        print("Oops!")