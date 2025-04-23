
fahrenheit_temperatures = [32, 68, 100, 50, 212]
print("Fahrenheit temperatures:", fahrenheit_temperatures)


celsius_temperatures = [(f - 32) * 5 / 9 for f in fahrenheit_temperatures]
print("Converted Celsius temperatures:", celsius_temperatures)
