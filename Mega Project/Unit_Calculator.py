# Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.
import time


if __name__ == "__main__":
    print("<        Welcome to Unit Calpy       />")
    print(" ")
    print(" ")
    while True:
        unit = input("""1. Kilometers to meters
    2. Meters to Kilometers
    3. Meters to Centimeters
    4. Centimeters to Meters
    5. Centimeters to Milimeter
    6. Milimeter to Centimeter
    Enter the type unit convertion you want : """)
        try:
            unit = int(unit)
        except:
            print("Getting Information")
            time.sleep(2)
            print("Loading......")
            time.sleep(2)
            print("Operation Not Found")
            time.sleep(2)
            print("Sorry, Calpy under Construction.....")
            time.sleep(2)
            break
        num = int(input("Enter the First Number: "))
        # print(" ")
        # print(" ")
        if unit == 1:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print(f"{num} km in meters is {num*1000} m")
        elif unit == 2:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print(f"{num} m in kilometers is {num/1000} km")
        elif unit == 3:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print(f"{num} m in centimeters is {num*100} cm")
        elif unit == 4:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print(f"{num} cm in meters is {num/100} m")
        elif unit == 5:
            print(f"{num} cm in milimeters is {num*10} mm")
        elif unit == 6:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print(f"{num} mm in centimeters is {num/10} cm")
        else:
            time.sleep(2)
            print("Calculating....")
            time.sleep(2)
            print("Working on It....")
            print("Invalid Input  ):")
            break
        print(" ")
        print(" ")