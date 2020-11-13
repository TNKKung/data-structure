def easurSpeed(n):
    if (n >= 0 and n <= 51.99):
        return 'Breeze'
    elif (n >= 52 and n <= 55.99) :
        return 'Depression'
    elif (n >= 56 and n <= 101.99) :
        return 'Tropical Storm'    
    elif (n >= 102 and n <= 208.99) :
        return 'Typhoon'
    elif (n >= 209) :
        return 'Super Typhoon'

print(" *** Wind classification *** ")

n = float(input("Enter wind speed (km/h) : "))

print("Wind classification is " + easurSpeed(n)+".")
