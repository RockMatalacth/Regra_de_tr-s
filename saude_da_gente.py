print("PROGRAMA DE REGRA DE TRÊS")
print("A regra será composta de três elementos: \n"
      "A --- B\n"
      "C --- X\n"
      "Será multiplicado em cruz")

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))
X = 1

if A or B or C == int:
    Regra_de_tres = (C*B)/(A*X)
    print(f"Seu X vale: {Regra_de_tres}\n")
else:
    print("Seu número é um número booleano.")

print("Desconto ou aumento?\n")
print("Com base no valor gerado na última conta(X), agora descobriremos se houve um aumento ou desconto se comparado a outros valores: \n\n"
      "Valor gerado --- X\n"
      "Valor como base --- 100%\n"
      "Será multiplicado em cruz")
valor_gerado = Regra_de_tres
X=1
valor_base = int(input("Valor de base:"))
porcentagem = 100

if valor_gerado < valor_base:
    cont_porcentagem = (Regra_de_tres*porcentagem)/(valor_base*X)
    aumento_porcentagem = porcentagem - cont_porcentagem
    print(f"O valor do seu X é:{cont_porcentagem}% de desconto, significa que você tem uma diferença de: {aumento_porcentagem}")
elif valor_gerado > valor_base:
    cont_porcentagem = (Regra_de_tres * porcentagem) / (valor_base * X)
    desconto_porcentagem = cont_porcentagem - porcentagem
    print(f"O valor do seu X é:{cont_porcentagem}%, cujo aumento foi de:{desconto_porcentagem}% em relação aos 100% ")
