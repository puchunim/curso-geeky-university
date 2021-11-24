from csv import writer

with open("./filmes.csv", "w") as arquivo:
    escritor = writer(arquivo)
    escritor.writerow(["Título", "Gênero", "Duração", "Classificação"]) # Cabeçalho
    while (filme := input("Digite o nome do filme: ")) != "sair":
        genero = input("Digite o gênero: ")
        duracao = input("Digite a duração: ")
        classificacao = input("Digite a classificação: ")
        escritor.writerow([filme, genero, duracao, classificacao])
