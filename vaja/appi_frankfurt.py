
import requests
"""
url = "https://api.frankfurter.dev/v1/latest"

odgovor = requests.get(url, params={"symbols": "USD,GBP,CHF,JPY"})

if odgovor.status_code != 200:
    print("Napaka pri klicu API-ja.")
    exit()

podatki = odgovor.json()
tecaji = podatki["rates"]

print("Tečaji na dan", podatki["date"])

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj valut:", len(tecaji))
"""

#vaja 2



podatki = requests.get("https://api.frankfurter.dev/v1/latest").json()
tecaji = podatki["rates"]


def v_tujo(evri, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return evri * tecaji[valuta]


def v_evre(znesek, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return znesek / tecaji[valuta]


evri = float(input("Znesek v EUR: "))
valuta = input("Valuta: ").upper()

tuje = v_tujo(evri, valuta, tecaji)

if tuje is None:
    print("Valuta", valuta, "ne obstaja.")
else:
    print(evri, "EUR =", round(tuje, 2), valuta)
    nazaj = v_evre(tuje, valuta, tecaji)
    print(round(tuje, 2), valuta, "=", round(nazaj, 2), "EUR")





