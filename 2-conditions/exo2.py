#   exo2 - algoDivideByFour
#
#   Variables
#
#       num1 : float
#       num2 : float
#       result : float
#
#   **Instructions**
#
#       result <- num1 / num2
#       If result%4 <- 0:
#           Write("Yes")
#       Else
#           Write("No")
#       EndIf

num1 = 40
num2 = 10

result = num1 / num2

if result % 4 == 0:
    print("yes")
else:
    print("no")
