un1=float(input("escreva a media da unidade 1:"))
un2=float(input("escreva a media da unidade 2:"))

mediafinal=(un1 + un2)/2
if mediafinal == 7:
  print("Você está APROVADO,e sua media final é",mediafinal)
elif mediafinal<3:
   print("Você está REPROVADO,e sua media final é",mediafinal)
else:
   print("Você irá fazer a prova final",mediafinal)