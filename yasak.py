"""
Hiçbir yasal sorumluluk kabul etmiyorum :D
"""

gün= input("Bugün haftaiçi mi haftasonu mu?: ")
if gün == "haftaiçi":
    yaş=int(input("Yaşınız: "))
    if yaş <= 20:
        print("Saat 13.00-16.00 arası sokağa çıkabilirsiniz")
    elif 20 < yaş < 65:
        print("Bütün gün boyunca sokağa çıkabilirsiniz")
    elif 65<= yaş:
        print("Saat 10.00 13.00 arası sokağa çıkabilirsiniz")
        
    
elif gün == "haftasonu":
    yaş=int(input("Yaşınız: "))
    if yaş <= 20:
        print("Saat 13.00-16.00 arası sokağa çıkabilirsiniz")
    elif 20 < yaş < 65:
        print("Saat 10.00-20.00 arası sokağa çıkabilirsiniz")
    elif 65<= yaş:
        print("Saat 10.00 13.00 arası sokağa çıkabilirsiniz")