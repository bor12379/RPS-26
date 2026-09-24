def vnos(s:list):
    while True:
        izdelek = input("vnesi: ")
        if izdelek =="":
            break
        s.append(izdelek)

def izpis(s:list):

    print("-------------------------")
    for index in range(len(s)):
        print(f"({index +1}) {s[index]}")

def briši(s:list):
    brisi = input("briši: ").lower()
    print("brisem", end="")
    while brisi in s:
        s.remove(brisi)
        print("*", end="")
    print()

def posodobi(s:list):
    stara =input("posodobi: ").lower()
    nova = input("nova: ").lower()
    for index in range(len(s)):
        if stara == s[index]:
            s[index] = nova

if __name__ == "__main__":
    db = []
    vnos(db)
    izpis(db)
    briši(db)
    izpis(db)
    posodobi(db)
    izpis(db)