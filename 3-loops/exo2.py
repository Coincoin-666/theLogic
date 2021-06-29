#   exo2 - whileLoop
#
#   Variables
#
#        count : integer
#        bankAccount : integer
#        msg : string
#
#
#   **Instructions**
#
#       bankAccount <- 600
#       count <- 50
#       msg <- "Il vous reste {}€ sur votre compte."
#       While bankAccount > 0 do
#           bankAccount <- bankAccount - count
#           Read(bankAccount)
#           Write(msg)
#       EndWhile
#
#   Huh. Apparemment pour l'instant je ne sais pas
#   encore bien comment prévoir le msg dans une variable
#   alors que le résultat de la dite variable n'est pas
#   encore déterminé. Donc: je fais pas la var "msg".
#   À revoir.

bankAccount = 600
count = 50

while bankAccount > 0:
    bankAccount -= count
    print(f"Il vous reste {bankAccount}€ sur votre compte.")
