#ApproxPi.py
#Name:Bennett McDonald
#Date: 2/9/25
#Assignment: aprox pie
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
    realPi = math.pi

    # Ask user for decimal precision (up to 10)
    precision = int(input("Enter the decimal precision (0-10): "))
    
    if precision < 0 or precision > 10:
        print("Invalid precision! Please enter a value between 0 and 10.")
        return

    start = time.time()

    # Calculate pi using the approximation technique
    pi_approximation = input(precision)

    end = time.time()

    elapsedTime = end - start
    print(f"Calculated Pi: {pi_approximation}")
    print(f"Real Pi: {3.141592653589793}")
    print(f"Elapsed time: {elapsedTime:.6f} seconds")

if __name__ == '__main__':
    main()
