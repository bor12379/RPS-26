
def hello():
    o = input("kateri oddelek si")
    if o.lower() == "1.ri":
        print(f"hello {o} 3")
    else:
        print(f"hello {o} ")

def poštevanka():
    x = int(input("izberi si število: "))
    a = 1
    while a <=10:
        print("...")
        a +=1

if __name__ =="__main__":
    # hello()
    poštevanka()

