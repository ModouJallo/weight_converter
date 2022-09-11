# Takes a user inputs weight and converts it to either Kilograms or pounds 
weight = int(input('Enter your weight: '))
unit = input("Enter L for (lb) or K for (kg): ")

if unit.upper == 'L':
  convert = round(weight / 0.454)
  print(f" you weigh {convert} Pounds")
else:
  convert = round(weight * 0.454)
  print(f"You weigh {convert} Kilograms")

