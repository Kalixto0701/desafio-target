numero = input("Qual número você gostaria de saber se pertencia a sequencia de fibonacci? ")

numero = int(numero)

sequencia_fibonacci = [0, 1]

while sequencia_fibonacci[-1] < numero:
    sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])
if numero in sequencia_fibonacci:
    print("O número pertence à sequência!")
else:
    print("O número escolhido não pertence à sequência!")