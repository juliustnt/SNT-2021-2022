def main():
  f= open("Population.csv", "r", encoding='utf=8') 
  entete = f.readline()
  popEurope = 0
  ligne = f.readline()
  while ligne !="":
    nom,pop,sup,den = ligne.split(";")
    popEurope = popEurope + int(pop)
    densEurope = den
    ligne = f.readline()
  print("Population totale :", popEurope)
  print("Density totale :", densEurope, "hab/km^2")
  f.close

choisis_exo = input("Quelle exercice voulez-vous? ")

if choisis_exo == "6": 
  main()
elif choisis_exo == "5":
  print("fart")
else:
  "i farted"