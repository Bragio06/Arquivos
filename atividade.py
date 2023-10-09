numero = int(input("digite o numero: "))

with open ('arquivo.txt','w') as arquivo:
    for n in range(numero):
        number = int(input("digite um numero: "))
        arquivo.write(f"{number}\n")      
     

with open ('arquivo.txt','r') as arquivo:
    soma = 0
    quantidade = 0
    for line in arquivo:
        number = int(line)
        soma = soma + number
        quantidade += 1

    r = soma/quantidade
    print(f"{r}")
