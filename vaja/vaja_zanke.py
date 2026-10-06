avto = {
    "znamka": "marcedez",
    "model": "amg",
    "letnik": 2021
}

print(avto["model"])

avto["barva"] = "rdeča"

for a, b in avto.items():
    print(f"{a}, : {b}")









sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}


print(sola["naslov"]["posta"], sola["naslov"]["ulica"], sola["naslov"]["kraj"])

for a, b in sola.items():
    print(f"{a}, : {b}")

