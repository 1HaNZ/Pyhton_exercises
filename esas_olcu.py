açı = int(input("Lütfen Açıyı Girin: "))
açı2=açı % 360

if açı2 == 0:
    print("Esas Ölçü:",açı2)

elif açı2 < 0:
    print("Esas Ölçü:",360-açı2)

else: 
    print("Esas Ölçü:",açı2)