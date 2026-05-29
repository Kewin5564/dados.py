# Solicita os dados ao usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Grava os dados em um arquivo chamado dados.txt
with open("dados.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")

# Lê o arquivo e mostra os dados na tela
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("\nDados gravados no arquivo:")
    print(conteudo)
