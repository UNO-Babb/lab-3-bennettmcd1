#TempConvert.py
#Name: Bennett McDonald
#Date: 2/9/25 
#Assignment: temp convert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = 80

  tempC = (tempF - 32) * 5.0/9.0

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
