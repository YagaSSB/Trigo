import math

# Dictionary of special angles
special_angles = { "sin" : {0 : "0", 15 : "(√6-√2)/4", 30 : "1/2" , 45 : "(√2)/2", 60 : "(√3)/2", 75 : "(√6+√2)/4"}, 
                   "cos" : {0 : "1", 15 : "(√6+√2)/4", 30 : "(√3)/2", 45 : "(√2)/2", 60 : "1/2" , 75 : "(√6-√2)/4"},
                   "tan" : {0 : "0", 15 : "(2-√3)", 30 : "(√3)/3", 45 : "1", 60 : "√3", 75 : "(2+√3)"},
                   "cot" : {0 : "undefined", 15 : "(2+√3)", 30 : "√3", 45 : "1", 60 : "(√3)/3", 75 : "(2-√3)"}}

def main():
    while True:
        run = True

        # Takes input from the user and checks if its a valid number
        num = None
        while num == None:
            try:
                mode = int(input("Choose Mode: 1. Degrees 2. Radians 3. Coordinates 4. Exit | "))
                if mode not in range(1,5):
                    raise Exception("Invalid input")
                if mode == 1:
                    num = float(input("Degrees: "))
                elif mode == 2:    
                    num = input("Radians (in π): ")
                    if "/" in num:
                        frac = num.strip().rsplit("/")
                        num = float((int(frac[0]) * 180)/int(frac[1]))
                    else:
                        num = float(num) * 180
                elif mode == 3:
                    cart_cords = input("Coordinates x,y: ").rstrip().rsplit(",")
                    polar_cords = cart_to_polar(cart_cords)
                    num = polar_cords[0]
                    radius = polar_cords[1]
                else:
                    run = False
                    break
            except:
                print("Error: invalid input")
        if not run:
            break

        # Converts angles to radians
        numr = math.radians(num)

        # Estimates the decimal values of the trigonometric functions for the angle provided
        sin = round(math.sin(numr),3)
        cos = round(math.cos(numr),3)
        try:
            tan = round(math.tan(numr),3) 
            cot = round(1/math.tan(numr),3)
            if num%180 - 90 == 0:
                raise Exception("Error: cannot divide by zero")
            elif num%180 == 0:
                raise Exception("Error: cannot divide by zero")
        except:
            if num%180 - 90 == 0:
                tan = "undefined"
            elif num%180 == 0:
                cot = "undefined"

        # Divides the number of radians by pi and rounds to 3 decimal points
        numr = round(numr/math.pi,3)
        
        # Prints results for normal angles
        if mode == 3:
            print(f"Polar coordinates: ({radius},{round(num,2)}°)")
        if mode in [2,3]:
            print(f"Degrees: {round(num,2)}°")
        if num%90 not in special_angles["sin"]:
            print(f"Radians: {numr}π",end="")
            if num >= 360:
                print(f" (equivalent to: Degrees: {round(num%360,2)}°, Radians: {round(numr%2,3)}π)", end="") 
            print(f"\nsin: {sin}, cos: {cos}, tan: {tan}, cot: {cot}")

        # Prints special results for angles that are multiples of 15
        else:
            specials = specialangles(int(num))
            print(f"Radians: {specials[0][0]}", end="")
            if num >= 360: 
                  print(f" (equivalent to: Degrees: {round(num%360,2)}°, Radians: {specials[0][1]})", end="")
            print(f"\nsin: {specials[1]}, cos: {specials[2]}, tan: {specials[3]}, cot: {specials[4]}")
        print()

# Gives fractioal value for radians for angles that are multiples of 15: 
def specialanglesr(num):
    numr_s_numerator = int(num/15)
    numr_s_denominator = 12
    for i in [2,2,3]:
        if numr_s_numerator % i == 0:
            numr_s_numerator = int(numr_s_numerator/i)
            numr_s_denominator = int(numr_s_denominator/i)
    numr_s_r = f"{numr_s_numerator%(2*numr_s_denominator)}"
    if numr_s_numerator == 1:
        numr_s_numerator = ""
        numr_s_r = "π" 
    if numr_s_denominator == 1:
        numr_s_r += "π"
        numr_s = f"{numr_s_numerator}π"
    else:
        numr_s = f"{numr_s_numerator}π/{numr_s_denominator}"
        numr_s_r += f"π/{numr_s_denominator}"
    return [numr_s, numr_s_r]

# Gives fractional and square root values for angles that are multiples of 15:
def specialangles(num):
    sign = "-"
    if 0 <= num%360 < 90:
        sin_s = special_angles["sin"][num%90]
        cos_s = special_angles["cos"][num%90]
        tan_s = special_angles["tan"][num%90]
        cot_s = special_angles["cot"][num%90]
    elif 90 <= num%360 < 180:
        sin_s = special_angles["cos"][num%90]
        if num%90 == 0:
            sign = ""
        cos_s = sign + special_angles["sin"][num%90]
        tan_s = sign + special_angles["cot"][num%90]
        cot_s = sign + special_angles["tan"][num%90]
    elif 180 <= num%360 < 270:
        cos_s = sign + special_angles["cos"][num%90]
        if num%90 == 0:
            sign = ""
        sin_s = sign + special_angles["sin"][num%90]
        tan_s = special_angles["tan"][num%90]
        cot_s = special_angles["cot"][num%90]
    elif 270 <= num%360 < 360:
        sin_s = sign + special_angles["cos"][num%90]
        cos_s = special_angles["sin"][num%90]
        if num%90 == 0:
            sign = ""
        tan_s = sign + special_angles["cot"][num%90]
        cot_s = sign + special_angles["tan"][num%90]
    return [specialanglesr(num), sin_s, cos_s, tan_s, cot_s]

# Converts Cartesian Coordinates to Polar Coordinates
def cart_to_polar(cords):
    cords[0] = float(cords[0])
    cords[1] = float(cords[1])
    if cords[0] != 0:
        tan = cords[1]/cords[0]
        if cords[0] > 0 and cords[1] >= 0:
            degrees = round(math.degrees(math.atan(tan)),3)
        elif cords[0] < 0 and cords[1] >= 0:
            degrees = 180 + round(math.degrees(math.atan(tan)),3)
        elif cords[0] < 0 and cords[1] <= 0:
            degrees = 180 + round(math.degrees(math.atan(tan)),3)
        elif cords[0] > 0 and cords[1] <= 0:
            degrees = 360 + round(math.degrees(math.atan(tan)),3)       
    else:
        if cords[1] > 0:
            degrees = 90
        elif cords[1] < 0:
            degrees = 270
        else:
            degrees = 0
    radius = round(math.sqrt((cords[0]**2) + (cords[1]**2)),2)

    return [degrees, radius]


if __name__ == "__main__":
    main()