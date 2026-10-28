'''
i = 1
while i <= 5:
    print(i)
    i = i + 1

print("\n")

i = 1
while i <= 5:
     i = i + 1
     print(i)

print("\n")

i = 1
while i < 5:
  print(i)
  i += 1

print("\n")
i = 1
while i < 5:
    i += 1
    print(i)

print("\n")  
'''

#exercicio#

print("MENU: ")
print("1 - Par ou Ímpar")
print("2 - Compare os Números")
print("3 - Calcule o Dobro")

resp = "s"
while resp == "s":
    print("escolha uma opção [1 / 2 / 3]: ")
    opc = int(input(""))
    print("\n")
    match opc:
        case 1:
            print("Par ou Ímpar")
            num0 = int(input("Digite um número: "))
            if num0 %2 == 0:
                print(f"{num0} é par.")
            else:
                print(f"{num0} é ímpar.")
        case 2:
            print("Compare os Números")
            num1 = int(input("Digite um 1º número: "))
            num2 = int(input("Digite um 2º número: "))
            if num1 > num2:
                print(f"{num1} é maior que {num2}.")
            elif num1 < num2:
               print(f"{num1} é menor que {num2}.")
            else:
                print(f"{num1} é igual a {num2}.")
        case 3:
            print("Calcule o Dobro")
            num3 = int(input("Escolha um número:"))
            dobro = num3 * 2
            print(f"O dobro de {num3} é {dobro}")
        case _:
            print("Opção Invalida")
    print("Deseja continuar [S/N]?")
    resp = input("").lower()
    if resp != "s":
        print("Programa encerrado")
        break