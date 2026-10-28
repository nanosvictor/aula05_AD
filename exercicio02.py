print("Digite cinco nomes e suas idades:")

for (x) in range (1,6):
    nome = input(f"{x}º Nome: ").title()
    idd = int(input(f"{x}ª Idade: "))
    print(f"{x}º Nome: {nome}")
    print(f"{x}ª Idade: {idd}")
    print("\n")
    

print("\nFim do programa")
