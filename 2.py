massa = float(input("масса вашего тела: "))

rost = float(input("ваш рост: "))

index_mass123 = float(massa / (rost*rost))

if index_mass123 > 25:
    print('у вас перевес')
if index_mass123 < 18.5:
    print ('у вас недовес')
else:
    print('у вас идеальный вес')
