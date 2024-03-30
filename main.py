palabras = {"LOL": "una respuesta a algo gracioso", "CRINGE" :"algo raro o embarazoso",
"ROFL": "una respuesta a una broma", "SHEESH" : "ligera desaprobación",
"CREEPY": "aterrador, siniestro", "AGGRO": "ponerse agresivo/enojado"}
print("Lista de palabras ")
for i in palabras:
    print(i)
incognita = str(input("Ingrese una palabra que desea conocer su significado").upper())
if incognita in palabras:
   print("El significado de", incognita, "es:", palabras[incognita])
else:
    print("La palabra debe estar dentro de la lista")
    