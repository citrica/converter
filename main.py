
while True:

    km = float(input("Enter km: "))
    miles = km*0.621
    print(str(km) + " km = " + str(miles) + " miles")
    OK = input("Do you want to do another conversion? (Y/N) ")
    while OK.lower() != "y" and OK.lower() != "n":
        OK = input("Please, enter N or Y ")
    if OK.lower() == "n":
        break










