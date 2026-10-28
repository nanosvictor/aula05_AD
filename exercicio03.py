print("Mostrar os números pares entre 0 a 100:")
print("\n")
for x in range(0,101):
    if x % 2 == 0:
        print (x)





print("Mostrar os números pares entre 1 a 111:")
print("\n")
for (y) in range (1,112):
    if y % 2 == 1:
        print (y)





print("Teste 5 números e verifique se é par ou ímpar:")
print("\n")
for (i) in range(1,6):
    numero = int(input(""))
    if (numero % 2 == 0):
        print(f"{numero} é um número PAR!")
    else:
        print(f"{numero} é um número ÍMPAR!")
  




print("Faça uma tabuada de multiplicação com um número escolhido pelo usuário:")
print("\n")
b = int(input("\nDigite um número: "))
for (a) in range (0,11):
    c = a * b
    print (f"{a} x {b} = {c}")
    
    #funcionaria igual este 
    #print (f"{b} X {a} = {a*b}")
    



#ok



    #teste 5 entradas de nomes, prova1, prova2, prova3
    #faça a media e mostre se aluno >=7 aprovado >=5 recuperação <5 reprovado
print("Conceito 4º COC:")
print("\n")
for (q) in range(1,6):
    print(f"{q}º Aluno")
    nome = input("Nome: ").title()
    turma = input("Turma: ")
    nota1 = float(input("Nota 1ª avaliação: ").replace(",","." ))
    nota2 = float(input("Nota 2ª avaliação: ").replace(",","." ))
    nota3 = float(input("Nota 3ª avaliação: ").replace(",","." ))
    media = (nota1+nota2+nota3) / 3
    if (media >= 7):
       conceito = "APROVADO"
    elif(media >= 5):
        conceito = "RECUPERAÇÃO"
    elif(media < 5):
       conceito = "REPROVADO"            
    print(f"\nSituação do aluno {nome} com média {media:.1f} da turma {turma}: {conceito}".replace(".",","))
    print("\n")
