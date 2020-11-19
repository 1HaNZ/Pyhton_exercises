print("""*******************
HESAP MAKİNESİ
    
İŞLEMLER:
1-TOPLAMA İŞLEMİ
2-ÇIKARMA İŞLEMİ
3-ÇARPMA İŞLEMİ
4-BÖLME İŞLEMİ
      
*******************""")

a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))

işlem=int(input("İşlem:"))

if işlem==1:
    print("{} ve {} toplamı {}".format(a,b,a+b))
    
elif işlem==2:
    print("{} ve {} farkı {}".format(a,b,a-b))
    
elif işlem==3:
    print("{} ve {} çarpımı {}".format(a,b,a*b))
    
elif işlem==4:
    print("{} ve {} bölümü {}".format(a,b,a/b))
    
else:
    print("Geçerli Bir Değer Giriniz!")
