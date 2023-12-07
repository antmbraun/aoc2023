input = open("input.txt", "r")
strs = input.read().split("\n")

total = 0

for str in strs:
  calibration_values = None 

  for c in str:
    if c.isdigit():
      if not calibration_values:
        calibration_values = [c, c]
      else:
        calibration_values[1] = c

  calibration_value_int = int("".join(calibration_values))
  total += calibration_value_int

print(total)




    
  