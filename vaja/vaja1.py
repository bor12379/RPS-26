x = 5
y = 15
z = -10

print(x-z)
print(x*z) #množenje
print(x/z)

print (10 % 12) #deljenje z ostankom

print (11 % 2) #deljenje z ostankom

print (10**3) #potenca**


#decimalna float stevila

x=3.14
y = 10.012

print(0.5+0.5 == 1) # pravilno
print(0.1+0.2 ==0.3) # narobe 

#STRING - nizi znakov

a = "pozdravljen svet"
b = "dober dan svet"
print(len(a))

st = "22"

print(st * 100)

naslov = "kidriceva 55    "

print(naslov.strip())


ime = "bor gouverneur"
ime = ime.upper()
splitime = ime.split()
print(splitime)

ime = splitime[0]
pri  =splitime [1]
print(ime[0], pri[0])
print(f"{ime[0]}.{pri[0]}")