"""
Please type in your height in meters
Please type in your weight in kilograms
"""

boy=float(input("Boy:"))
kilo=int(input("Kilo:"))
bki=(kilo / (boy ** 2))
print("Beden kitle endeksiniz:",bki)

if bki<18.5:
    print("Zayıf")

elif 18.5 < bki <25:
    print("Normal")

elif 25 < bki < 30:
    print("Fazla Kilolu")

elif bki > 30:
    print("Obez")
    
else:
    print("Geçerli bir değer girin!")