import webbrowser


ans = input("Would you like to open the Omni Conversion Calculator? (y/n) :")
url = "https://www.omnicalculator.com/conversion"

if ans == "y":
    webbrowser.open(url)
else:
    print("OK...Good-bye")
    exit()
