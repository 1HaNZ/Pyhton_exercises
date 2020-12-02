def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    return a/b

a=0
b=0
islem=()

while (True):
    
    a = int(input("Ilk sayi: "))
    islem = input("Islem: ")
    b = int(input("Ikinci sayi: "))

    if (islem != None):
        if (islem == "+"):
            print("Toplam: ",topla(a,b))
        elif (islem == "-"):
            print("Fark: ",cikar(a,b))
        elif (islem == "/"):
            print("Bolum: ",bol(a,b))
        elif (islem == "*"):
            print("Carpim: ",carp(a,b))
        else:
            print("Gecersiz deger...")
    
    q = input("Cikis? [e/h] ")
    if (q == "e" or q == "E"):
        break