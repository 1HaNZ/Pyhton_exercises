print("""
********************************
    Program Başlatılıyor...

    Çıkmak İçin q ya basın

********************************
""")

while True:
    n =  input("Sayı:")
    if (n == "q"):
        print("Programdan çıkılıyor...")
        break
    n = int(n)

    f = int(1)
    for i in range(2,n+1):
        f *= i

    print("Faktoriyel:",f)