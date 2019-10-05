import random

print("Willkommen im Würfelsimulator v1.0.\n")
spieler1Wuerfe = input("Anzahl Würfe Spieler 1: ")
print("Spieler 1 wird " + spieler1Wuerfe + " Mal würfeln.")
spieler2Wuerfe = input("Anzahl Würfe Spieler 2: ")
print("Spieler 2 wird " + spieler1Wuerfe + " Mal würfeln.")
print("In welchem Modus soll simuliert werden?\n1. Standard\n2. Risikomodus")
modus = input("Bitte die Zahl des Modus eingeben: ")

if modus == 1:
    print("Standard Modus ausgewählt.")

if modus == 2:
    print("Risikomodus ausgewählt.")

anzahlSimulationen = input("Wie oft soll simuliert werden: ")
simulationsErgebnisse = []

for j in range(0, int(anzahlSimulationen)):
    spieler1Counter = 0;
    spieler2Counter = 0;
    for i in range(0, int(spieler1Wuerfe)):
        if random.randint(0,6) == 6:
            spieler1Counter += 1
    for i in range(0, int(spieler2Wuerfe)):
        if random.randint(0,6) == 6:
            spieler2Counter += 1
    simulationsErgebnisse.append(max(0, spieler2Counter - spieler1Counter))

for k in range(1, len(simulationsErgebnisse)+1):
    print("Simulation " + str(k) + " Differenz: " + str(simulationsErgebnisse[k-1]))