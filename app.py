weight = int(input ("What is your weight?: "))
unit = input ("(L)pds or (K)gs: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print (f'your weight is: {converted}')
else :
    converted = weight // 0.45
    print (f" your weight is: {converted}")