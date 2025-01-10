# Função que será responsavel por inverter a string
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Entrada dos dados da string
entrada = input("Digite uma string: ")

# Mostrando a string invertida
print(f"Invertida: {inverter_string(entrada)}")