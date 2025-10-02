placa = input()
nome = input()
velocidade = int(input())
velocidade_max = int(input())
multado_antes = input()
pagar = input()

classificacao = "Nenhuma"
multa = 0.0
pontos = 0
suspensao = False

if velocidade > velocidade_max:
    excesso = (velocidade - velocidade_max) / velocidade_max * 100

    if excesso <= 20:
        classificacao = "Leve"
        multa = 130.16
        pontos = 0
    elif excesso <= 50:
        classificacao = "Grave"
        multa = 195.23
        pontos = 5
    else:
        classificacao = "Gravíssima"
        multa = 880.41
        pontos = 7
        suspensao = True

multa_base_exibicao = multa
reincidencia = False

if (classificacao == "Grave" or classificacao == "Gravíssima") and multado_antes.strip().lower() in ["sim", "s"]:
    multa *= 2 
    reincidencia = True

print(f"Placa: {placa}")
print(f"Motorista: {nome}")
print(f"Velocidade registrada: {velocidade} km/h")
print(f"Velocidade máxima permitida: {velocidade_max} km/h")

if classificacao == "Nenhuma":
    print("Infração: Nenhuma. Nenhuma penalidade aplicada.")
else:
    texto = f"Infração: {classificacao} - Multa de R$ {multa_base_exibicao:.2f}, {pontos} pontos na CNH"
    if suspensao:
        texto += " e suspensão da carteira."
    else:
        texto += "."
    print(texto)

    if reincidencia:
        print("Atenção: Multa DOBRADA por reincidência!")

    if suspensao:
        print("Atenção: CNH suspensa! Compareça ao Detran.")
        print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")

    if pagar.strip().lower() in ["sim", "s"]:
        valor_final = multa * 0.8
        print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ {valor_final:.2f}")
