consumo = float(input("Digite o consumo em kWh: "))
custo_base = consumo * 0.6

resposta_verao = input("Estamos no perído de verão? (S/N)").strip().lower()

verao = not (resposta_verao == "n")

if consumo > 300 and verao:
    taxa_bandeira = 15.00
    print("Bandeira: Vermelha (Consumo crítico no verão)")
elif consumo > 200 and verao:
    taxa_bandeira = 7.5
    print("Bandeira: Amarela (Consumo elevado no verão)")
else:
    taxa_bandeira = 0.0
    print("Bandeira: Verde (Consumo sob controle)")

valor_total = custo_base + taxa_bandeira
print(f"O custo total do consumo de {consumo} kWh é R$ {valor_total:.2f}")
