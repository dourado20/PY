municipio = (input("Escreva o nome do seu municipio:"))
eleitores = int(input("EScreva o número de eleitores:"))
votos = int(input("Escreva a quantidade de votos do candidato mais votado:")) 

if eleitores > 200.000 and votos < (0.5 * eleitores):
  print ("Terá o segundo turno")
else:
   print("Não terá o segundo turno")