#   exo2 - Hello {name}
#
#
#   Variables
#
#       invitation : string
#       name : input
#       hello : string
#       greetings : string
#
#
#   **Instructions**
#
#       hello <- "Hello, "
#       invitation <- "Please enter your name:"
#       Read(invitation)
#       Write(invitation)
#       name <- input
#       Read(hello)
#       Read(name)
#       Write(hello + name)

invitation = "Please enter your name:"
hello = "Hello, "

print(invitation)
name = input()

print(hello + name)