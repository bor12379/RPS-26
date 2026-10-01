"""
def izračunajZmage(igre:list) -> list:
    zmage = []
    for i in range(0, len(igre), 2):
        # print(i, i+1)
        prvi = igre[i]
        drugi = igre[i+1]
        odg = kdoZmaga(prvi, drugi)
        zmage.append(odg)
    return zmage
 
def izdelajStat(zmage: list) -> list:
    zmage1 = 0
    zmage2 = 0
    izen = 0
    for z in zmage:
        if z == 1:
            zmage1 += 1
        elif z == 2:
            zmage2 += 1
        else:
            izen += 1
            
    return [izen, zmage1, zmage2] 
       
    #           'K'     'Š'      ->  1
def kdoZmaga(prvi:str, drugi:str) -> int:
    if prvi == drugi: return 0
    if prvi == 'K' and drugi == 'Š': return 1
    if prvi == 'K' and drugi == 'P': return 2
    if prvi == 'Š' and drugi == 'K': return 2
    if prvi == 'Š' and drugi == 'P': return 1
    if prvi == 'P' and drugi == 'Š': return 2
    if prvi == 'P' and drugi == 'K': return 1
    
    
 
if __name__ == "__main__":
    # poz:   0    1   2   3   4     5   6   7
    igre = ['K', 'Š', 'K', 'P', 'Š', 'P', 'K', 'K']
    z = izračunajZmage(igre)
    s = izdelajStat(z)
    print(z)
    print(s)    
"""

import requests

url="https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"

klic =requests.get(url)

klicJson=klic.json()

print(klicJson["current"]["temperature_2m"])