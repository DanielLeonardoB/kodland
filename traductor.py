import random

eng_words = ['Hi','Bye','Task', 'Programm']
sp_words = ['Hola','Adiós','Tarea', 'Programa']
score = 0
respuesta = "S"
while respuesta == "S":
  mode = int(input("Elige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n"))
  while mode not in range(0,2):
      mode = int(input("Símbolo no válido. Elija 0 o 1. \n"))
  if mode == 1:
      print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")
      for i in range(10):
          number = random.randint(0, len(eng_words)-1)
          print("Cómo deberíamos traducir " + eng_words[number])
          if input().capitalize() == sp_words[number]:
              print("¡¡¡Genial!!!")
              score += 1 
              print("*"*10)
              print(f"Puntuacion = {score}")
              print(f"Ronda = {i+1}")
              print("*"*10)
          else:
              print("No, no del todo... La palabra correcta es - " + sp_words[number])
              print("*"*10)
              print(f"Puntuacion = {score}")
              print(f"Ronda = {i+1}")
              print("*"*10)
  else:
      word = input("Escribe una palabra en español: ").capitalize()
      translate = input("Escriba la traducción de esta palabra: ").capitalize()
      if len(word) > 0 and len(translate) > 0:
          sp_words.append(word)
          eng_words.append(translate)
          print("¡La palabra se ha añadido correctamente!")
  respuesta = str(input("Quiere seguir jugando S/N ")).upper()

          eng_words.append(translate)
          print("¡La palabra se ha añadido correctamente!")
  respuesta = str(input("Quiere seguir jugando S/N ")).upper()
