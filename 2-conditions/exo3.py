#   exo3 - algoCalcIMC
#
#   Variables
#
#       weight : float
#       size : float
#       imcResult : float
#
#   **Instructions**
#
#       weight <- 85.6
#       size <- 1.75
#       imcResult <- weight / (size * size)
#       If imcResult <= 18.5 and imcResult <= 25 then
#           Write("Votre IMC est normal, votre IMC est de: " imcResult)
#       Else
#           Write("Surveillez votre poids, votre IMC est de: " imcResult)
#       EndIf
#
#
################
#
#   My answer: 85.6 / (1.75 * 1.75)
#              85.6 / 3.0625
#            = 27.9510
#
#   So the answer would be "Surveillez votre poids, votre IMC est de 27.95"
#
################
#
#   Python answer:

weight = 85.6
size = 1.75
imcResult = weight / (size * size)

if 15 <= imcResult <= 25:
    print(f"Votre IMC est normal, votre IMC est de: {imcResult}")
else:
    print(f"Surveillez votre poids, votre IMC est de: {imcResult}")
