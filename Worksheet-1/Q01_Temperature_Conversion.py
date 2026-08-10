def celsius_to_fahrenheit(celsius):
  fahrenheit =  (celsius * 9/5) + 32
  return fahrenheit
  
celsius = float(input("Enter Temperature in Celsius:"))
print(celsius_to_fahrenheit(celsius))
