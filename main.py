Aufgaben=[]
with open("aufgaben.txt","r") as datei:
    for zeile in datei:
        aufgabe=zeile.strip()
        Aufgaben.append(aufgabe)
while True:
  wahl=input("Wähle 1-4")
  if wahl == "1":
        task=input("Was ist deine Aufgabe?")
        Aufgaben.append(task)
        with open("aufgaben.txt","w") as datei:
         for aufgabe in Aufgaben:
            datei.write(aufgabe+"\n")     
  elif wahl == "2":
        for nummer,aufgabe in enumerate(Aufgaben,start=1):
             print(nummer,aufgabe)
  elif wahl=="3":
        aufgabe_löschen=input("Welche Aufgabe möchtest du löschen?").strip()
        if aufgabe_löschen in Aufgaben:
            Aufgaben.remove(aufgabe_löschen)
            with open("aufgaben.txt","w") as datei:
                for aufgabe in Aufgaben:
                    datei.write(aufgabe+"\n")
        else:
            print("Aufgabe nicht gefunden")
  elif wahl == "4":
        break 
 