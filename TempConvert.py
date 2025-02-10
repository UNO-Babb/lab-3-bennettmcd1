#TempConvert.py
#Name: Bennett McDonald
#Date: 2/9/25 
#Assignment: temp convert


def main():
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))

  tempC = (tempF - 32) * 5.0/9.0

  celsius_rounded = round(celsius, 1)
  
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
