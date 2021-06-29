#   exo1 - algoAgeGender
#
#   Variables
#
#       age : integer
#       male : boolean
#       female : boolean
#
#   **Instructions**
#
#       Write("Hi, how old are you?")
#       age <- input
#       Read(age)
#       Write("Please enter your gender (male or female)")
#       gender <- input
#       Read(gender)
#       If age >= 18 AND gender == female then:
#           Write("Hello miss. You are old enough to vote.")
#       Elif age < 18 and gender == female then:
#           Write("Hello sir. You are old enough to vote.")
#       Elif age >= 18 AND gender == male then:
#           Write("Hello miss. You are old enough to vote.")
#       Elif age < 18 and gender == male then:
#           Write("Hello sir. You are old enough to vote.")
#       EndIf

age = input("Hello, how old are you?")
age_as_number = int(age)
gender = input("Please select your gender, male (m) or female(f):")


if age_as_number >= 18 and gender == "f":
    print("Hello miss. You're old enough to vote.")
elif age_as_number < 18 and gender == "f":
    print("Hello miss. Sorry come back in a few years!")
elif age_as_number >= 18 and gender == "m":
    print("Hello sir. You're old enough to vote.")
elif age_as_number < 18 and gender == "m":
    print("Hello sir. Sorry come back in a few years!")
elif gender != "f" or "m":
    print("Please select one of the following m or f (CaSe SeNsItiVe")
