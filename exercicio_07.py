leituras = []

quantidade = int(input("Quantas leituras você deseja fazer? "))
for i in range(quantidade):
    valor = float(input(f"Digite o valor da {i + 1}ª leitura: "))
    leituras.append(valor)
    print(f'Lista atualizada: {leituras}\n')


print(f"Maior leitura: {max(leituras)}")
print(f"Menor leitura: {min(leituras)}")
print(f"Soma das leituras: {sum(leituras)}")

#  A forma "dificil" de fazer a soma, maximo e minimo seria varrendo o array, desta forma:

# maximo = leituras[0]
# minimo = leituras[0]
# soma = 0
# for leiura in leituras:
#   soma = soma + leitura
#   if leitura > maximo:
#       maximo = leitura
#   if leitura < minimo:
#       minimo = leitura   

# --- Professor mostrando comando len ---

# for i in range(len(leituras)):
#    print(leituras[i])