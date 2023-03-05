import webbrowser


ans = input("Would you like to open the test command website (y/n) :")
url = "https://linuxhint.com/bash-test-command/"


if ans == "y":
    webbrowser.open(url)
else:
    print("OK...Good-bye")
    exit()
