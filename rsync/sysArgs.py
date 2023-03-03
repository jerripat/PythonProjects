# usr_str=input("Enter a string: ")
# usr_action=input("Enter your action on your string (valid actions are: lower/upper/title: ")
import sys

if len(sys.argv) != 3:
    print("Invalid number of arguments")
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]


if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option was invalid")
