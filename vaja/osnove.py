
#vaja1
"""
doma =int(input("koliko golov so zadeli domači: "))
gostje = int(input("vnesi koliko golov so zadeli gostje: "))
print(f"rezultat je bil {doma} - {gostje}")
print(f"popravljen rezultat {gostje} - {doma}")
a = doma + gostje
print(f"skupaj {a}")
"""
#vaja 2



"""
minute = int(input("vnesi minute igranja: "))
dnevi = minute//1440
ure = (minute%1440) //60
minute= minute%60

print(f"{dnevi}dni, {ure}ure ,{minute}minute.")
"""
#VAJA 3
"""
dijaki = int(input("vnesi število dijakov: "))
pice = float(input("vnesi število pic: "))
spic = (dijaki+2) //3 
skupna_cena = pice*spic
na_dijaka = skupna_cena/dijaki
print(spic)
print(skupna_cena)
print(f"{na_dijaka} €")
"""
#vaja 4
"""
cena = 0
x = int(input("vnesi starsot: "))
y = input("vnesi dan: ")
if x < 0 or x == 0:
    print(f"Neveljavna starost.")
else:
    if y == "torek":
        cena = - 2
    if x <= 5:
        cena = "brezplačno"
    elif x > 6 and x <= 17:
        cena = cena + 5
    elif x > 18 and x <= 64:
        cena = cena + 8
    else:
        cena = cena + 6
    
print(f"{cena} €")
"""




