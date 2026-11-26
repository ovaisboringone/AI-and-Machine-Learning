readings = [22.5, 23.1, 20.9, 24.0, 21.5, 19.8, 26.2, 23.5]

fahrenheit_readings = [c * 1.8 + 32 for c in readings]
hot_days = [c for c in readings if c > 23.0]

print(fahrenheit_readings)
print(hot_days)