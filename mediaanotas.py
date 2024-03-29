medias_alunos = {}

for aluno in range(1, 11):
    notas = []  
    soma_notas = 0

    nome_aluno = input(f"Digite o nome do aluno {aluno}: ")  

    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i} do aluno {aluno}: "))
        notas.append(nota)  
        soma_notas += nota

    media = soma_notas / 4

    if media > 7:
        medias_alunos[nome_aluno] = media

print("Alunos com médias maiores que sete:")
for nome, media in medias_alunos.items():
    print(f"{nome}: {media}")
