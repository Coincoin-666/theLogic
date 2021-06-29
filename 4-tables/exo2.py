#   exo2 -
#
#   Soit un tableau contenant 5 tableaux de données clients (prénoms, noms et adresses mail).
#   Écrire un algorithme qui sera capable d'afficher chaque donnée de chaque client.
#
#########
#
#   Donc: [1 [1
#               [1][2][3]]
#            [2
#               [1][2][3]]
#            [3
#               [1][2][3]]
#            [4
#               [1][2][3]]
#            [5
#               [1][2][3]]  ]
#
##########
#
#   clientsData
#
#
#   Variables
# 
#       clientsData[5] : array array
#           clientData[3] : string array
#               firstName : string
#               lastName : string
#               email : string
#
# 
#    **Instruction**
# 
#       clientsData[0] <- clientData[0] <- firstName <- "Marlène"
#       clientsData[0] <- clientData[1] <- lastName <- "ChiaPas"
#       clientsData[0] <- clientData[2] <- email <- "tagueule@connasse.gouv.fr"
#       clientsData[1] <- clientData[0] <- firstName <- "Marlène"
#       clientsData[1] <- clientData[1] <- lastName <- "ChiaPas"
#       clientsData[1] <- clientData[2] <- email <- "tagueule@connasse.gouv.fr"
#       clientsData[2] <- clientData[0] <- firstName <- "Marlène"
#       clientsData[2] <- clientData[1] <- lastName <- "ChiaPas"
#       clientsData[2] <- clientData[2] <- email <- "tagueule@connasse.gouv.fr"
#       clientsData[3] <- clientData[0] <- firstName <- "Marlène"
#       clientsData[3] <- clientData[1] <- lastName <- "ChiaPas"
#       clientsData[3] <- clientData[2] <- email <- "tagueule@connasse.gouv.fr"
#       clientsData[4] <- clientData[0] <- firstName <- "Marlène"
#       clientsData[4] <- clientData[1] <- lastName <- "ChiaPas"
#       clientsData[4] <- clientData[2] <- email <- "tagueule@connasse.gouv.fr"
#           For clientData in clientsData do
#               Read(clientData)
#               Write(clientData)


clientData_0 = {
        'firstName': "Marlène",
        'lastName': "ChiaPas",
        'email': "tagueule@connasse.gouv.fr",
}

clientData_1 = {
        'firstName': "Olivier",
        'lastName': "Vereux",
        'email': "tagueule@connasse.gouv.fr",
}

clientData_2 = {
        'firstName': "Manu",
        'lastName': "SaMajesté",
        'email': "tagueule@connasse.gouv.fr",
}

clientData_3 = {
        'firstName': "Jean",
        'lastName': "CasseTete",
        'email': "tagueule@connasse.gouv.fr",
}

clientData_4 = {
        'firstName': "Karine",
        'lastName': "LaConne",
        'email': "tagueule@connasse.gouv.fr",
}

clientsData = [clientData_0, clientData_1, clientData_2, clientData_3, clientData_4]

for client in clientsData:
    print(client)